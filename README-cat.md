# GuideBot

Aquest projecte ha consistit en la creació d'un bot de telegram que, mitjançant dos mòduls de python, ofereix rutes als seus usuaris. Aquestes els parmetran anar des d'on són fins una localització desitjada mentre són guiats pel bot.

Això ho fa reaccionant a un seguit de comandes (`/help`, `/author`, `/go`, `/imin` i `/cancel`). Algunes d’aquestes s’han d’utilitzar d’una manera concreta. Per afrontar aquest possible problema s'informa en tot moment al client de que i com ho ha de fer mitjançant missatges diferents depenent de la situació en la que es troba.

El codi està dividit en dos grans blocs que conformen els dos documents de python (guide.py i bot.py) presents a la carpeta. El primer, conté tot el codi relacionat amb l’adquisició, l'emmagatzematge i la gestió de grafs corresponents a mapes així com el càlcul de rutes. El segon, disposa de tot el codi del bot de Telegram tot usant el mòdul guide.

## Abans de començar

### Descàrrega dels arxius
Desa els dos móduls (guide.py i bot.py) en un mateix directori. Durant l'execució d'aquest programa és possible que es descarreguin altres arxius, és per això que és recomanable crear una carpeta específica per aquests dos documents.  S'indica quins documents han estat creats pel bot al final del seu nom, on es llegirà _GuideBot. Aquests arxius no han de ser modificats sota cap concepte, de fer-ho el funcionament del bot podria veure's afectat.

### Aplicacions necessàries

El qui vulgui executar l'arxiu bot.py, així com tot usuari que vulgui fer-ne ús, haurà de descarregar l'aplicació de Telegram, disponible a qualsevol AppStore.

D'altra banda, si el client vol provar el bot sense haver de moure's es recomana l'ús d'una aplicació anomenada "Mock Locations" només diponible per dispositius Android. Aquesta aplicació simula la teva localització i et dona l'opció de generar rutes que pots recórrer a la velocitat desitjada.

### Creació d'un bot de telegram
Per executar l'arxiu bot.py abans hauràs de crear un bot. Per fer-ho has de buscar el perfil de BotFather a l'aplicació de Telegram i enviar-li `/newbot`. Doncs tansols hauràs de seguir els passos que ell t'indiqui (triar nom i nom d'usuari).

Una vegada fet això el BotFather t'oferirà un link (per exemple t.me/GuideBot) per accedir al teu bot i un access token (per exemple `AAHlODiaTsuH5nxxYknP96F9f5NcGptFKsc`).

El segon l'has de copiar i enganxar en un arxiu anomenat **token.txt** que només ha de contenir aquest codi. Aquest document l'hauràs de desar al mateix directori on tinguis els documents bot.py i guide.py. L' access token no l’has de compartir, altrament, algú altre podria substituir el teu bot.

### Instal·lació de llibreries necessàries

Per tal de poder executar els documents oferts, cal que abans descarreguis les llibreries d'haversine, networkx, osmnx, python-telegram-bot i staticmap. Per fer-ho només has d'executar ```pip3 install -r requirements.txt```  o bé ```pip install -r requirements.txt``` segons la versió de python de que disposis. La última d'aquestes llibreries sobint dona problemes a l'hora d'instal·lar-se, és per això que al mateix document s'indica que fer en aquest cas.

Alternativament, també pots descarregar aquests paquets un a un usant:
```
pip install networkx
pip install staticmap
pip install python-telegram-bot

brew install spatialindex *(per Mac)*
apt install libspatialindex-dev *(per Ubuntu)*
pip install osmnx
```

D'aquesta manera podràs executar l'arxiu bot.py.

## Mòduls del projecte

### Guide

Guide.py conté codi relacionat amb l'adquisició i l'enmagatzematge de grafs corresponents a mapes i amb el càlcul de rutes.

Aquest mòdul conté 7 funcions públiques: `download_graph`, `get_directions`, `get_location`, `load_graph`, `plot_directions`, `save_graph` , `print_graph`.

 - `download_graph`:  Descarrega el graf que representa un lloc indicat.
 - `save_graph`: Desa el graf en el document desitjat.
 - `load_graph`: Obté un graf d'un fitxer.
 - `print_graph`: Escriu al terminal tota la informació continguda al graf.
 - `get_location`: Donat un lloc retorna les coordenades on es troba.
 - `get_directions`: Crea i retorna la ruta més curta per anar des d'un punt fins un altre.
 - `plot_directions`: Crea i desa una imatge que representa una ruta per anar d'un punt a un altre.

### Bot

Bot.py  conté tot el codi relacionat amb el bot de Telegram. La seva tasca és reaccionar a les comandes i als canvis de localització
dels usuaris per poder-los guiar.

Aquest mòdul conté 6 funcions públiques: `start`, `help`, `where`,  `imin`,  `go`,  `cancel` i `author`.

 - `start`: Inicia la conversa amb el bot.
 - `help`: Envia missatges d'ajuda que expliquen com fer un bon ús de l'aplicació.
 - `where`: Reacciona dabant les actualitzacions de la localització i s'encarrega de revisar si s'ha arribat al següent punt de la ruta, enviant un missatge amb la següent ordre en cas afirmatiu.
 - `imin`: Canvia de ciutat en la que es considera que es troba el client.
 - `go`: Comença la ruta per la que es guiarà fins el destí.
 - `cancel`: Cancel·la la ruta.
 - `author`: Envia un missatge amb el nom de l'autor del projecte.

Totes elles (excepte `where`) s'executen enviant un missatge al bot amb "/" seguit del nom de la funció desitjada (a més cal indicar el destí en cas de `go` i el municipi en `imin`).

## Com utilitzar-lo

Executa bot.py en el teu terminal i assegura't que ets l'únic que ho fa. Una vegada fet això, serà el teu ordinador donarà vida al bot, que serà accessible mitjançant el link obtingut en la creació del bot o bé buscant el seu perfil a Telegram.

Una vegada al chat, hauràs de clicar a "Iniciar" i automàticament t'apareixerà un missatge.

<img src="https://lh3.googleusercontent.com/Gxz-b05JimnSob22gk_ijBtjBdX1xEDHSUg532ZtO6lydUhW8znQKyetGhO_ADQxTGwayj4x1zzCV9J7U7NSNT0D3_dZdmseMfqGxs4Btrh4ASu2YuPwCvJAMguFoP1td43bV4QqmXT1DSfjb8J8XvEt485AtX3yuSWd9YLoWIovj0ld-ROxSd83XkEGf-MPJ06wH6ytkFl_pgnSJxzHyWfz2sFpNmzBgmVIIDdXfoUa-NmUlSn-6oSB6Ho7MT4iT0HJqoZR4YG5RgpuUt4GJj8MOQkApAh4jTVRwxkCFlHoobYVhtcdbgDvIHzHnMaucH3fGsHezjQ8Tr_K4qy1-sW-ebViwhUjZbe-ndN9ZWfl19NeHHK7PxHfpVo4n0UM13-zIvIH_i3gVViURCUe_YqSJ2fApOWGOChdbproosOCG8_wM4mRikPgM8gnM8jXf26XclWZj9sdqScNdGIC8uPpB19MxjK1DOBemsGs_29KPO949twe6zPPsGChiCMxjnyeToqiYGvldyiCgqI961G2fovHe3cBDgVyDYDhINEBwo9X-W4yQJ07gj77Q9rwGIvmtI55Sflsqgt630iolrPdQLJZJbL0QkwoBw7_poyGkoxJOhLgbDX60VC2IMbICdnPL00kNexbF3NOCaly8mOQAkx55Vb2d-WTFmNBac35boj1wbMym2_JVWUreg=w1080-h244-no?authuser=0" width="300">

<img src="https://lh3.googleusercontent.com/hfT6MtMJLqbw6YtsDuC1UDrvAzU5ajHFdvSTEx5Tc4XfCqjnGZ6pGC7NL8AD3M0-96hIgRBFztKUiSO43BAoiwZEItrCp-R6Ij1-DkQQfQ2vWS7hV5Q5S_v0NjAlNXuP6MxhZMn-_f9Xi6SUkSBGQcDBMdGmUwyUE0twEa5N6zL3FikF6zHGs0erkwOaTY8O4WMQcJm3jLf9hO8Te1EzsX2vJTyD_JgkjLk8JNPHi3dAk6S766rziok4FRUujuat70t04HZMDpmU9OURm3yReFGDlKobvCpiJErqYC1qNgCEzYn4Cq9w1hOX3Hvcn5wJFvAv17THaSrqVpDGT-zPJfMu-Hxbg944dVMLrA8r1Lxhb7o-WYnFOwJyRk5D73tbmFCihguqcoWts2iL3azmK0xsaY6i-ygQjD2Sd_uiXV08pWlhGdb1-FjpgBGQWbvFnwP7qcFs9mHG5dhijYt4dsNDDm3rd1cqcUDuhrD4yr13xzLjl28LKN97Wdts82qRSz5B0LbLEKCRcla3urCZp2saLjwpohmLhLZrceIOXXrgU4EeGqyonfySBZCEXapPcXgutevtpsGJCRLh9QxYTCRjKUtfELllTp5yWR6yA3a6Yr14cAq10vlddh6Awg1nxwrMuTWY6vuJrarO-RcYWNcPewmHqG8NxQubpc7O4O7AJtmGvumErDmDDRwFVg=w743-h317-no?authuser=0" width="300">

Si escrius `/help` com s'indica, t'apareixeran tres missatges informatius explicant com fer un ús correcte del bot.

<img src="https://lh3.googleusercontent.com/Xiifg5YHZQZ2bBTYszWUV6YaGHjfIpgTbR7Xh6LflTRi5nf_t5rwbQvwBY5vcNYLXmRVbyS5az4fg7P7Mutj6FlYukhnc0hogAwcXZZ_4xfRIV-PlthFhjdY2yubnI5bLxDFJ2I2ke7YcIUsLOPFxj924r4vikRZGhb-0UKm4IbuWdD8177vaVfDCPppHA5YBUUnrt-sbAD4-0CMu2l2g4xlvXnSham75MnIFZQpYinnVFMgzzFnKakoj3MbXQWzVOzOen8O3pwhcNv37oRmFu7zmFjzBH6vvkkZOZKlbFR9IMKC7wpAljyYJ4-flWjV8JdxLO2_1dC_fRGlm3pK6SiVLm2WgjXsZU-1p4UWx45mk-hcVIP0Ug-GcNSjRq6uDEtzIVSrEs-Z8ZgHKQX8ZGeznm0c37QFS_xEqDYiVcKhl5vOVGXhagEEn0kmuWe3d9HYfc0DBXqF4LlVJWwBupTkAaFLe_fr5CriGrZ-iUxSJm7Nj0O1Mq0zQKTQ5Mc1a30h0OyeUUD8Bk_QFhJfaudN5Gbw6r9SUxcrtUhmoyIVTbCR-EgyWODaNhSokm3HfqepTjMtSyuZ0wtGr9RjDw1GYYNt4Urn9pnHGjG9LvxHPX0cL_gGODOn3fiPb8nVs9DkZQCYpXCzPBMsPFNR3PI3noMK0CJiS4MusckY0B_k1CgeU3wCkfE-Naqjgw=w1080-h1492-no?authuser=0" width="300">

Per començar la ruta hauràs d'enviar la teva localització en directe i després indicar on vols anar amb un  `/go (destí)` tenint en compte que si un d'aquests dos punts no pertany a Barcelona rebràs un missatge d'error.

En aquest cas el que hauràs de fer és descarregar el graf que contigui les dades del lloc on et trobes, mitjançant la comanda   `/imin (municipi)`.  Això pot trigar una estona, durant la qual la resta d'usuaris tampoc podran realitzar algunes accions amb normalitat.

Després d'això, podràs ser guiat pel teu municipi sempre tenint en compte que no es contemplen rutes entre diferents pobles o ciutats.
A mesura que la ruta es vagi completant s'enviaran missatges que et guiaran fins el pròxim punt on hi hagi un encreuament. D'altra banda, també es pot acabar la ruta abans d'arribar al destí si s'indica fent  `/cancel`.

<img src="https://lh3.googleusercontent.com/YcjqszWlU2E5LtuDAiu4V_6T6wWVtvzN70JDVdILm7eIdMtC0iA0O-cWUKSdPgTJ3k0hxM-YDF_VXS70zPHSvKw2d2eRy0hORKNSamC-h64cRHKcQlf-ZUaeqWEVSOWjZOIA7yH4chel1TIUXftA7a-4QPeHsXJr70n6uktgdvRgDyMfmIpa0fqMAnhcREBCHKF4q0TuFOcJzwhR1zt00CE_QbvDmIFCdS_BA0yjN_tho0PKio9_456kleERUFm7FZaRkOkSpMaYA69YAFTCgmmznrcR0c3iKTjnjE1UhRtcebTEaTuDIYrv5RL4y6fMiJetU4ypbYWk3JQ8iMeftzxd7-KXtyHSY6AMV7b4yaKYf9Rpp4kxGOedj8EIupU-uxZpGQvSLM0b_8HDD-RjO5IkV7NX3YX4HICj3YJ0CTzSmZuOEZNNMM4YWIm7MJ49CGmbAgjv3wM1Uq1Tnt2cUzwHlJ00HBPNdlZvhe46Dxvpqzn7nxZdVNuOLBbYeWaQhDQKsEwqIvnTx99_c5eWDjmd2Dy0VwfPtX8zrreHuKZZheXMxS00IXfqEK_YAmIegxbyNCmTCWog11bOHK71zQ6GMpYfgNT1zYNo0TrmYna3neqsKunrp3hgT_w7VnwUrqaL-DGq6c0F3lxISwWB5Kcn3RNon4lEesMONkCquMQz5zR9e9Ps3Ez8Qx_n_g=w1080-h255-no?authuser=0" width="300">

El camí ofert està definit per un seguit de punts, perquè les ordres apareguin s'ha d'arribar a cadascun d'aquests seguint l'ordre indicat, altrament el bot deixarà de donar ordres fins que no s'arribi al node pendent.

### Exemple

Intentem anar des de *Carrer del Baró de les Quatre Torres* fins a *Plaça Imperial Tarraco*. En aquest cas, com que no ens trobem a Barcelona si intentem crear la ruta sense indicar-ho rebrem un missatge d'error:

<img src="https://lh3.googleusercontent.com/cjjF3j0VlYfxL6juGa2F2RhG_khnfhwsbHD2egOhcViHmGSJf0_8a10P5GQroAt2Oi4d_wFXkdGEqgW5rplzipCIE8PdptKe0KJzVRHA8GtTS4BymoiBwbfJfVWQcXBhVxiyT9Wi29QfewWdItkb2177v7Qnl01xxDJ68mK8XKjW-JUanoTTfZ9lqHyEDMGKg4k16LAfdIY2L1YSikAXB03tUd01D55E7mo82qvLqAI_aj20UpwYLTEMNkfxlM6ezm_U8kYcap54Pabiz0DEktLJd6muA_mal0FMoJkSgLcubYS-wqHeXVZFWwu9XrutRLqocDcYBz_iSXMjd-N7wf0YZ3waxbeSflMPj2paZaJUxAU_-Y3ps20Msej3fSpgqwX9iuf5LUMnGGe24KE3Z-mqkVhaZLp1bKOq_agLGd6YGygltlPbaTODlrTqmLqUV8XUidfg_deVE_rEmZMky8S2KO1-Awv8ecS9HyHWDoEalDVti1cjBk6UhtJlY6HAj6VEI5iFRDWFf3iRRhjogySySd_tpHc0PXA_TjgH5tiIxC2rwLVpsos0sKJ35TQHu1Mb_auNGJlF0oTD-mh6nu4-550Bfqn_0oXRdP4BB4yNp3RvYNRfhfN3UtcGBbl3SOSCIT9r8yb-MPx1y1GUgpBIbTJT-ivkrE4rFe6KA3mjv1ex2ZiQ7hPJEziUjQ=w1080-h534-no?authuser=0" width="300">

Haurem doncs de demanar al bot que ens descarregui el mapa de Tarragona.

<img src="https://lh3.googleusercontent.com/7nok2O5QR1Ub1XBYVyKaUtowSLYcEf4VB15IdorTNrwBTeqtlkldETBvPAg-t5hqD5oO9CLMJx05ThonCnH1NKtj7VPbBlb6UgknbL36qUdVsxAguOm4L5siz0-S_wCKXg1dCz81iS8AiEsGaUUKucnOqpT9MWcMTCzpMtizo7D9tehCZBAFY61NnNDTDBjAhvw_hcclEX6XiUIWOk1762_sPI84oyjYRZIL2ZIQShLzsMJek_uQPgk1LQJM3EswZa5RuNDIK_Fgt-PAXyitPkcspm75QpgJcEi2sSv9abGJeMswXxAx-LClIt1loXYxUv4a0WkYSL6h9u3MHx3_tPxpIEnPnc9VbGR_G-pGLJ37LdDDqejkvzghr_r01fORvfBH_VA6OqS8_VdpniTmxmUGU3UefoY48GtyH26KB_MrHfi6glKxHSllkFMZz2XZc2ZUgylFboTMyokL10T_tb3JJG-yROkHqtH-Rk0RsQdpcY9LDVXTGlXUqDdkas9-tnMHKc8xVVCFm4ktUjAdLdTuN5W8EUKwY5Nzv5-5-GCScJh4SZ7Bu0DaSKBz67WVej6XLDhk-qFapTT7XrYBR-obZmtIuUuMb7JkxH5EVeiEnYUiM_Uj9-mDXBMp__xAUnVs0ZnxSderUm2eS0pnO-MoV63Euaa0FR6SdRA7yjVWgqy8QBT2ujvjvYLF2g=w1080-h530-no?authuser=0" width="300">

Una vegada fet això, podrem demanar anar fins el destí desitjat sense cap problema.

<img src="https://lh3.googleusercontent.com/edWfpUQdB4A7CiV2nT-ZkE_iQ98ngXzBhT1iAe19vI13anYRgTi6Wf1fbC-1AOjHNuAd_uQ3n79I7H93BM73QWF1ajEuMsCncgQh4sztbuguLsQNotxm1xqHqFYkOb_xbK-afUj6FS0XWiJWm7sY20cwg4_-mAF2e6wyb0iFgM1L0XCi-7yBEatYLnfJnYf2Apr3KZ75aRklx6JCeMc_seFPElkrDbRT6q28FImrYIYeGpT1JIH2GRWPhioxSRol6_cLjkEfvfI1CL-llY0RfS4ZzhGj_OddRQzKdXmSIcClvGuUIP_MZSWoudcBBN-CmqjYXrpHSiB_B84R8OHtyGuHirYH7hP2Li8ECkYDto7tr0ptqXS0mDFqN0zRkGPEhnT9kW0CPsMXT2e4tNnYDiZKNqHVt8QmXzZ4jLG7z1fVF1PBWjHAxProJPuykwk8zQOuRqPH_DPbR4hsyCjoOS1dJ7HUiBrut36k92k1yioo184lvtBdIVrIQVdsLZdYGZ3RgKbmnuRMTSNijaBLDBPpBpQgvG53vOUwsL-L0vseOOfMUFxBJib_o_WpS3GSYTTJQgErp46y1g96xy2IPbBA4bjWtz7PCNmZx-sEyIZrV07Rzc6idt-TdDnU-cfM1yaCJbDff85LQ-9H3W2qssTG8H2CBrimit4gAS5ymGXx07OYq5OltqcTNrpC3g=w1080-h1213-no?authuser=0" width="300">

Per últim només haurem de completar la ruta indicada seguint les indicacions que anirem rebent.

<img src="https://lh3.googleusercontent.com/9V74x0wR9fnk98b6QBz8v4qr2ejo976vvUhL5boHo92KrsRCH4akou0xqbKtbkhIVIgBCxYEx2oppQ9_7HVwxSGVyV7LwSCpgc3UucVTlSHKEPyeDOFr_777izpphyz-IP_6_4hGvIG3Fx_3tFFM_XeAv5Mhx3wY78aThp1QFH4HGxBsFs7hfTJbO4jUfz8Wq4FSDMyJ8E0OYtWQE38ANGzdjOeIfiGZ9gGLsA6IUQ2fqDRE_3ApToG2QRvPx65GyAe1ghS6As9fsUT2r70nPgL9vSfhAnlSm2Sq1YP77EAS2JGKj-IBbUGjEkdDi0Ekse-ODiQjrjOX-znVO_Wr_SwD3G4wIgRg05lFpg2oCY7dit_Q-WRVVYJGQv46V9MVYJK83Suv9MjEyTsT80phl1JA4Ph0QmfRR81mdzxnyxLYtlFDGpYYIKHv_rtYR33brUSLp3LOT4NwB5hZLQ8juUQ-XFUHNDHnLh49Chy9-11BcSpCG0ofyTPOHsSM2bqEiQqXSV-OxSLPuHqvMCugG39Zagn-YnggAbQCTilzJLVck1xw2qdaHWxP9rtpVPDJei9o5NJr_n0xxQTRBI0ZxvpZxhMpe-I3qmVEHAxCEOIHcIGSeCdMxFM-ImeebI2sdB8yhmNSVmXlmlvFdYS4QsixUczuNt0G--gu3iZirnwrL9WUreOeIIC_khu5bw=w1080-h357-no?authuser=0" width="300">

<img src="https://lh3.googleusercontent.com/mAPoLtZQ3RnnjcnA7_0RhYzG7__lfT5Y3m8gBr8UQIb5x2Cp-J5gDqN_AL7fAFhQ74VzyAAfKFQbRuf8CemHA7YN-aU19Z169_WN4D_4lWnLM8NYQXqQMyCTL0izB6FZS2YfF3oRDTzp_v9lSA-5NpGIPY_Z5pi5FSit7DEkmifIYcffxUEGfGlbUZhM2lnBgrMDpI2dfGrqoG-EinsYAGik5LuagFfyL2rQUYLzZBQRAFBK13mxtV44cG1LAL-AHYjQhKyL3EjOO9lq4bP6vqdvEcTVVVGUbqC804XWD6_C5GBYVg0TbZDE2lKC3yYgIfKwUHiYkwhkxt3AWW7ifGaaucemLW8ypyzwgjktAg8WQ3r7jE_WjLB0v78yPIDgZ57fuq-wGyVUSkUP-5LQJdvsIxdDU-OXehQWX8AH9uc8XIYMKqvHhkDhgVvyQuFROexvYxxkndqclUD05PVpzMqyftWf0DfDLPQIOCwWXzeiOY1uJQRf1-nt3vGY0b76V8cjey11Pr1wuN7jNC5jbxJEnB6j7bTBHbaQVRbgNgf66cLTOk9z1mQMyalYTD9qZQ1qygp1tVnsz3koQD4iGsaekfKg_W402qLll8O0Hsuv-5Pwujc0UdFXER4MzhW3aU0A39HAFO9DDfYlc-qdiLn7DRmUO3nSi5lt6ufKE9-PQySu6u0SIZHSXbALqA=w1080-h417-no?authuser=0" width="300">

## Informació disponible al terminal

Mentre s'executi bot.py aniran apareixent missatges al terminal. Alguns d'aquests poden ser missatges d'error, altres en canvi pretenen informar al administrador de que s'està descarregant un graf i per tant altres usuaris poden veure's afectats o indiquen quins grafs estàn disponibles pels usuaris i per tant un `imin` d'aquell lloc no suposaria cap "bloqueig" temporal.


## Documentació de les llibreries usades

* [Networkx](https://networkx.github.io) - Usada pel tractament dels grafs.
* [Osmnx](https://osmnx.readthedocs.io/en/stable/) - Necessària per l'obtenció de l'informació dels punts d'interès.
* [StaticMap](https://rometools.github.io/rome/) - Usada per l'obtenció de mapes.
* [Python-Telegram-Bot](https://python-telegram-bot.readthedocs.io/en/stable/) - Encarregada de tot alló que té relació amb el bot de telegram.

## Autor

Alejandro Campayo Fernández

## Referències

Aquest projecte s'ha dut a terme seguint els passos oferts per [README.md](https://github.com/jordi-petit/ap2-guidebot/blob/master/README.md). Document els autors del qual són Jordi Petit i en Jordi Cortadella, professors de l'Universitat Politècnica de Catalunya.
