"""
db.py

Data access module for the Baseball Team Manager program.

<<<<<<< Updated upstream
This module is responsible for reading player data from the SQLite
database and saving updated player data back to the database.
=======
It is responsible for reading and writing player data using SQLite.
This file acts as the Data Access Layer of the program.

The program stores player information in a database file called "players.db".
>>>>>>> Stashed changes
"""

import sqlite3
from objects import Player


<<<<<<< Updated upstream
def connect():
    """
    Creates and returns a connection to the SQLite database.

    Returns
    -------
    sqlite3.Connection
        A connection object for players.db.
    """
    return sqlite3.connect("players.db")
=======
# -----------------------------------------------------------
# Database Connection
# -----------------------------------------------------------

def connect():
    """
    Creates and returns a connection to the SQLite database.
    """
    return sqlite3.connect("players.db")

>>>>>>> Stashed changes

# -----------------------------------------------------------
# Read Players
# -----------------------------------------------------------

def read_players():
    """
<<<<<<< Updated upstream
    Reads all players from the database.

    This function retrieves all rows from the Player table
    and converts them into Player objects.

    Returns
    -------
    list
        A list of Player objects.
=======
    Reads all players from the database and returns them as Player objects.
>>>>>>> Stashed changes
    """
    players = []

    conn = connect()
    cursor = conn.cursor()

<<<<<<< Updated upstream
    cursor.execute("SELECT * FROM Player ORDER BY batOrder")
=======
    cursor.execute("SELECT * FROM Player")
>>>>>>> Stashed changes
    rows = cursor.fetchall()

    for row in rows:
        player = Player(
            first_name=row[2],
            last_name=row[3],
<<<<<<< Updated upstream
            pos=row[4],
=======
            position=row[4],
>>>>>>> Stashed changes
            ab=row[5],
            h=row[6]
        )
        players.append(player)

    conn.close()
    return players


<<<<<<< Updated upstream
def get_player(player_id):
    """
    Retrieves one player from the database using playerID.

    Parameters
    ----------
    player_id : int
        The ID of the player to retrieve.

    Returns
    -------
    tuple or None
        A row from the Player table if found, otherwise None.
=======
# -----------------------------------------------------------
# Add Player
# -----------------------------------------------------------

def add_player(player):
    """
    Adds a new player to the database.
>>>>>>> Stashed changes
    """
    conn = connect()
    cursor = conn.cursor()

<<<<<<< Updated upstream
    cursor.execute("SELECT * FROM Player WHERE playerID = ?", (player_id,))
    row = cursor.fetchone()

    conn.close()
    return row


def update_player(player_id, first_name, last_name, position, at_bats, hits):
    """
    Updates one player's data in the database.

    Parameters
    ----------
    player_id : int
        The player's ID.
    first_name : str
        The updated first name.
    last_name : str
        The updated last name.
    position : str
        The updated field position.
    at_bats : int
        The updated at-bats value.
    hits : int
        The updated hits value.
    """
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE Player
        SET firstName = ?,
            lastName = ?,
            position = ?,
            atBats = ?,
            hits = ?
        WHERE playerID = ?
    """, (first_name, last_name, position, at_bats, hits, player_id))
=======
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO Player (batOrder, firstName, lastName, position, atBats, hits)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (0, player.first_name, player.last_name, player.position, player.ab, player.h))

    conn.commit()
    conn.close()


# -----------------------------------------------------------
# Delete Player (optional)
# -----------------------------------------------------------

def delete_player(player_id):
    """
    Deletes a player from the database using player ID.
    """

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Player WHERE playerID = ?", (player_id,))
>>>>>>> Stashed changes

    conn.commit()
    conn.close()