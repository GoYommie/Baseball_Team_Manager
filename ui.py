"""
ui.py

This file contains the user interface logic for the Baseball Team Manager program.

The functions in this file handle:
- Displaying menus and headers
- Getting user input
- Showing the lineup
- Adding, removing, moving, and editing players

This file works together with:
objects.py  -> contains the Player and Lineup classes
db.py       -> handles saving and loading player data from the CSV file
"""

import db
from datetime import date, datetime
from objects import Player, Lineup


# -----------------------------------------------------------
# Constants used throughout the program
# -----------------------------------------------------------

# Valid baseball positions allowed in the program
POSITIONS = ("C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "P")

# A divider line used to make the console output look clean
LINE = "=" * 64


def display_menu():
    """
    Displays the main menu options to the user.

    This menu shows the actions that the user can perform
    such as displaying the lineup, adding a player, editing
    player stats, or exiting the program.
    """
    print(LINE)
    print(" Baseball Team Manager")
    print(" MENU OPTIONS")
    print(" 1 - Display lineup")
    print(" 2 - Add player")
    print(" 3 - Remove player")
    print(" 4 - Move player")
    print(" 5 - Edit player position")
    print(" 6 - Edit player stats")
    print(" 7 - Exit program")
    print(" POSITIONS")
    print(", ".join(POSITIONS))
    print(LINE)


def get_int(prompt):
    """
    Gets an integer value from the user.

    The function keeps asking the user for input until
    a valid integer is entered.

    Parameters
    ----------
    prompt : str
        The message displayed to the user.

    Returns
    -------
    int
        A valid integer entered by the user.
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid integer. Try again.")


def get_date(prompt, allow_blank=True):
    """
    Gets a valid date from the user.

    The date must be entered in the format YYYY-MM-DD.
    If blank input is allowed, the user can skip entering a date.

    Returns
    -------
    date or None
        Returns a date object if valid, otherwise None.
    """
    while True:
        s = input(prompt).strip()

        if allow_blank and s == "":
            return None

        try:
            return datetime.strptime(s, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date. Use YYYY-MM-DD (example: 2026-03-21).")


def display_header(current_date, game_date):
    """
    Displays the program header.

    Shows today's date and optionally the game date.
    If a game date is provided, it also shows the
    number of days remaining until the game.
    """
    print(LINE)
    print(" Baseball Team Manager")
    print()

    print(f"{'CURRENT DATE:':<15} {current_date:%Y-%m-%d}")

    if game_date is not None:
        print(f"{'GAME DATE:':<15} {game_date:%Y-%m-%d}")

        days = (game_date - current_date).days
        if days > 0:
            print(f"{'DAYS UNTIL GAME:':<15} {days}")

    print()


def get_menu_option():
    """
    Prompts the user to select a menu option.

    Only options 1 through 7 are allowed.

    Returns
    -------
    str
        The selected menu option.
    """
    while True:
        option = input("Menu option: ").strip()

        if option in ("1", "2", "3", "4", "5", "6", "7"):
            return option

        print("Invalid menu option. Try again.\n")


def get_position():
    """
    Prompts the user to enter a valid baseball position.

    Returns
    -------
    str
        A valid position from the POSITIONS list.
    """
    while True:
        pos = input("Position: ").upper().strip()

        if pos in POSITIONS:
            return pos

        print("Invalid position. Try again.")


def lineup_is_empty(players, action_name):
    """
    Checks whether the lineup has any players.

    This prevents operations like remove or edit
    when there are no players in the lineup.

    Returns
    -------
    bool
        True if the lineup is empty, otherwise False.
    """
    if len(players) == 0:
        print(f"\nNo players to {action_name}.\n")
        return True
    return False


def display_lineup(players):
    """
    Displays the current lineup of players.

    The lineup is displayed in a table format showing:
    - Player number
    - First name
    - Last name
    - Position
    - At bats
    - Hits
    - Batting average
    """
    print(LINE)

    print(f"{'No':<4}{'First':<12}{'Last':<14}{'POS':<6}{'AB':>6}{'H':>6}{'AVG':>8}")

    print("-" * 64)

    for i, p in enumerate(players, start=1):
        print(f"{i:<4}{p.first_name:<12}{p.last_name:<14}{p.pos:<6}{p.ab:>6}{p.h:>6}{p.avg:>8.3f}")

    print(LINE)
    print()


def add_player(players):
    """
    Adds a new player to the lineup.

    The user enters player information including:
    first name, last name, position, at bats, and hits.
    """
    print("\nAdd Player")

    first = input("First name: ").strip()
    last = input("Last name: ").strip()

    pos = get_position()

    at_bats = get_int("At bats: ")
    while at_bats < 0:
        print("At bats must be 0 or more.")
        at_bats = get_int("At bats: ")

    hits = get_int("Hits: ")
    while hits < 0 or hits > at_bats:
        print("Hits must be between 0 and at bats.")
        hits = get_int("Hits: ")

    players.add(Player(first, last, pos, at_bats, hits))

    db.write_players(players)

    print(f"{first} {last} was added.\n")


def remove_player(players):
    """
    Removes a player from the lineup based on their number.
    """

    print("\nRemove Player")

    if lineup_is_empty(players, "remove"):
        return

    display_lineup(players)

    number = get_int("Player number to remove: ")

    if number < 1 or number > len(players):
        print("Invalid player number.\n")
        return

    removed = players.remove(number - 1)

    db.write_players(players)

    print(f"{removed.full_name} was removed.\n")


def move_player(players):
    """
    Moves a player from one position in the lineup to another.
    """

    print("\nMove Player")

    if lineup_is_empty(players, "move"):
        return

    display_lineup(players)

    old_num = get_int("Current lineup number: ")

    if old_num < 1 or old_num > len(players):
        print("Invalid player number.\n")
        return

    new_num = get_int("New lineup number: ")

    if new_num < 1 or new_num > len(players):
        print("Invalid lineup position.\n")
        return

    player = players.get(old_num - 1)

    players.move(old_num - 1, new_num - 1)

    db.write_players(players)

    print(f"{player.full_name} moved to position {new_num}.\n")


def edit_position(players):
    """
    Allows the user to update a player's field position.
    """

    print("\nEdit Player Position")

    if lineup_is_empty(players, "edit"):
        return

    display_lineup(players)

    number = get_int("Player number: ")

    if number < 1 or number > len(players):
        print("Invalid player number.\n")
        return

    new_pos = get_position()

    player = players.get(number - 1)

    player.pos = new_pos

    db.write_players(players)

    print(f"{player.full_name}'s position updated to {new_pos}.\n")


def edit_stats(players):
    """
    Allows the user to update a player's batting statistics.
    """

    print("\nEdit Player Stats")

    if lineup_is_empty(players, "edit"):
        return

    display_lineup(players)

    number = get_int("Player number: ")

    if number < 1 or number > len(players):
        print("Invalid player number.\n")
        return

    at_bats = get_int("New at bats: ")

    while at_bats < 0:
        print("At bats must be 0 or more.")
        at_bats = get_int("New at bats: ")

    hits = get_int("New hits: ")

    while hits < 0 or hits > at_bats:
        print("Hits must be between 0 and at bats.")
        hits = get_int("New hits: ")

    player = players.get(number - 1)

    player.ab = at_bats
    player.h = hits

    db.write_players(players)

    print("Player stats updated.\n")


def main():
    """
    Main function that runs the program.

    It loads players from the CSV file and repeatedly
    displays the menu until the user chooses to exit.
    """

    players = Lineup()

    players.players = db.read_players()

    current_date = date.today()

    game_date = get_date("Game date (YYYY-MM-DD) (press Enter to skip): ", True)

    while True:

        display_header(current_date, game_date)

        display_menu()

        choice = get_menu_option()

        if choice == "1":
            display_lineup(players)

        elif choice == "2":
            add_player(players)

        elif choice == "3":
            remove_player(players)

        elif choice == "4":
            move_player(players)

        elif choice == "5":
            edit_position(players)

        elif choice == "6":
            edit_stats(players)

        elif choice == "7":
            print("Bye!")
            break