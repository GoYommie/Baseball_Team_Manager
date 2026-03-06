"""
objects.py

This file contains the main classes used in the Baseball Team Manager program.

Classes
-------
Player
    Represents a single baseball player and stores their information
    such as name, position, and batting statistics.

Lineup
    Manages the list of players in the team lineup and provides
    methods to add, remove, move, and retrieve players.
"""


class Player:
    """
    Represents a baseball player.

    A Player object stores basic information about a player including
    their first name, last name, position, number of at bats, and hits.
    It also provides properties to get the player's full name and
    calculate their batting average.
    """

    def __init__(self, first_name, last_name, pos, ab, h):
        """
        Initializes a new Player object.

        Parameters
        ----------
        first_name : str
            The player's first name.

        last_name : str
            The player's last name.

        pos : str
            The player's field position (for example CF, SS, 1B).

        ab : int
            The number of at bats the player has.

        h : int
            The number of hits the player has.
        """

        # Store the player's basic information
        self.first_name = first_name
        self.last_name = last_name
        self.pos = pos

        # Convert at bats and hits to integers to ensure calculations work correctly
        self.ab = int(ab)
        self.h = int(h)

    @property
    def full_name(self):
        """
        Returns the player's full name.

        Returns
        -------
        str
            The player's full name created by combining
            the first name and last name.
        """
        return f"{self.first_name} {self.last_name}"

    @property
    def avg(self):
        """
        Calculates the player's batting average.

        Batting average is calculated as:
        hits / at_bats

        If the player has zero at bats, the average is returned as 0.0
        to avoid dividing by zero.

        Returns
        -------
        float
            The batting average rounded to three decimal places.
        """
        if self.ab == 0:
            return 0.0
        return round(self.h / self.ab, 3)

    def to_dict(self):
        """
        Converts the Player object into a dictionary.

        This method is used when saving player data to the CSV file.

        Returns
        -------
        dict
            A dictionary containing the player's information.
        """
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "pos": self.pos,
            "ab": self.ab,
            "h": self.h
        }

    @staticmethod
    def from_dict(d):
        """
        Creates a Player object from a dictionary.

        This method is used when reading player data from the CSV file.

        Parameters
        ----------
        d : dict
            A dictionary containing player data.

        Returns
        -------
        Player
            A new Player object created from the dictionary values.
        """
        return Player(d["first_name"], d["last_name"], d["pos"], d["ab"], d["h"])


class Lineup:
    """
    Manages the list of players in the team lineup.

    The Lineup class stores Player objects in a list and provides
    methods to add, remove, move, and retrieve players.
    """

    def __init__(self):
        """
        Initializes an empty lineup.

        The lineup is stored as a list that will hold Player objects.
        """
        self.players = []

    def add(self, player):
        """
        Adds a player to the lineup.

        Parameters
        ----------
        player : Player
            The Player object that will be added to the lineup.
        """
        self.players.append(player)

    def remove(self, index):
        """
        Removes a player from the lineup.

        Parameters
        ----------
        index : int
            The position of the player in the lineup.

        Returns
        -------
        Player
            The player object that was removed from the lineup.
        """
        return self.players.pop(index)

    def move(self, old_index, new_index):
        """
        Moves a player to a new position in the lineup.

        Parameters
        ----------
        old_index : int
            The player's current position.

        new_index : int
            The new position where the player should be placed.
        """
        player = self.players.pop(old_index)
        self.players.insert(new_index, player)

    def get(self, index):
        """
        Retrieves a player from the lineup.

        Parameters
        ----------
        index : int
            The position of the player in the lineup.

        Returns
        -------
        Player
            The player object at the requested position.
        """
        return self.players[index]

    def __len__(self):
        """
        Returns the number of players in the lineup.

        Returns
        -------
        int
            The total number of players currently in the lineup.
        """
        return len(self.players)

    def __iter__(self):
        """
        Allows the lineup to be looped through using a for loop.

        Example
        -------
        for player in lineup:
            print(player.full_name)
        """
        return iter(self.players)