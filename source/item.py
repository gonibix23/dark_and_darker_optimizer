class Item(object):
    def __init__(self, character, type, name, stats):
        self.name = name
        self.character = character
        self.type = type
        self.stats = stats

    def __str__(self):
        string = self.name + '\n'
        string += 'Character: ' + ', '.join(self.character) + '\n'
        string += 'Type: ' + self.type + '\n'
        for stat, value in self.stats.items():
            if value != 0:
                string += stat + ': ' + str(value) + '\n'
        return string