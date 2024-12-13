# U.S. States Game

This project is an interactive game that helps users learn and identify all 50 U.S. states. The program uses the `turtle` and `pandas` libraries to display a map of the United States and record user input for state names.

## How to Play
1. The game starts with a blank map of the U.S.
2. The user is prompted to guess the name of a U.S. state.
3. Correct guesses will display the state's name on the map.
4. The game ends when all 50 states are correctly guessed or when the user types `Exit`.
5. Upon exiting, a CSV file (`states_to_learn.csv`) is created with the names of states that the user missed.

## Features
- Interactive map to visualize state locations.
- Keeps track of guessed and missing states.
- Generates a list of states to learn after exiting the game.

## Prerequisites
- Python 3.x
- Libraries: `turtle`, `pandas`
- Required files:
  - `blank_states_img.gif`: Image of the U.S. map.
  - `50_states.csv`: CSV file containing state names and their x, y coordinates.

## Installation and Setup
1. Clone the repository or download the files.
2. Ensure the following files are in the same directory:
   - `main.py` (the provided Python script)
   - `blank_states_img.gif`
   - `50_states.csv`
3. Install required libraries if not already installed:
   ```bash
   pip install pandas
