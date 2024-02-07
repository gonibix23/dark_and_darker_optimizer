class Item(object):
    def __init__(self, character, type, name, stats):
        self.name = name
        self.character = character
        self.type = type

        for stat in stats:
            self.stats[stat] = stats[stat]

    def __str__(self):
        return f"{self.name} - {self.character} - {self.type} - {self.stats}"