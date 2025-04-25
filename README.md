# GuideBot

This project involved creating a Telegram bot that, using two Python modules, provides routes to its users. These routes allow users to travel from their current location to a desired destination while being guided by the bot.

The bot responds to a set of commands (`/help`, `/author`, `/go`, `/imin`, and `/cancel`). Some of these commands must be used in a specific way. To address potential issues, the bot informs the user at all times about what to do and how to do it through different messages depending on the situation.

The code is divided into two main blocks, which correspond to the two Python files (guide.py and bot.py) located in the folder. The first file contains all the code related to acquiring, storing, and managing graphs for maps, as well as route calculations. The second file contains all the code for the Telegram bot, which uses the guide module.

## Before You Start

### Downloading the Files

Save the two modules (guide.py and bot.py) in the same directory. During the execution of this program, additional files may be downloaded, so it is recommended to create a specific folder for these two files. Files created by the bot are identified by the suffix `_GuideBot` in their names. These files should not be modified under any circumstances, as doing so could affect the bot's functionality.

### Required Applications

Anyone who wants to run the bot.py file, as well as any user who wants to use it, must download the Telegram application, available on any App Store.

Additionally, if the user wants to test the bot without moving, it is recommended to use an application called "Mock Locations," which is only available for Android devices. This application simulates your location and allows you to generate routes that you can follow at your desired speed.

### Creating a Telegram Bot

To run the bot.py file, you first need to create a bot. To do this, search for the BotFather profile in the Telegram app and send it the `/newbot` command. Then, simply follow the steps it provides (choose a name and username).

Once this is done, BotFather will provide you with a link (e.g., t.me/GuideBot) to access your bot and an access token (e.g., `AAHlODiaTsuH5nxxYknP96F9f5NcGptFKsc`).

Copy and paste the access token into a file named **token.txt**, which should contain only this code. Save this file in the same directory as bot.py and guide.py. Do not share the access token, as someone else could take control of your bot.

### Installing Required Libraries

To run the provided files, you must first install the libraries `haversine`, `networkx`, `osmnx`, `python-telegram-bot`, and `staticmap`. To do this, simply execute:

```bash
pip3 install -r requirements.txt
```

or

```bash
pip install -r requirements.txt
```

depending on your Python version. The last library often causes installation issues, so the requirements file includes instructions for resolving this.

Alternatively, you can install these packages one by one using:

```bash
pip install networkx
pip install staticmap
pip install python-telegram-bot

brew install spatialindex *(for Mac)*
apt install libspatialindex-dev *(for Ubuntu)*
pip install osmnx
```

This will allow you to run the bot.py file.

## Project Modules

### Guide

The guide.py file contains code related to acquiring and storing graphs for maps, as well as route calculations.

This module includes 7 public functions: `download_graph`, `get_directions`, `get_location`, `load_graph`, `plot_directions`, `save_graph`, and `print_graph`.

- `download_graph`: Downloads the graph representing a specified location.
- `save_graph`: Saves the graph to the desired file.
- `load_graph`: Loads a graph from a file.
- `print_graph`: Prints all the information contained in the graph to the terminal.
- `get_location`: Returns the coordinates of a specified location.
- `get_directions`: Creates and returns the shortest route between two points.
- `plot_directions`: Creates and saves an image representing a route between two points.

### Bot

The bot.py file contains all the code related to the Telegram bot. Its task is to respond to user commands and location updates to guide them.

This module includes 6 public functions: `start`, `help`, `where`, `imin`, `go`, `cancel`, and `author`.

- `start`: Starts the conversation with the bot.
- `help`: Sends help messages explaining how to use the application correctly.
- `where`: Responds to location updates and checks if the user has reached the next point on the route, sending the next instruction if so.
- `imin`: Changes the city where the user is considered to be located.
- `go`: Starts the route to guide the user to the destination.
- `cancel`: Cancels the route.
- `author`: Sends a message with the author's name.

All of these (except `where`) are executed by sending a message to the bot with "/" followed by the desired function name (you must also specify the destination for `go` and the municipality for `imin`).

## How to Use It

Run `bot.py` in your terminal and ensure that you are the only one doing so. Once this is done, your computer will bring the bot to life, making it accessible via the link obtained during the bot creation process or by searching for its profile on Telegram.

Once in the chat, you will need to click "Start," and a message will automatically appear.

<img src="https://lh3.googleusercontent.com/Gxz-b05JimnSob22gk_ijBtjBdX1xEDHSUg532ZtO6lydUhW8znQKyetGhO_ADQxTGwayj4x1zzCV9J7U7NSNT0D3_dZdmseMfqGxs4Btrh4ASu2YuPwCvJAMguFoP1td43bV4QqmXT1DSfjb8J8XvEt485AtX3yuSWd9YLoWIovj0ld-ROxSd83XkEGf-MPJ06wH6ytkFl_pgnSJxzHyWfz2sFpNmzBgmVIIDdXfoUa-NmUlSn-6oSB6Ho7MT4iT0HJqoZR4YG5RgpuUt4GJj8MOQkApAh4jTVRwxkCFlHoobYVhtcdbgDvIHzHnMaucH3fGsHezjQ8Tr_K4qy1-sW-ebViwhUjZbe-ndN9ZWfl19NeHHK7PxHfpVo4n0UM13-zIvIH_i3gVViURCUe_YqSJ2fApOWGOChdbproosOCG8_wM4mRikPgM8gnM8jXf26XclWZj9sdqScNdGIC8uPpB19MxjK1DOBemsGs_29KPO949twe6zPPsGChiCMxjnyeToqiYGvldyiCgqI961G2fovHe3cBDgVyDYDhINEBwo9X-W4yQJ07gj77Q9rwGIvmtI55Sflsqgt630iolrPdQLJZJbL0QkwoBw7_poyGkoxJOhLgbDX60VC2IMbICdnPL00kNexbF3NOCaly8mOQAkx55Vb2d-WTFmNBac35boj1wbMym2_JVWUreg=w1080-h244-no?authuser=0" width="300">

<img src="https://lh3.googleusercontent.com/hfT6MtMJLqbw6YtsDuC1UDrvAzU5ajHFdvSTEx5Tc4XfCqjnGZ6pGC7NL8AD3M0-96hIgRBFztKUiSO43BAoiwZEItrCp-R6Ij1-DkQQfQ2vWS7hV5Q5S_v0NjAlNXuP6MxhZMn-_f9Xi6SUkSBGQcDBMdGmUwyUE0twEa5N6zL3FikF6zHGs0erkwOaTY8O4WMQcJm3jLf9hO8Te1EzsX2vJTyD_JgkjLk8JNPHi3dAk6S766rziok4FRUujuat70t04HZMDpmU9OURm3yReFGDlKobvCpiJErqYC1qNgCEzYn4Cq9w1hOX3Hvcn5wJFvAv17THaSrqVpDGT-zPJfMu-Hxbg944dVMLrA8r1Lxhb7o-WYnFOwJyRk5D73tbmFCihguqcoWts2iL3azmK0xsaY6i-ygQjD2Sd_uiXV08pWlhGdb1-FjpgBGQWbvFnwP7qcFs9mHG5dhijYt4dsNDDm3rd1cqcUDuhrD4yr13xzLjl28LKN97Wdts82qRSz5B0LbLEKCRcla3urCZp2saLjwpohmLhLZrceIOXXrgU4EeGqyonfySBZCEXapPcXgutevtpsGJCRLh9QxYTCRjKUtfELllTp5yWR6yA3a6Yr14cAq10vlddh6Awg1nxwrMuTWY6vuJrarO-RcYWNcPewmHqG8NxQubpc7O4O7AJtmGvumErDmDDRwFVg=w743-h317-no?authuser=0" width="300">

If you type `/help` as indicated, you will receive three informational messages explaining how to use the bot correctly.

<img src="https://lh3.googleusercontent.com/Xiifg5YHZQZ2bBTYszWUV6YaGHjfIpgTbR7Xh6LflTRi5nf_t5rwbQvwBY5vcNYLXmRVbyS5az4fg7P7Mutj6FlYukhnc0hogAwcXZZ_4xfRIV-PlthFhjdY2yubnI5bLxDFJ2I2ke7YcIUsLOPFxj924r4vikRZGhb-0UKm4IbuWdD8177vaVfDCPppHA5YBUUnrt-sbAD4-0CMu2l2g4xlvXnSham75MnIFZQpYinnVFMgzzFnKakoj3MbXQWzVOzOen8O3pwhcNv37oRmFu7zmFjzBH6vvkkZOZKlbFR9IMKC7wpAljyYJ4-flWjV8JdxLO2_1dC_fRGlm3pK6SiVLm2WgjXsZU-1p4UWx45mk-hcVIP0Ug-GcNSjRq6uDEtzIVSrEs-Z8ZgHKQX8ZGeznm0c37QFS_xEqDYiVcKhl5vOVGXhagEEn0kmuWe3d9HYfc0DBXqF4LlVJWwBupTkAaFLe_fr5CriGrZ-iUxSJm7Nj0O1Mq0zQKTQ5Mc1a30h0OyeUUD8Bk_QFhJfaudN5Gbw6r9SUxcrtUhmoyIVTbCR-EgyWODaNhSokm3HfqepTjMtSyuZ0wtGr9RjDw1GYYNt4Urn9pnHGjG9LvxHPX0cL_gGODOn3fiPb8nVs9DkZQCYpXCzPBMsPFNR3PI3noMK0CJiS4MusckY0B_k1CgeU3wCkfE-Naqjgw=w1080-h1492-no?authuser=0" width="300">

To start the route, you will need to send your live location and then indicate where you want to go using `/go (destination)`. Keep in mind that if either of these points is not in Barcelona, you will receive an error message.

In this case, you will need to download the graph containing the data for your current location using the command `/imin (municipality)`. This process may take some time, during which other users may also experience limited functionality for certain actions.

After this, you will be able to be guided within your municipality, always keeping in mind that routes between different towns or cities are not supported. As the route progresses, messages will be sent to guide you to the next intersection. Alternatively, the route can be ended before reaching the destination by using the `/cancel` command.

<img src="https://lh3.googleusercontent.com/YcjqszWlU2E5LtuDAiu4V_6T6wWVtvzN70JDVdILm7eIdMtC0iA0O-cWUKSdPgTJ3k0hxM-YDF_VXS70zPHSvKw2d2eRy0hORKNSamC-h64cRHKcQlf-ZUaeqWEVSOWjZOIA7yH4chel1TIUXftA7a-4QPeHsXJr70n6uktgdvRgDyMfmIpa0fqMAnhcREBCHKF4q0TuFOcJzwhR1zt00CE_QbvDmIFCdS_BA0yjN_tho0PKio9_456kleERUFm7FZaRkOkSpMaYA69YAFTCgmmznrcR0c3iKTjnjE1UhRtcebTEaTuDIYrv5RL4y6fMiJetU4ypbYWk3JQ8iMeftzxd7-KXtyHSY6AMV7b4yaKYf9Rpp4kxGOedj8EIupU-uxZpGQvSLM0b_8HDD-RjO5IkV7NX3YX4HICj3YJ0CTzSmZuOEZNNMM4YWIm7MJ49CGmbAgjv3wM1Uq1Tnt2cUzwHlJ00HBPNdlZvhe46Dxvpqzn7nxZdVNuOLBbYeWaQhDQKsEwqIvnTx99_c5eWDjmd2Dy0VwfPtX8zrreHuKZZheXMxS00IXfqEK_YAmIegxbyNCmTCWog11bOHK71zQ6GMpYfgNT1zYNo0TrmYna3neqsKunrp3hgT_w7VnwUrqaL-DGq6c0F3lxISwWB5Kcn3RNon4lEesMONkCquMQz5zR9e9Ps3Ez8Qx_n_g=w1080-h255-no?authuser=0" width="300">

The offered path is defined by a series of points. To receive instructions, you must reach each of these points in the specified order; otherwise, the bot will stop providing instructions until the pending node is reached.

### Example

Let’s try to go from *Carrer del Baró de les Quatre Torres* to *Plaça Imperial Tarraco*. In this case, since we are not in Barcelona, if we attempt to create the route without specifying it, we will receive an error message:

<img src="https://lh3.googleusercontent.com/cjjF3j0VlYfxL6juGa2F2RhG_khnfhwsbHD2egOhcViHmGSJf0_8a10P5GQroAt2Oi4d_wFXkdGEqgW5rplzipCIE8PdptKe0KJzVRHA8GtTS4BymoiBwbfJfVWQcXBhVxiyT9Wi29QfewWdItkb2177v7Qnl01xxDJ68mK8XKjW-JUanoTTfZ9lqHyEDMGKg4k16LAfdIY2L1YSikAXB03tUd01D55E7mo82qvLqAI_aj20UpwYLTEMNkfxlM6ezm_U8kYcap54Pabiz0DEktLJd6muA_mal0FMoJkSgLcubYS-wqHeXVZFWwu9XrutRLqocDcYBz_iSXMjd-N7wf0YZ3waxbeSflMPj2paZaJUxAU_-Y3ps20Msej3fSpgqwX9iuf5LUMnGGe24KE3Z-mqkVhaZLp1bKOq_agLGd6YGygltlPbaTODlrTqmLqUV8XUidfg_deVE_rEmZMky8S2KO1-Awv8ecS9HyHWDoEalDVti1cjBk6UhtJlY6HAj6VEI5iFRDWFf3iRRhjogySySd_tpHc0PXA_TjgH5tiIxC2rwLVpsos0sKJ35TQHu1Mb_auNGJlF0oTD-mh6nu4-550Bfqn_0oXRdP4BB4yNp3RvYNRfhfN3UtcGBbl3SOSCIT9r8yb-MPx1y1GUgpBIbTJT-ivkrE4rFe6KA3mjv1ex2ZiQ7hPJEziUjQ=w1080-h534-no?authuser=0" width="300">

We will then need to ask the bot to download the map of Tarragona.

<img src="https://lh3.googleusercontent.com/7nok2O5QR1Ub1XBYVyKaUtowSLYcEf4VB15IdorTNrwBTeqtlkldETBvPAg-t5hqD5oO9CLMJx05ThonCnH1NKtj7VPbBlb6UgknbL36qUdVsxAguOm4L5siz0-S_wCKXg1dCz81iS8AiEsGaUUKucnOqpT9MWcMTCzpMtizo7D9tehCZBAFY61NnNDTDBjAhvw_hcclEX6XiUIWOk1762_sPI84oyjYRZIL2ZIQShLzsMJek_uQPgk1LQJM3EswZa5RuNDIK_Fgt-PAXyitPkcspm75QpgJcEi2sSv9abGJeMswXxAx-LClIt1loXYxUv4a0WkYSL6h9u3MHx3_tPxpIEnPnc9VbGR_G-pGLJ37LdDDqejkvzghr_r01fORvfBH_VA6OqS8_VdpniTmxmUGU3UefoY48GtyH26KB_MrHfi6glKxHSllkFMZz2XZc2ZUgylFboTMyokL10T_tb3JJG-yROkHqtH-Rk0RsQdpcY9LDVXTGlXUqDdkas9-tnMHKc8xVVCFm4ktUjAdLdTuN5W8EUKwY5Nzv5-5-GCScJh4SZ7Bu0DaSKBz67WVej6XLDhk-qFapTT7XrYBR-obZmtIuUuMb7JkxH5EVeiEnYUiM_Uj9-mDXBMp__xAUnVs0ZnxSderUm2eS0pnO-MoV63Euaa0FR6SdRA7yjVWgqy8QBT2ujvjvYLF2g=w1080-h530-no?authuser=0" width="300">

Once this is done, we will be able to request to go to the desired destination without any issues.

<img src="https://lh3.googleusercontent.com/edWfpUQdB4A7CiV2nT-ZkE_iQ98ngXzBhT1iAe19vI13anYRgTi6Wf1fbC-1AOjHNuAd_uQ3n79I7H93BM73QWF1ajEuMsCncgQh4sztbuguLsQNotxm1xqHqFYkOb_xbK-afUj6FS0XWiJWm7sY20cwg4_-mAF2e6wyb0iFgM1L0XCi-7yBEatYLnfJnYf2Apr3KZ75aRklx6JCeMc_seFPElkrDbRT6q28FImrYIYeGpT1JIH2GRWPhioxSRol6_cLjkEfvfI1CL-llY0RfS4ZzhGj_OddRQzKdXmSIcClvGuUIP_MZSWoudcBBN-CmqjYXrpHSiB_B84R8OHtyGuHirYH7hP2Li8ECkYDto7tr0ptqXS0mDFqN0zRkGPEhnT9kW0CPsMXT2e4tNnYDiZKNqHVt8QmXzZ4jLG7z1fVF1PBWjHAxProJPuykwk8zQOuRqPH_DPbR4hsyCjoOS1dJ7HUiBrut36k92k1yioo184lvtBdIVrIQVdsLZdYGZ3RgKbmnuRMTSNijaBLDBPpBpQgvG53vOUwsL-L0vseOOfMUFxBJib_o_WpS3GSYTTJQgErp46y1g96xy2IPbBA4bjWtz7PCNmZx-sEyIZrV07Rzc6idt-TdDnU-cfM1yaCJbDff85LQ-9H3W2qssTG8H2CBrimit4gAS5ymGXx07OYq5OltqcTNrpC3g=w1080-h1213-no?authuser=0" width="300">

Finally, we just need to complete the indicated route by following the instructions we will receive.

<img src="https://lh3.googleusercontent.com/9V74x0wR9fnk98b6QBz8v4qr2ejo976vvUhL5boHo92KrsRCH4akou0xqbKtbkhIVIgBCxYEx2oppQ9_7HVwxSGVyV7LwSCpgc3UucVTlSHKEPyeDOFr_777izpphyz-IP_6_4hGvIG3Fx_3tFFM_XeAv5Mhx3wY78aThp1QFH4HGxBsFs7hfTJbO4jUfz8Wq4FSDMyJ8E0OYtWQE38ANGzdjOeIfiGZ9gGLsA6IUQ2fqDRE_3ApToG2QRvPx65GyAe1ghS6As9fsUT2r70nPgL9vSfhAnlSm2Sq1YP77EAS2JGKj-IBbUGjEkdDi0Ekse-ODiQjrjOX-znVO_Wr_SwD3G4wIgRg05lFpg2oCY7dit_Q-WRVVYJGQv46V9MVYJK83Suv9MjEyTsT80phl1JA4Ph0QmfRR81mdzxnyxLYtlFDGpYYIKHv_rtYR33brUSLp3LOT4NwB5hZLQ8juUQ-XFUHNDHnLh49Chy9-11BcSpCG0ofyTPOHsSM2bqEiQqXSV-OxSLPuHqvMCugG39Zagn-YnggAbQCTilzJLVck1xw2qdaHWxP9rtpVPDJei9o5NJr_n0xxQTRBI0ZxvpZxhMpe-I3qmVEHAxCEOIHcIGSeCdMxFM-ImeebI2sdB8yhmNSVmXlmlvFdYS4QsixUczuNt0G--gu3iZirnwrL9WUreOeIIC_khu5bw=w1080-h357-no?authuser=0" width="300">

<img src="https://lh3.googleusercontent.com/mAPoLtZQ3RnnjcnA7_0RhYzG7__lfT5Y3m8gBr8UQIb5x2Cp-J5gDqN_AL7fAFhQ74VzyAAfKFQbRuf8CemHA7YN-aU19Z169_WN4D_4lWnLM8NYQXqQMyCTL0izB6FZS2YfF3oRDTzp_v9lSA-5NpGIPY_Z5pi5FSit7DEkmifIYcffxUEGfGlbUZhM2lnBgrMDpI2dfGrqoG-EinsYAGik5LuagFfyL2rQUYLzZBQRAFBK13mxtV44cG1LAL-AHYjQhKyL3EjOO9lq4bP6vqdvEcTVVVGUbqC804XWD6_C5GBYVg0TbZDE2lKC3yYgIfKwUHiYkwhkxt3AWW7ifGaaucemLW8ypyzwgjktAg8WQ3r7jE_WjLB0v78yPIDgZ57fuq-wGyVUSkUP-5LQJdvsIxdDU-OXehQWX8AH9uc8XIYMKqvHhkDhgVvyQuFROexvYxxkndqclUD05PVpzMqyftWf0DfDLPQIOCwWXzeiOY1uJQRf1-nt3vGY0b76V8cjey11Pr1wuN7jNC5jbxJEnB6j7bTBHbaQVRbgNgf66cLTOk9z1mQMyalYTD9qZQ1qygp1tVnsz3koQD4iGsaekfKg_W402qLll8O0Hsuv-5Pwujc0UdFXER4MzhW3aU0A39HAFO9DDfYlc-qdiLn7DRmUO3nSi5lt6ufKE9-PQySu6u0SIZHSXbALqA=w1080-h417-no?authuser=0" width="300">

## Information Available in the Terminal

While bot.py is running, messages will appear in the terminal. Some of these may be error messages, while others are intended to inform the administrator that a graph is being downloaded, which may affect other users. Additionally, the terminal will indicate which graphs are available for users, meaning that an `imin` command for that location would not cause any temporary "blockage."

## Documentation of the Libraries Used

* [Networkx](https://networkx.github.io) - Used for graph processing.
* [Osmnx](https://osmnx.readthedocs.io/en/stable/) - Necessary for obtaining information about points of interest.
* [StaticMap](https://rometools.github.io/rome/) - Used for generating maps.
* [Python-Telegram-Bot](https://python-telegram-bot.readthedocs.io/en/stable/) - Handles everything related to the Telegram bot.

## Author

Alejandro Campayo Fernández

## References

This project was carried out following the steps provided [here](https://github.com/jordi-petit/ap2-guidebot/blob/master/README.md). The document was authored by Jordi Petit and Jordi Cortadella, professors at the Polytechnic University of Catalonia.
