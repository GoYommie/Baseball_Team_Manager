import db

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
    print(f"{'No':<4}{'Player':<22}{'POS':<7}{'AB':>6}{'H':>6}{'AVG':>8}")
    print("-" * 64)

    for i, p in enumerate(players, start=1):
        avg = calc_avg(p["ab"], p["h"])
        print(f"{i:<4}{p['name']:<22}{p['pos']:<7}{p['ab']:>6}{p['h']:>6}{avg:>8.3f}")

    print(LINE)
    print()



def add_player(players):
    print("\nAdd Player")
    name = input("Name: ").strip()

    pos = get_position()

    at_bats = get_int("At bats: ")
    while at_bats < 0:
        print("At bats must be 0 or more.")
        at_bats = get_int("At bats: ")

    hits = get_int("Hits: ")
    while hits < 0 or hits > at_bats:
        print("Hits must be between 0 and at bats.")
        hits = get_int("Hits: ")

    players.append({"name": name, "pos": pos, "ab": at_bats, "h": hits})
    db.write_players(players)

    print(f"{name} was added.\n")

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
    removed = players.pop(number - 1)

    # save updated lineup back to CSV file
    db.write_players(players)

    # confirm removal to user
    print(f"{removed[0]} was removed.\n")

def move_player(players):
    # show section title
    print("\nMove Player")

    # check if lineup has players
    if lineup_is_empty(players, "move"):
        return

    # show lineup so user knows player numbers
    display_lineup(players)

    # get player number to move
    old_num = get_int("Current lineup number: ")

    # validate player number
    if old_num < 1 or old_num > len(players):
        print("Invalid player number.\n")
        return

    # get new lineup position
    new_num = get_int("New lineup number: ")

    # validate new position
    if new_num < 1 or new_num > len(players):
        print("Invalid lineup position.\n")
        return

    # remove player from old position
    player = players.pop(old_num - 1)

    # insert player into new position
    players.insert(new_num - 1, player)

    # save updated lineup to CSV
    db.write_players(players)

    # confirm move to user
    print(f"{player[0]} moved to position {new_num}.\n")

def edit_position(players):
    # show section title
    print("\nEdit Player Position")

    # check if lineup has players
    if lineup_is_empty(players, "edit"):
        return

    # display lineup so user sees numbers
    display_lineup(players)

    # get player number
    number = get_int("Player number: ")

    # validate player number
    if number < 1 or number > len(players):
        print("Invalid player number.\n")
        return

    # get new valid position
    new_pos = get_position()

    # update position in list
    players[number - 1][1] = new_pos

    # save updated lineup to CSV
    db.write_players(players)

    # confirm update
    print("Player position updated.\n")

def edit_stats(players):
    # show section title
    print("\nEdit Player Stats")

    # check if lineup has players
    if lineup_is_empty(players, "edit"):
        return


    # display lineup so user sees numbers
    display_lineup(players)

    # get player number
    number = get_int("Player number: ")

    # validate player number
    if number < 1 or number > len(players):
        print("Invalid player number.\n")
        return

    # get new at bats value
    at_bats = get_int("New at bats: ")
    while at_bats < 0:
        print("At bats must be 0 or more.")
        at_bats = get_int("New at bats: ")

    # get new hits value
    hits = get_int("New hits: ")
    while hits < 0 or hits > at_bats:
        print("Hits must be between 0 and at bats.")
        hits = get_int("New hits: ")

    # update values in lineup
    players[number - 1][2] = str(at_bats)
    players[number - 1][3] = str(hits)

    # save updated lineup to CSV
    db.write_players(players)

    # confirm update
    print("Player stats updated.\n")


def main():
    players = db.read_players()   # load from CSV at start

    while True:
        display_menu()
        choice = get_menu_option()

        if choice == "1":
            display_lineup(players)
        elif choice == "7":
            print("Bye!")

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

        else:
            print("Feature not added yet.\n")


if __name__ == "__main__":
    main()
