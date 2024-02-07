class Item(object):
    def __init__(self, character, type, name, stats):
        self.name = name
        self.character = character
        self.type = type
        self.stats = stats

    def __str__(self):
        return f"{self.name} - {self.character} - {self.type} - {self.stats}"
    
    def get_type(self):
        return self.type