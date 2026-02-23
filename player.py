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
            "name": self.full_name,
            "pos": self.pos,
            "ab": self.ab,
            "h": self.h
        }

    @staticmethod
    def from_dict(d):
        # split full name into first and last
        parts = d["name"].split(" ", 1)
        first = parts[0]
        last = parts[1] if len(parts) > 1 else ""
        return Player(first, last, d["pos"], d["ab"], d["h"])