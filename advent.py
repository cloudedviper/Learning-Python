class Advent:
    def __init__(self, name, weapon, materia, gender):
        self.name = name
        self.weapon = weapon
        self.materia = materia
        self.gender = gender

    alive = True

    def attack(self):
        print(f"{self.name} Attacks with {self.weapon} for 9999!!")
        return self

    def spell(self):
        print(f"{self.name} Attacks with {self.materia}!!")
        return self


class Villain(Advent):
    undead = True

    def attack(self):
        print(f"{self.name} Attacks with {self.weapon} for 9999!!")
        return self

    def spell(self):
        print(f"{self.name} Attacks with {self.materia} !")
        return self


# yuf = Advent("yuffie", "ninja star", "steal", "female")
# vin = Advent("Vincent", "Gun", "Chaos", "male")
# seph = Villain("Sephiroth", "Murasama", "Super Nova", "male")
# squ = Advent("Squall", "Lionheart", "Ultima", "male")
# ulta = Villain("Ultimecia", "Magic", "Time", "female")
#
# # method chaining
# ulta.attack().spell().spell()
# print(seph.undead)
