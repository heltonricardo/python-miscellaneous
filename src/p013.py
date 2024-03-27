class Player:
    def __new__(cls, *args, **kwargs):
        print("Creating a new player instance")
        instance = super().__new__(cls)
        return instance

    def __init__(self, name, level):
        print("Initializing player instance")
        self.name = name
        self.level = level


player = Player("John", 1)

print("Player name:", player.name)
print("Player level:", player.level)
