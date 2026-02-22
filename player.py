class Player:
    def __init__(self, name, pos, ab, h):
        self.name = name
        self.pos = pos
        self.ab = int(ab)
        self.h = int(h)

    def avg(self):
        if self.ab == 0:
            return 0.0
        return round(self.h / self.ab, 3)

    def to_dict(self):
        return {"name": self.name, "pos": self.pos, "ab": self.ab, "h": self.h}

    @staticmethod
    def from_dict(d):
        return Player(d["name"], d["pos"], d["ab"], d["h"])