#!/usr/local/bin/python3

class User():
    def __init__(self, email):
        self.email = email
    
    def sign_in(self):
        print('logged in')
    
    def attack(self):
        print('Do nothing')

class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)
        self.name = name
        self.power = power
    
    def attack(self):
        User.attack(self)
        print(f'attacking with the power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows
    
    def attack(self):
        print(f'attacking with arrows: {self.num_arrows}')

wizard1 = Wizard('Merlin', 60, 'merlin@gmail.com')
archer1 = Archer('Robin', 30)

print(dir(wizard1))

