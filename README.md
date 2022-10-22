# PingPong Classic

PingPong is a two-dimensional table tennis simulation game.

## Rules

---

PingPong is played according to the following rules.

- Players can move up and down...
  - Player one moves using the 'W' and 'S' keys.
  - Player two moves using the '↑' and '↓' keys.
- Players hit the ball to try to get past the side of the opposing player.
- The player with the most points after 9 rounds will win.
  - A "game over" message is displayed in the middle of the screen.

## Interface

---

![PingPong Interface](https://user-images.githubusercontent.com/44569083/197333600-92800b97-e369-4fd0-9a2a-9e53e3be2bdb.PNG)

## Getting Started

---

Make sure you have Python 3.8.0 or newer and Raylib Python CFFI 3.7 installed and running on your machine. You can install Raylib Python CFFI by opening a terminal and running the following command.

```
python3 -m pip install raylib
```

After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.

```
python3 pingpong
```

or

```
py pingpong
```

You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the
project folder. Select the main module inside the greed folder and click the "run" icon.

## Project Structure

---

The project files and folders are organized as follows:

```
  root                (project root folder)
  +-- pingpong        (source code for game)
    +-- assets        (game assets)
    +-- game          (specific game classes)
    +-- __main__.py   (entry point for program)
    +-- constants.py  (constant values used by the modules)
  +-- README.md       (general info)
```

## Required Technologies

---

- Python 3.8.0
- Raylib Python CFFI 3.7

## Authors

---

- Reuel Magistrado (mag21010@byui.edu)
