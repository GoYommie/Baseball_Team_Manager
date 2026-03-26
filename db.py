"""
db.py

Data access module for the Baseball Team Manager program.

This module is responsible for reading player data from the SQLite
database and saving updated player data back to the database.
"""

import sqlite3
from objects import Player


def connect():
    """
    Creates and returns a connection to the SQLite database.

    Returns
    -------
    sqlite3.Connection
        A connection object for players.db.
    """
    return sqlite3.connect("players.db")


def read_players():
    """
    Reads all players from the database.

    This function retrieves all rows from the Player table
    and converts them into Player objects.

    Returns
    -------
    list
        A list of Player objects.
    """
    players = []

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Player ORDER BY batOrder")
    rows = cursor.fetchall()

    for row in rows:
        player = Player(
            first_name=row[2],
            last_name=row[3],
            pos=row[4],
            ab=row[5],
            h=row[6]
        )
        players.append(player)

    conn.close()
    return players


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
    """
    conn = connect()
    cursor = conn.cursor()

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

    conn.commit()
    conn.close()