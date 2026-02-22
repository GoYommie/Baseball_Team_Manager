import csv
from player import Player

FILENAME = "players.csv"
FIELDNAMES = ["name", "pos", "ab", "h"]

def read_players():
    players = []
    with open(FILENAME, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f, fieldnames=FIELDNAMES)
        for row in reader:
            # convert numeric strings to int
            row["ab"] = int(row["ab"])
            row["h"] = int(row["h"])
            players.append(Player.from_dict(row))
    return players

def write_players(players):
    with open(FILENAME, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        for p in players:
            writer.writerow(p.to_dict())
