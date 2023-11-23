import time
import random
#from Functions import *
from Quest_Class import *

#Yep, this function is copied from functions.py but if i import it, a circular dependency occurs
def first_letter_uppercase_e(input):
    output = ""
    input = input.split(" ")

    for element in input:
        first_letter = element[0]
        first_letter = first_letter.upper()
        word = first_letter+element[1:]
        output = output+word+" "
    return output


class Enemy:

    def __init__(self, name, health, attack_damage, gold):
        self.name = name
        self.health = health
        self.attack_damage = attack_damage
        self.gold = gold


    def take_damage(self, damage, player):
        self.health = self.health - damage
        if self.health < 1:
            self.die(player)

    def heal(self, health):
        self.health = self.health + health

   def attack(self, target):
        print(first_letter_uppercase_e(self.name) + " greift an")
        target.health -= self.attack_damage
        if target.health >= 0:
            print(f"{target.name} hat noch {target.health} HP")
        else:
            target.die()

    def die(self, player):
        print(first_letter_uppercase_e(self.name) + " wurde besiegt")
        player.gold += self.gold
        print(f"{player.name} hat {self.gold} Gold erhalten" )
        player.subarea.enemies.remove(self)
       Quest.all_killed_enemies[self.name] += 1
        del self

class Wolf(Enemy):
    def __init__(self):
        super().__init__("Wolf", 20, 5, 1)

class Bear(Enemy):
    def __init__(self):
        super().__init__("Baer", 100, 20, 3)


class Great_Forest_Spider(Enemy):
    def __init__(self):
        super().__init__("grosse Waldspinne", 70, 35, 4)


class Barbarian(Enemy):
    def __init__(self):
        super().__init__("wilder", 45, 20, 2)


class Robber(Enemy):

    def __init__(self):
        super().__init__("Raeuber", 40, 20, 3)

    def steal_item(self, target):

        if len(target.inventory) != 0:
            print("Der Raeuber hat "+ target.name+" beraubt")
            stolen_item = random.randint(0, len(target.inventory)-1)
            print(target.inventory[stolen_item].name + " wurde gestohlen")
            target.inventory.pop(stolen_item)

        else:
            print("Dein Inventar ist leer\nDer Raeuber konnte nichts stehlen")

class Evil_Knight(Enemy):
    def __init__(self):
        super().__init__("feindlicher ritter", 80, 30, 5)

class Evil_Cavalry(Enemy):
    def __init__(self):
        super().__init__("feindlicher Reiter", 200, 50, 10)


class Evil_Heavy_Knight(Enemy):
    def __init__(self):
        super().__init__("feindlicher gepanzerter Ritter", 150, 40, 8)


class Evil_Squad(Enemy):
    def __init__(self):
        super().__init__("feindliche Soldaten", 275, 75, 15)


class Skeleton(Enemy):
    def __init__(self):
        super().__init__("skelett", 120, 40, 12)

class Zombie(Enemy):
    def __init__(self):
        super().__init__("zombie", 110, 38, 11)


class Bat(Enemy):
    def __init__(self):
        super().__init__("fledermaus", 50, 20, 4)


class Drowned_Sailor(Enemy):
    def __init__(self):
        super().__init__("ertrunkener seemann", 80, 30, 5)


class Drunken_Sailor(Enemy):
    def __init__(self):
        super().__init__("betrunkener seemann", 40, 10, 2)


class Assasin(Enemy):
    def __init__(self):
        super().__init__("Kopfgeldjaeger", 70, 60, 8)


class Boss(Enemy):
    def __init__(self, name, health, attack_damage, gold):
        super().__init__(name, health, attack_damage, gold)



class Mountain_Troll(Boss):
    def __init__(self):
        super().__init__("Bergtroll", 300, 40, 30)

    def attack(self, player):

        rand = random.randint(1,3)
        if rand == 1:
            self.special_attack(player)
        else:
            super().attack(player)

    def special_attack(self, player):

        print(f"{self.name} setzt seine Spezialattacke ein")
        time.sleep(2)
        super().attack(player)
        time.sleep(2)
        super().attack(player)



class Mage(Boss):
    def __init__(self):
        super().__init__("Magier", 400, 50, 40)

    def attack(self, player):

       rand = random.randint(1,3)
        if rand == 1:
            self.special_attack(player)
        else:
            super().attack(player)


    def special_attack(self, player):

        print(f"{self.name} setzt einen Zauberspruch ein")
        time.sleep(2)
        super().attack(player)
        time.sleep(2)
        print(f"{player.name} ist gelaehmt und kann nicht angreifen")
        time.sleep(2)
        super().attack(player)

class Water_Ghost(Boss):
    def __init__(self):
        super().__init__("Wassergeist", 300, 70, 30)


    def special_attack(self, player):

        print(f"{self.name} setzt Wasserstrahl ein")
        time.sleep(2)
        super().attack(player)
        time.sleep(2)
        super().attack(player)
        time.sleep(2)

class Fire_Ghost(Boss):
    def __init__(self):
        super().__init__("Feuergeist", 300, 70, 30)

    def special_attack(self, player):

        print(f"{self.name} setzt Feuerstrahl ein")
        time.sleep(2)
        super().attack(player)
        time.sleep(2)
        super().attack(player)
        time.sleep(2)

class Earth_Ghost(Boss):
    def __init__(self):
        super().__init__("Erdgeist", 300, 70, 30)

    def special_attack(self, player):

        print(f"{self.name} setzt Erdrutsch ein")
        time.sleep(2)
        super().attack(player)
        time.sleep(2)
        super().attack(player)
        time.sleep(2)

class Air_Ghost(Boss):
    def __init__(self):
        super().__init__("Luftgeist", 300, 70, 30)

    def special_attack(self, player):

        print(f"{self.name} setzt Starkwind ein")
        time.sleep(2)
        super().attack(player)
        time.sleep(2)
        super().attack(player)
        time.sleep(2)


if __name__ == "__main__":

    print("Bitte oeffne die Datei \"Spiel.py\"")
    time.sleep(10)

