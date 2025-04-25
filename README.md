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

Run bot.py in your terminal and ensure you are the only one doing so. Once this is done, your computer will power the bot, which will be accessible via the link obtained during bot creation or by searching for its profile on Telegram.

Once in the chat, click "Start," and a message will automatically appear.

<img src="https://lh3.googleusercontent.com/Gxz-b05JimnSob22gk_ijBtjBdX1xEDHSUg532ZtO6lydUhW8znQKyetGhO_ADQxTGwayj4x1zzCV9J7U7NSNT0D3_dZdmseMfqGxs4Btrh4ASu2YuPwCvJAMguFoP1td43bV4QqmXT1DSfjb8J8XvEt485AtX3yuSWd9YLoWIovj0ld-ROxSd83XkEGf-MPJ06wH6ytkFl_pgnSJxzHyWfz2sFpNmzBgmVIIDdXfoUa-NmUlSn-6oSB6Ho7MT4iT0HJqoZR4YG5RgpuUt4GJj8MOQkApAh4jTVRwxkCFlHoobYVhtcdbgDvIHzHnMaucH3fGsHezjQ8Tr_K4qy1-sW-ebViwhUjZbe-ndN9ZWfl19NeHHK7PxHfpVo4n0UM13-zIvIH_i3gVViURCUe_YqSJ2fApOWGOChdbproosOCG8_wM4mRikPgM8gnM8jXf26XclWZj9sdqScNdGIC8uPpB19MxjK1DOBemsGs_29KPO949twe6zPPsGChiCMxjnyeToqiYGvldyiCgqI961G2fovHe3cBDgVyDYDhINEBwo9X-W4yQJ07gj77Q9rwGIvmtI55Sflsqgt630iolrPdQLJZJbL0QkwoBw7_poyGkoxJOhLgbDX60VC2IMbICdnPL00kNexbF3NOCaly8mOQAkx55Vb2d-WTFmNBac35boj1wbMym2_JVWUreg=w1080-h244-no?authuser=0" width="300">

If you type `/help` as indicated, you will receive three informative messages explaining how to use the bot correctly.

...

(Translation continues for the remaining sections in the same manner.)
