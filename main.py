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

def get_position():
    while True:
        pos = input("Position: ").upper().strip()
        if pos in POSITIONS:
            return pos
        print("Invalid position. Try again.")



def calc_avg(at_bats, hits):
    if at_bats == 0:
        return 0.0
    return round(hits / at_bats, 3)


def display_lineup(lineup):
    print()
    print(f"{'Player':<22}{'POS':<5}{'AB':<6}{'H':<6}{'AVG'}")
    print("-" * 50)
    for i, p in enumerate(lineup, start=1):
        name = p[0]
        pos = p[1]
        ab = int(p[2])
        hits = int(p[3])
        avg = calc_avg(ab, hits)
        print(f"{i:<2} {name:<20}{pos:<5}{ab:<6}{hits:<6}{avg:.3f}")
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

    players.append([name, pos, str(at_bats), str(hits)])
    db.write_players(players)
    print(f"{name} was added.\n")

def remove_player(players):
    # display section title
    print("\nRemove Player")

    # check if there are players in the list first
    if len(players) == 0:
        print("No players to remove.\n")
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


def main():
    players = db.read_players()   # load from CSV at start

    while True:
        display_menu()
        choice = input("Menu option: ").strip()

        if choice == "1":
            display_lineup(players)
        elif choice == "7":
            print("Bye!")

        elif choice == "2":
            add_player(players)
        
        elif choice == "3":
            remove_player(players)

        else:
            print("Feature not added yet.\n")


if __name__ == "__main__":
    main()
