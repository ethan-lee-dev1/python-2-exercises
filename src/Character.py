import random

class Character:

    def __init__(self, hit_points):
        self.hit_points = hit_points

    def fight(self, character):
        random_number = random.randint(1, 20)
        character.hit_points -= random_number
        if character.hit_points < 0:
            character.hit_points = 0
        

# Figter
class Fighter(Character):
    def __repr__(self):
        return f"Fighter : {self.hit_points} hit points."

# Dwarf
class Dwarf(Character):
    def __repr__(self):
        return f"Dwarf : {self.hit_points} hit points."
    
