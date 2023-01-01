from weapon import Weapon
from dinosaur import Dinosaur

class Robot:
    
    def __init__(self, name):
        self.name = ""
        self.health = 100
        self.active_weapon = Weapon

    def attack_on_dino(self,Dinosaur,Weapon):

        self.damage_done = Weapon
        self.dino_new_health = Dinosaur.health - self.damage_done





