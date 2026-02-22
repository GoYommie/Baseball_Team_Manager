from player import Player

class Lineup:
    def __init__(self, players=None):
        self.players = players if players is not None else []

    def is_empty(self):
        return len(self.players) == 0

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, number):
        return self.players.pop(number - 1)

    def move_player(self, old_num, new_num):
        p = self.players.pop(old_num - 1)
        self.players.insert(new_num - 1, p)

    def to_dict_list(self):
        return [p.to_dict() for p in self.players]

    @staticmethod
    def from_dict_list(dict_list):
        return Lineup([Player.from_dict(d) for d in dict_list])