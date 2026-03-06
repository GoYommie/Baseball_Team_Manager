"""
db.py

This file handles the data storage for the Baseball Team Manager program.

It is responsible for reading and writing player data to a CSV file.
This file acts as the Data Access Layer of the program.

The program stores player information in a file called "players.csv".
Each row in the CSV file represents one player.
"""

import csv
from objects import Player


# -----------------------------------------------------------
# Constants
# -----------------------------------------------------------

# Name of the CSV file used to store player data
FILENAME = "players.csv"

# Column names used in the CSV file
FIELDNAMES = ["first_name", "last_name", "pos", "ab", "h"]


def read_players():
    """
    Reads player data from the CSV file.

    This function opens the players.csv file and converts each row
    into a Player object using the Player.from_dict() method.

    Returns
    -------
    list
        A list of Player objects that represent the players stored
        in the CSV file.
    """

    players = []

    # open the CSV file for reading
    with open(FILENAME, newline="", encoding="utf-8") as f:

        # read the CSV rows as dictionaries
        reader = csv.DictReader(f, fieldnames=FIELDNAMES)

        for row in reader:

            # convert numeric values from strings to integers
            # because CSV files store everything as text
            row["ab"] = int(row["ab"])
            row["h"] = int(row["h"])

            # create a Player object from the dictionary
            players.append(Player.from_dict(row))

    return players


def write_players(players):
    """
    Writes player data to the CSV file.

    This function saves the current lineup of players to the
    players.csv file so the data persists after the program ends.

    Parameters
    ----------
    players : iterable
        A collection of Player objects that will be written to the file.
    """

    # open the CSV file for writing (this overwrites the old file)
    with open(FILENAME, "w", newline="", encoding="utf-8") as f:

        # create a CSV writer using the field names
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)

        # write each player's data to the file
        for p in players:
            writer.writerow(p.to_dict())