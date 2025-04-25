"""
INFORMACIÓ BÀSICA
-----------------
"Guide.py" és un módul que conté codi relacionat amb l'adquisició
i l'enmagatzematge de grafs corresponents a mapes i amb el càlcul de rutes.

FUNCIONS
--------
Aquest mòdul conté 7 funcions públiques i una d'auxiliar i privada:
"download_graph", "get_directions", "get_location", "load_graph",
"plot_directions", "save_graph" , "print_graph" i "_distance_two_points".
Usa help(bot."nom de la funció") per obtenir més informació.
"""


__author__ = 'Alejandro Campayo Fernández'


from haversine import haversine
from staticmap import *
import networkx as nx
import osmnx as ox
import pickle
import math


def download_graph(place):
    """
    Funció: Descarrega el graf del lloc demanat.
    ----------
    Input: Paraula corresponent al nom del lloc del qual volem el graf.
    ----------
    Output: Graf d'Osmnx que es correspon al mapa del lloc desitjat.
    ----------
    Precondició: El lloc escrit forma part de la llibreria d'Osmnx.
    """
    graph = ox.graph_from_place(place, network_type='all', simplify=True)
    ox.geo_utils.add_edge_bearings(graph)
    return graph


def save_graph(graph, filename):
    """
    Funció: Desa un graf a un fitxer.
    ----------
    Input: Graf i paraula corresponent al nom del fitxer on volem desar-lo.
    """
    try:
        f = open(filename, 'wb')
        pickle.dump(graph, f)
        f.close()
    except Exception as e:
        print(e)


def load_graph(filename):
    """
    Funció: Obté el graf contingut a un fixer.
    ----------
    Input: Paraula corresponent al nom del fitxer del qual volem extreure la
    informació.
    ----------
    Output: Graf contingut al fitxer.
    ----------
    Precondició: El fitxer existeix i està al mateix directori que
    "guide.py".
    """
    try:
        f = open(filename, 'rb')
        graph = pickle.load(f)
        f.close()
        return graph
    except Exception as e:
        print(e)


def print_graph(graph):
    """
    Funció: Escriu al terminal tota la informació continguda a un graf.
    ----------
    Input: Graf de osmnx.
    ----------
    Output: Informació de tots els nodes del graf juntament amb les seves
    arestes adjacents amb tots els seus atributs.
    """
    for node1, info1 in graph.nodes.items():
        print(node1, info1)
        for node2, info2 in graph.adj[node1].items():
            print('    ', node2)
            # els grafs de osmnx són multigrafs però només necessitem
            # la primera aresta.
            edge = info2[0]
            # eliminem la informació de geometria perquè no la necessitem.
            if 'geometry' in edge:
                del(edge['geometry'])
                print('        ', edge)


def get_location(place):
    """
    Funció: Obté les coordenades d'un lloc indicat.
    ----------
    Input: String que fa referència a un lloc.
    ----------
    Output: Vector (lat, log) corresponent a les coordenades del lloc
    demanat.
    ----------
    Precondició: El lloc s'ha contemplat a la llibreria d'Osmnx.
    """
    location = ox.geocode(place)
    return location


def get_directions(graph, source_location, destination_location):
    """
    Funció: Crea i retorna una ruta que representa el camí més curt entre
    dos punts.
    ----------
    Input: Un graf Osmnx i dues coordenades que és corresponen a l'origen
    i el final de la ruta que volem fer.
    ----------
    Output: Llista de nodes que determinen la ruta més curta entre els dos
    punts rebuts.
    ----------
    Precondició: Els dos nodes rebuts pertanyen al graf i hi ha arestes
    que permeten anar d'un punt a l'altre.
    """

    # Busca el primer i l'últim node ja que les coordenades d'aquests dos punts
    # no són cap dels que ofereix Osmnx. Busca els nodes de la llibreria
    # més propers.
    source_node = ox.geo_utils.get_nearest_node(
        graph, source_location, method='haversine', return_dist=False)
    destination_node = ox.geo_utils.get_nearest_node(
        graph, destination_location, method='haversine', return_dist=False)

    # Si la distancia entre la coordenada i el node més proper és més gran
    # 500 metres, considero que el node no pertany al graf i retorno error
    if _distance_two_points(source_location,
                            (graph.nodes[source_node]['y'], graph.nodes[source_node]['x'])
                            ) > 500:
        raise ValueError("Coordinate does not belong to the graph")
    elif _distance_two_points(destination_location,
                              (graph.nodes[destination_node]['y'],
                               graph.nodes[destination_node]['x'])) > 500:
        raise ValueError("Coordinate does not belong to the graph")

    L = nx.shortest_path(graph, source_node, destination_node)
    my_graph = nx.Graph()

    # Llista on desa tota la informació que volem a la sortida.
    directions = []

    # Afegir primer node.
    my_graph.add_node(0, angle=None, current_name=None,
                      dst=(graph.nodes[L[1]]['y'], graph.nodes[L[1]]['x']),
                      length=None, mid=(graph.nodes[L[0]]['y'],
                                        graph.nodes[L[0]]['x']), next_name=None,
                      src=source_location)
    edge = graph.get_edge_data(L[0], L[1])[0]
    if 'name' in edge.keys():
        my_graph.nodes[0]['next_name'] = edge['name']
        directions.append(my_graph.nodes.data()[0])

    # Afegim nodes sense possible problema.
    for i in range(0, len(L) - 2):
        node_src = L[i]
        node_mid = L[i + 1]
        node_dst = L[i + 2]
        src_ = (graph.nodes[node_src]['y'], graph.nodes[node_src]['x'])
        mid_ = (graph.nodes[node_mid]['y'], graph.nodes[node_mid]['x'])
        dst_ = (graph.nodes[node_dst]['y'], graph.nodes[node_dst]['x'])
        edge_src_mid = graph.get_edge_data(node_src, node_mid)[0]
        edge_mid_dst = graph.get_edge_data(node_mid, node_dst)[0]
        angle_ = (edge_mid_dst['bearing'] - edge_src_mid['bearing'])
        if angle_ < 0:
            angle_ += 360
        my_graph.add_node(i + 1, angle=angle_, current_name=None,
                          dst=dst_, length=edge_src_mid['length'], mid=mid_,
                          next_name=None, src=src_)
        # Hi ha carrers sense nom, si en tenen l'afegim, sinó afegim None.
        if 'name' in edge_src_mid.keys():
            my_graph.nodes[i + 1]['current_name'] = edge_src_mid['name']
        if 'name' in edge_mid_dst.keys():
            my_graph.nodes[i + 1]['next_name'] = edge_mid_dst['name']
        directions.append(my_graph.nodes.data()[i + 1])

    # Afegir penúltim node. L'afegeixo així ja que prefereixo que hi hagi
    # repetició de codi abans que un condicional que s'executa tota l'estona
    # preguntant si puc aconseguir l'angle o no.
    edge = graph.get_edge_data(L[len(L) - 2], L[len(L) - 1])[0]
    my_graph.add_node(len(L) - 1, angle=None, current_name=None,
                      dst=destination_location,
                      length=edge['length'],
                      mid=my_graph.nodes[len(L) - 2]['dst'],
                      next_name=None, src=my_graph.nodes[len(L) - 2]['mid'])
    if 'name' in edge.keys():
        my_graph.nodes[len(L) - 1]['current_name'] = edge['name']
    directions.append(my_graph.nodes.data()[len(L) - 1])

    # Afegir últim node.
    my_graph.add_node(len(L), angle=None, current_name=None,
                      dst=None, length=None, mid=destination_location,
                      next_name=None, src=my_graph.nodes[len(L) - 1]['mid'])
    directions.append(my_graph.nodes.data()[len(L)])

    return directions


def plot_directions(directions, filename, width=400, height=400):
    """
    Funció: Crea i desa una imatge que representa una ruta per anar
    d'un punt a un altre.
    ----------
    Input: Ruta determinada per una llista de nodes i nom del fitxer en
    que desarem la sortida.
    ----------
    Output: Imatge en la que haurem representat la ruta a seguir amb una
    línia blava on es marca amb un punt blau l'inici i amb
    un vermell el destí.
    ----------
    Precondició: El arxiu amb el nom donat existeix i es troba al mateix
    directori que guide.py.
    """
    map = StaticMap(width, height)

    # Insereix cercle que indica l'inici de la ruta.
    start = (directions[0]['src'][1], directions[0]['src'][0])
    marker = CircleMarker(start, 'blue', 8)
    map.add_marker(marker)

    for line in range(0, len(directions)):
        start = (directions[line]['src'][1], directions[line]['src'][0])
        end = (directions[line]['mid'][1], directions[line]['mid'][0])
        map.add_line(Line((start, end), 'blue', 2))
        marker = CircleMarker(start, 'blue', 4)
        map.add_marker(marker)

    # Insereix cercle vermell que indica el final de la ruta.
    destination = (directions[-1]['mid'][1], directions[-1]['mid'][0])
    map.add_marker(CircleMarker(destination, 'red', 8))

    image = map.render()
    image.save(filename)
    return


def _distance_two_points(a, b):
    """
    Funció: Obté i retorna la distància entre dos punts.
    ----------
    Input: Dues cordenades (lat, lon).
    ----------
    Output: Distància (en metres) entre les dues coordenades.
    """
    return haversine(a, b, unit='m')
