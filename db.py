import csv

FILENAME = "players.csv"

def read_players():
    players = []
    with open(FILENAME, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            # row: [full_name, position, at_bats, hits]
            players.append(row)
    return players

def write_players(players):
    with open(FILENAME, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(players)
