from robot import Robot
class Dinosaur:
    
    def __init__(self, name, attack_power_dino):
        self.name = ""
        self.health = 100
        self.attack_power_dino = attack_power_dino

    def attack_on_robot(self,robot):
        self.damage_done = self.attack_power_dino
        self.dino_new_health = Robot.health - self.attack_power_dino
        
        
