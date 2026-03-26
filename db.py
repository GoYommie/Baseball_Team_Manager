"""
db.py

This file acts as the Data Access Layer for the Baseball Team Manager program.

It is responsible for:
- Connecting to the SQLite database
- Reading player data
- Adding new players
- Updating existing players
- Deleting players

The database file used is: players.db
"""

import sqlite3
from objects import Player


# -----------------------------------------------------------
# CONNECT
# -----------------------------------------------------------
def connect():
    """
    Creates a connection to the SQLite database.

    Returns:
        sqlite3.Connection: Connection object used to interact with the database
    """
    # created this function so it can be used globally 
    return sqlite3.connect("players.db")


# -----------------------------------------------------------
# READ ALL PLAYERS
# -----------------------------------------------------------
def read_players():
    """
    Retrieves all players from the database.

    Returns:
        list: A list of Player objects created from database records
    """
    players = []  # list to store player objects

    conn = connect()  # database connection
    cursor = conn.cursor()

    # select all players from the table
    cursor.execute("SELECT * FROM Player")
    rows = cursor.fetchall()

    # convert each row into a Player object
    for row in rows:
        # row indexes that match database columns
        player = Player(
            first_name=row[2],   # firstName column
            last_name=row[3],    # lastName column
            pos=row[4],          # position column
            ab=row[5],           # atBats column
            h=row[6]             # hits column
        )
        players.append(player)

    conn.close()  
    return players


# -----------------------------------------------------------
# GET ONE PLAYER
# -----------------------------------------------------------
def get_player(player_id):
    """
    Retrieves a single player using their ID.

    Parameters:
        player_id (int): The ID entered by the user

    Returns:
        tuple: The database row if found, otherwise None
    """
    conn = connect()
    cursor = conn.cursor()

    # uses parameterized query 
    cursor.execute("SELECT * FROM Player WHERE playerID = ?", (player_id,))
    row = cursor.fetchone()

    conn.close()
    return row


# -----------------------------------------------------------
# ADD PLAYER
# -----------------------------------------------------------
def add_player(player):
    """
    Adds a new player to the database.

    Parameters:
        player (Player): A Player object containing player data
    """
    conn = connect()
    cursor = conn.cursor()

    # insert new player values into table
    cursor.execute("""
        INSERT INTO Player (batOrder, firstName, lastName, position, atBats, hits)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        0,                      # batOrder default value
        player.first_name,
        player.last_name,
        player.pos,
        player.ab,
        player.h
    ))

    conn.commit()  # save changes to database
    conn.close()


# -----------------------------------------------------------
# UPDATE PLAYER
# -----------------------------------------------------------
def update_player(player_id, first_name, last_name, pos, ab, hits):
    """
    Updates an existing player's data.

    Parameters:
        player_id (int): ID of the player to update
        first_name (str): Updated first name
        last_name (str): Updated last name
        pos (str): Updated position
        ab (int): Updated at-bats
        hits (int): Updated hits
    """
    conn = connect()
    cursor = conn.cursor()

    # update player record with new values
    cursor.execute("""
        UPDATE Player
        SET firstName = ?, lastName = ?, position = ?, atBats = ?, hits = ?
        WHERE playerID = ?
    """, (first_name, last_name, pos, ab, hits, player_id))

    conn.commit()
    conn.close()


# -----------------------------------------------------------
# DELETE PLAYER
# -----------------------------------------------------------
def delete_player(player_id):
    """
    Deletes a player from the database.

    Parameters:
        player_id (int): ID of the player to delete
    """
    conn = connect()
    cursor = conn.cursor()

    # delete player using ID
    cursor.execute("DELETE FROM Player WHERE playerID = ?", (player_id,))

    conn.commit()
    conn.close()