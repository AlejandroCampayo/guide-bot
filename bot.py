"""
INFORMACIÓ BÀSICA
-----------------
"Bot.py" és un módul que  conté tot el codi relacionat amb el bot de
Telegram i utilitza el mòdul guide.
La seva tasca és reaccionar a les comandes i als canvis de localització
dels usuaris per poder-los guiar.

VARIABLES GLOBALS
-----------------
-Graph: Conté el graf d'Osmnx de Barcelona, que és el que es dona per
defecte a l'usuari. No canvia en cap moment.
-Places: Vector de paraules que desa el nom dels llocs dels quals algún
dels usuaris ha descarregat el graf. Desde que aquests han estat
descarregats, aquests grafs estaràn disponibles per a qualsevol usuari
sense necessitat d'esperar.

INFORMACIÓ DEL USUARI (context.user_data)
-----------------------------------------
-'place': Conté el nom del lloc en el que considerem que es troba l'usuari.
Per defecte s'inicialitza com 'Barcelona'.
-'destination': Conté les coordenades (lat, lon) del destí de l'usuari.
-'location': Conté les coordenades (lat, lon) de l'última actualització
de la posició de l'usuari.
-'mygraph': Conté el graf d'Osmnx del lloc on considerem que es troba
l'usuari.
-'route': Conté la ruta que ha de seguir l'usuari per arribar fins el seu
destí. Per una explicació més detallada d'aquest punt, revisa el document
guide.py.

FUNCIONS
--------
Aquest mòdul conté 7 funcions públiques i dues d'auxiliars i privades.
"start", "help", "where", "imin", "go", "cancel", "author", "_gir" i
"_ordre" són les funcions de les que disposa, usahelp(bot."nom de la
funció") per obtenir més informació.
"""


__author__ = 'Alejandro Campayo Fernández'


import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler, MessageHandler, Filters
import guide
import random
import os


Graph = guide.download_graph('Barcelona, Spain')
guide.save_graph(Graph, 'Barcelona_GuideBot')
print("Downloaded, ready to start.")
#Graph = guide.load_graph('Barcelona_GuideBot')
Places = ['Barcelona']


def start(update, context):
    """
    Funció: Inicia el chat i insereix els valors predeterminats a
    l'informació de l'usuari. Concretament, si és la primera vegada
    que s'executa, fa que la seva ciutat sigui la de Barcelona i el
    seu graf sigui el corresponent a aquesta ciutat.
    ----------
    Output: Missatge informatiu al chat de telegram.
    """

    if 'mygraph' not in context.user_data:
        context.user_data['mygraph'] = Graph
    if 'place' not in context.user_data:
        context.user_data['place'] = "Barcelona"

    name = update.effective_chat.first_name
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='''
Hola, %s!
Sóc en GuideBot. 😄
Siusplau, envia'm un missatge amb el text */help* si vols apendre a utilitzar-me.
'''
                             % (name), parse_mode=telegram.ParseMode.MARKDOWN)


def help(update, context):
    """
    Funció: Envia missatges a l'usuari per tal que aquest
    entengui com utilitzar el bot correctament.
    """
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='''
*El meu objectiu és guiar-te!*
Per fer-ho només has de donar-me les ordres adients.
A continució t'explico com fer-ho.''',
        parse_mode=telegram.ParseMode.MARKDOWN)

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='''
Disposo de 4 funcions:
*/author*, */go*, */imin* i */cancel*.
Per executar-les simplement has d'enviar-me un missatge com els següents:
*/author*, */go* seguit del lloc on vols que
et guiï (Exemple: _/go Sagrada Família_),
*/imin* seguit del municipi en el que et trobes (Exemple: _/imin Tarragona_)
o */cancel*.''',
        parse_mode=telegram.ParseMode.MARKDOWN)

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='''
*/author* t'envia un missatge amb el nom de la persona que em va crear.
*/go (destí)* inicia la ruta necessària per arribar des d'on ets fins al
destí demanat.
*/imin (municipi)* et permet canviar de municipi , ja que per defecte
només sóc capaç de guiar-te per Barcelona.
*/cancel* cancel·la la ruta que estàs realitzant per tal que poguem
iniciar-ne una de nova. Només cal executar-la quan decideixis canviar de
destí mentre t'estigui guiant.''',
        parse_mode=telegram.ParseMode.MARKDOWN)


def where(update, context):
    """
    Funció: Obte l'última actualització de l'ubicació de l'usuari i
    canvia la variable corresponent a la localització d'aquest.
    Si l'usuari té una ruta a seguir, "where" comprovarà si s'ha arribat
    al següent node. Si és així, s'envia un missatge informatiu per tal
    de guiar fins el següent punt.
    ----------
    Output: Missatge informatiu al chat de telegram.
    """
    print("Ubication from %s received." %
          (update.effective_chat.username))

    had_location = True
    if not 'location' in context.user_data:
        had_location = False

    message = update.edited_message if update.edited_message else update.message
    lat, lon = message.location.latitude, message.location.longitude
    context.user_data['location'] = (lat, lon)

    if not had_location:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='Gràcies, ara ja em pots dir on vols anar!')
        had_location = True

    if 'route' in context.user_data:
        dist = guide._distance_two_points(
            context.user_data['location'], context.user_data['route'][0]['mid'])

        print("User %s is %d meters far from the next checkpoint." %
              (update.effective_chat.username, dist))

        # Si la distància entre les coordenades és inferior a 10 metres,
        # considero que he arribat.
        if dist < 10:
            print("%s has achieved a checkpoint." % update.effective_chat.username)
            try:
                # elimino el primer element de la ruta per veure el següent el
                # pròxim cop.
                context.user_data['route'].pop(0)
                ordre = _ordre(context.user_data['route'][0])
                context.bot.send_message(
                    chat_id=update.effective_chat.id,
                    text=ordre)
            except:
                # no puc fer pop perquè tinc vector de mida 0, he acabat la ruta
                context.bot.send_message(
                    chat_id=update.effective_chat.id,
                    text='''Hem acabat la ruta! Ha estat un plaer guiar-te. 😄''')
                del context.user_data['destination']
                del context.user_data['route']


def _ordre(info):
    """
    Funció: Donada la informació d'un node retorna l'ordre
    necessària per guiar l'usuari fins el següent node.
    ----------
    Input: Diccionari.
    ----------
    Output: Ordre a seguir.
    ----------
    Precondició: Length i current_name no són "None".
    """
    gir = _gir(info['angle'])
    ordre = "Has arribat a %s. Continua recte %d metres i després %s" % (
        info['current_name'],
        info['length'], gir)
    if info['next_name']:
        ordre += " cap a %s." % (
            info['next_name'])
    return ordre


def _gir(angle):
    """
    Funció: Donat un angle entre dos carrers, retorna un text amb el gir
    que l'usuari ha de fer per arribar al següent carrer.
    ----------
    Input: Double o None (si ens trobem a l'últim node).
    ----------
    Output: Text amb el gir que cal fer.
    ----------
    Precondició: L'angle donat es troba entre 0 i 360 graus.
    """
    if not angle:
        return "hauràs arribat al teu destí."
    elif angle >= 337.5 or angle < 22.5:
        return "continua recte"
    elif angle >= 22.5 and angle < 67.5:
        return "gira lleugerament a la dreta"
    elif angle >= 67.5 and angle < 112.5:
        return "gira a la dreta"
    elif angle >= 112.5 and angle < 157.5:
        return "gira a la dreta de manera pronunciada"
    elif angle >= 157.5 and angle < 202.5:
        return "fes un gir molt pronunciat"
    elif angle >= 202.5 and angle < 247.5:
        return "gira a l'esquerra de manera pronunciada"
    elif angle >= 247.5 and angle < 292.5:
        return "gira a l'esquerra"
    elif angle >= 292.5 and angle < 337.5:
        return "gira lleugerament a l'esquerra"
    else:
        raise ValueError("Angle no vàlid")
        return "..."


def imin(update, context):
    """
    Funció: Canvia el graf i el lloc on es considera que es troba
    l'usuari i s'afegeix al vector global "Places" el nom del lloc
    del qual hem descarregat el mapa per evitar que aquest mapa
    s'actualitzi de forma innecessària.
    Permetem així que el bot pugui guiar a llocs fora de Barcelona.
    Tot i així, no es contemplen rutes que vagin d'un graf a un altre.
    ----------
    Input: Nom del lloc dins del qual vull realitzar la ruta.
    ----------
    Output: Fitxer amb el nom del municipi seguit de "_GuideBot",
    missatge de text informatiu al chat de telegram i s'escriu al
    terminal el nom del document creat per desar el graf.
    ----------
    Precondició: El lloc forma part de la llibreria d'Osmnx.
    """

    place = update.message.text[6:]
    fitxer = "%s_GuideBot" % (place)

    try:
        if place not in Places:
            Places.append(place)

            # Com que la descarrega pot trigar un temps, es demana a l'usuari
            # que esperi a un missatge de confirmació després d'aquest.
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text='''
Aquesta acció pot trigar una mica.
*Siusplau espera a que et doni més informació.* ⏱️''',
                parse_mode=telegram.ParseMode.MARKDOWN)

            print('Downloading... (users may have a delay)')

            new_graph = guide.download_graph(place)
            context.user_data['mygraph'] = new_graph

            print('Creating ' + fitxer + ' file')
            guide.save_graph(new_graph, fitxer)
            print('Downloaded and saved in ' + fitxer)
            print('Maps available: ' + str(Places))

            # Missatge de confirmació per informar al usuari que ja pot usar
            # el chat amb normalitat.
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text='''Ja he acabat. Estic llest per guiar-te! 😄''')
        else:
            # Si el lloc demanat ja ha estat demanat abans pel mateix o algun
            # altre usuari, només cal fer un load del mapa necessari.
            context.user_data['mygraph'] = guide.load_graph(fitxer)
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text='''Fet! Ara pots moure't per *%s*! 😄''' % (place),
                parse_mode=telegram.ParseMode.MARKDOWN)

        # En qualsevol cas cal indicar que el lloc on es troba l'usuari ha
        # canviat.
        context.user_data['place'] = place

    except:
        # Elimino la última posició del vector ja que és la que he afegit al
        # "try:" abans de produir-se l'error.
        del Places[-1]

        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='''
No trobo aquest municipi. 🤔
Siusplau, assegura't d'haver-lo escrit correctament. 😅''')


def go(update, context):
    """
    Funció: Obté l'ubicació en directe de l'usuari i canvia la variable
    corresponent a la localització d'aquest.
    Si l'usuari té una ruta a seguir, "where" comprovarà si s'ha arribat
    al següent node. Si és així, s'envia un missatge informatiu per tal
    de guiar fins el següent punt.
    ----------
    Input: Nom del destí.
    ----------
    Output: Fotografia amb la ruta a seguir, missatge informatiu al chat
    de telegram o missatge d'error.
    ----------
    Precondició: La localització s'ha enviat i el destí i la ubicació
    pertanyen al graf desat a context.user_data['mygraph']. No és
    contemplen en cap cas rutes per les que calgui informació de més
    d'un graf.
    """

    if 'location' not in context.user_data:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Siusplau, envia'm abans la teva *ubicació en temps real*. 📍",
            parse_mode=telegram.ParseMode.MARKDOWN)
    else:
        try:
            dest = update.message.text[4:]
            # Busco el destí amb el nom del municipi per tal d'evitar casos
            # en els que buscar-ho sense concretar el municipi dona problemes.
            # Exemple: Plaça Catalunya, Barcelona
            try:
                context.user_data['destination'] = guide.get_location(
                    dest + ', ' + context.user_data['place'])
            # També el busco sense el nom del municipi ja que potser l'usuari
            # està buscant un punt fora d'aquest i m'agradaria indicar-ho.
            except:
                context.user_data['destination'] = guide.get_location(dest)

            try:
                context.user_data['route'] = guide.get_directions(
                    context.user_data['mygraph'], context.user_data['location'],
                    context.user_data['destination'])

                filename = "%d.png" % random.randint(1000000, 9999999)

                # Crea i desa a "filename" la fotografia amb la ruta que
                # ha de seguir l'usuari.
                guide.plot_directions(context.user_data['route'], filename)

                context.bot.send_photo(
                    chat_id=update.effective_chat.id,
                    photo=open(filename, 'rb'))
                os.remove(filename)

                context.bot.send_message(
                    chat_id=update.effective_chat.id,
                    text="Dirigeix-te a %s." % (
                        context.user_data['route'][0]['next_name']))
            except:
                context.bot.send_message(
                    chat_id=update.effective_chat.id,
                    text='''
Sembla que no hi ha ruta per anar a on vols... 🤔
Estic suposant que ets a *%s*, si no és així indica'm-ho escrivint
*/imin* seguit del municipi en el que et trobes.'''
                    % (context.user_data['place']),
                    parse_mode=telegram.ParseMode.MARKDOWN)

        except:
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text='''
No trobo aquest punt. 🤔
Siusplau, assegura't d'haver escrit correctament el teu destí. 😅''')


def cancel(update, context):
    """
    Funció: Cancel·la la ruta que està fent l'usuari.
    """
    try:
        del context.user_data['destination']
        del context.user_data['route']
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Has cancel·lat la ruta. 😐")
    except:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Per cancel·lar la ruta abans has de crear-ne una. 🤨")


def author(update, context):
    """
    Output: Missatge al chat de telegram amb el nom del autor del projecte.
    """
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="L'autor d'aquest projecte és l'Alejandro Campayo")


TOKEN = open('token.txt').read().strip()
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(MessageHandler(Filters.location, where))
dispatcher.add_handler(CommandHandler('imin', imin))
dispatcher.add_handler(CommandHandler('go', go))
dispatcher.add_handler(CommandHandler('cancel', cancel))
dispatcher.add_handler(CommandHandler('author', author))

updater.start_polling()
