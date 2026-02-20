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


def main():
    players = db.read_players()   # load from CSV at start

    while True:
        display_menu()
        choice = input("Menu option: ").strip()

        if choice == "1":
            display_lineup(players)
        elif choice == "7":
            print("Bye!")
            break
        else:
            print("Feature not added yet.\n")


if __name__ == "__main__":
    main()
