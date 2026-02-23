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