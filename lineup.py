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