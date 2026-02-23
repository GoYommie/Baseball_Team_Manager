import db
from datetime import date, datetime
from objects import Player,Lineup


# Constants
POSITIONS = ("C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "P")
LINE = "=" * 64


def display_menu():
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
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid integer. Try again.")

def get_date(prompt, allow_blank=True):
    while True:
        s = input(prompt).strip()
        if allow_blank and s == "":
            return None
        try:
            return datetime.strptime(s, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date. Use YYYY-MM-DD (example: 2026-03-21).")

def display_header(current_date, game_date):
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
    while True:
        option = input("Menu option: ").strip()
        if option in ("1","2","3","4","5","6","7"):
            return option
        print("Invalid menu option. Try again.\n")

def get_position():
    while True:
        pos = input("Position: ").upper().strip()
        if pos in POSITIONS:
            return pos
        print("Invalid position. Try again.")

def lineup_is_empty(players, action_name):
    if len(players) == 0:
        print(f"\nNo players to {action_name}.\n")
        return True
    return False

def calc_avg(ab, hits):
    if ab == 0:
        return 0.0
    return round(hits / ab, 3)

def display_lineup(players):
    print(LINE)
    print(f"{'No':<4}{'First':<12}{'Last':<14}{'POS':<6}{'AB':>6}{'H':>6}{'AVG':>8}")
    print("-" * 64)

    for i, p in enumerate(players, start=1):
        print(f"{i:<4}{p.first_name:<12}{p.last_name:<14}{p.pos:<6}{p.ab:>6}{p.h:>6}{p.avg:>8.3f}")

    print(LINE)
    print()

def add_player(players):
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
    # display section title
    print("\nRemove Player")

    # check if there are players in the list first
    if lineup_is_empty(players, "remove"):
        return

    # show current lineup so user can choose correctly
    display_lineup(players)

    # get player number from user
    number = get_int("Player number to remove: ")

    # validate player number range
    if number < 1 or number > len(players):
        print("Invalid player number.\n")
        return

    # remove player from list (minus 1 because list index starts at 0)
    removed = players.remove(number - 1)

    # save updated lineup back to CSV file
    db.write_players(players)

    # confirm removal to user
    print(f"{removed.full_name} was removed.\n")

def move_player(players):
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

    # get the player before moving 
    player = players.get(old_num - 1)

    # move using Lineup method
    players.move(old_num - 1, new_num - 1)

    db.write_players(players)

    print(f"{player.full_name} moved to position {new_num}.\n")

def edit_position(players):
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

