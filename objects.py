class Player:
    def __init__(self, first_name, last_name, pos, ab, h):
        self.first_name = first_name
        self.last_name = last_name
        self.pos = pos
        self.ab = int(ab)
        self.h = int(h)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def avg(self):
        if self.ab == 0:
            return 0.0
        return round(self.h / self.ab, 3)

    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "pos": self.pos,
            "ab": self.ab,
            "h": self.h
        }

    @staticmethod
    def from_dict(d):
        return Player(d["first_name"], d["last_name"], d["pos"], d["ab"], d["h"])
    
class Lineup:
    def __init__(self):
        self.players = []

    def add(self, player):
        self.players.append(player)

    def remove(self, index):
        return self.players.pop(index)

    def move(self, old_index, new_index):
        player = self.players.pop(old_index)
        self.players.insert(new_index, player)

    def get(self, index):
        return self.players[index]

    def __len__(self):
        return len(self.players)

    def __iter__(self):
        return iter(self.players)