#Item Class
import time

class Item:

    all_currently_existing_items = []
    def __init__(self, name):
        self.name = name
        Item.all_currently_existing_items.append(self)

    def check_if_exists(self, item):

        if isinstance(item, Item):
            for element in Item.all_currently_existing_items:
                if element.name.lower().strip() == item.name.lower().strip():
                    exists = True
                    break
            else:
                exists = False
        elif isinstance(item, str):
            for element in Item.all_currently_existing_items:
                if element.name.lower().strip() == item.lower().strip():
                    exists = True
                    break
            else:
                exists = False
        return exists

    def check_if_in_subarea(self, player):

        for element in player.subarea.items:
            if element.name.lower().strip() == self.name.lower().strip():
                return True
        else:
            print(f"{player.name} findet das Item nicht")
            return False


    def find_object(item):
        if isinstance(item, str):
            for element in Item.all_currently_existing_items:
                if element.name.lower().strip() == item.lower().strip():
                    item = element
                    return item
            else:
                print("Dieses Item existiert nicht")
        else:
            return item

class Food(Item):

    def __init__(self, name, saturation):
        super().__init__(name)
        self.saturation = saturation

class Apple(Food):
    def __init__(self):
        super().__init__("apfel", 10)

class Carrot(Food):
    def __init__(self):
        super().__init__("karotte", 15)

class Potato(Food):
    def __init__(self):
        super().__init__("kartoffel", 20)

class Pumpkin(Food):
    def __init__(self):
        super().__init__("kuerbis", 35)

class Chicken_Soup(Food):
    def __init__(self):
        super().__init__("huehnersuppe", 25)

class Roast_Beef(Food):
    def __init__(self):
        super().__init__("Rinderbraten", 50)

class Roast_Pork(Food):
    def __init__(self):
        super().__init__("Schweinebraten", 70)

class Potion(Item):


    def __init__(self, name):
        super().__init__(name)

    def drink(self, player):
        raise NotImplementedError

class Healing_Potion(Potion):

    def __init__(self):
        super().__init__("heiltrank")
        self.healing = 40

class Teleportation_Potion(Potion):

    def __init__(self):
        super().__init__("teleportationstrank")

#Here you can create more Potions





class Weapon(Item):

    def __init__(self, name, damage):
        super().__init__(name)
        self.damage = damage

class Close_Combat_Weapon(Weapon):

    def __init__(self, name, damage):
        super().__init__(name, damage)

class Ranged_Combat_Weapon(Weapon):

    def __init__(self, name, damage):
        super().__init__(name, damage)

class Sword(Close_Combat_Weapon):

    def __init__(self, name, damage):
        super().__init__(name, damage)

class Wooden_Sword(Sword):

    def __init__(self):
        super().__init__("Holzschwert", 25)

class Iron_Sword(Sword):

    def __init__(self):
        super().__init__("Eisenschwert", 50)

class Mace(Close_Combat_Weapon):

    def __init__(self):
        super().__init__("Morgenstern", 75)

class Battle_Axe(Close_Combat_Weapon):

    def __init__(self):
        super().__init__("Kampfaxt", 90)

class Devils_Sword(Sword):

    def __init__(self):
        super().__init__("Teufelsschwert", 200)

    def special_attack(self):
        print()

    #TODO special swords should have special attacks, pls implement

class Victory_of_Atyr(Sword):

    def __init__(self):
        super().__init__("Sieg von Atyr", 500)

    def special_attack(self):
        print("")


class Dagger(Close_Combat_Weapon):

    def __init__(self, name, damage):
        super().__init__(name, damage)


class Small_Dagger(Dagger):

    def __init__(self):
        super().__init__("Kleiner Dolch", 20)

class Great_Dagger(Dagger):

    def __init__(self):
        super().__init__("grosser Dolch", 50)


class Armor(Item):
    #TODO if you get hurt and then take of your armor, it is possible that you die, pls fix
    def __init__(self, name, protection):
        super().__init__(name)
        self.protection = protection

class Clothes(Armor):

    def __init__(self):
        super().__init__("Lederkleidung", 0)


class Leather_Armor(Armor):
    def __init__(self):
        super().__init__("Lederruestung", 20)

class Chain_Armor(Armor):
    def __init__(self):
        super().__init__("Kettenhemd", 35)

class Iron_Armor(Armor):
    def __init__(self):
        super().__init__("Eisenruestung", 50)

class Devils_Armor(Armor):
    def __init__(self):
        super().__init__("Teufelsruestung", 100)

        #TODO pls implement that, if you have Devils_Sword and Devils_Armor, you get some kind of advantage

class Armor_of_Destiny(Armor):

    def __init__(self):
        super().__init__("Schicksalsruestung", 200)

class Element_Armor(Armor):

    def __init__(self):
        super().__init__("Elementarruestung", 400)



class Stick(Item):

    def __init__(self):
        self.name = "Stock"

class Stone(Item):

    def __init__(self):
        self.name = "Stein"

class Leaf(Item):

    def __init__(self):
        self.name = "Blatt"

class Grass(Item):

    def __init__(self):
        self.name = "Grass"

class Book(Item):

    def __init__(self):
       self.name = "Buch"

class Chair(Item):

    def __init__(self):
        self.name = "Stuhl"

class Shelf(Item):

    def __init__(self):
        self.name = "Regal"

class Feather(Item):

    def __init__(self):
        self.name = "Feder"

class Sand(Item):

    def __init__(self):
        self.name = "Sand"

if __name__ == "__main__":

    print("Bitte oeffne die Datei \"Spiel.py\"")
    time.sleep(10)

