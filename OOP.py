#OOP
class PlayerCharacter:
    # Classic Object Attribute
    membership = True
    def __init__(self, name, age):
        if (self.membership):
            self.name = name
            self.age = age
    
    def run(self):
        print('run')

player1 = PlayerCharacter('Cindy', 44)
player2 = PlayerCharacter('Tom', 21)

print(player1.membership)