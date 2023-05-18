#!/usr/local/bin/python3

class User():
    def __init__(self, email):
        self.email = email
    
    def sign_in(self):
        print('logged in')
    
    def attack(self):
        print('Do nothing')

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power
    
    def attack(self):
        User.attack(self)
        print(f'attacking with the power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows
    
    def check_arrows(self):
        print(f'attacking with arrows: {self.num_arrows}')
    
    def run(self):
        print('ran really fast')

class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)

hb1 = HybridBorg('borgie', 50, 100)
print(hb1.attack())