from Classes import *
from Enemy_Class import *
from Variables import *
from NPC_Class import *
from Locations_Class import *



class Player:

    def __init__(self, name, health, inventory, location, subarea, main_weapon, gold, armor, hunger):
        self.name = name
        self.health = health
        self.inventory = inventory
        self.location = location
        self.subarea = subarea
        self.main_weapon = main_weapon
        self.gold = gold
        self.armor = armor
        self.hunger = hunger
        self.max_health = self.health




    def take_damage(self, damage):
        self.health = self.health - damage

        if self.health < 1:
            self.die()

    def heal(self, health):
        self.health = self.health + health

    def attack(self, Target, Weapon):
        for element in self.subarea.enemies:
            if element.name.lower().strip() == Target.lower().strip():
                Target = element
                break
        else:
            print("Dieser Gegner existiert nicht")
            return 1

        time.sleep(2)



        rand = random.randint(1,3)
        if rand == 1:
            print(self.name + " greift " + first_letter_uppercase(Target.name)+ " mit "+ first_letter_uppercase(Weapon.name)+ " an")
            Target.take_damage(Weapon.damage, self)
            if Target.health > 0:
                print(f"{self.name} hat einen kritischen Treffer erzielt")
                Target.take_damage(Weapon.damage, self)
        elif rand == 2 or rand == 3:
            print(self.name + " greift " + first_letter_uppercase(Target.name)+ " mit "+ first_letter_uppercase(Weapon.name)+ " an")
            Target.take_damage(Weapon.damage, self)

        if Target.health > 0:
            print(f"Der Gegner hat noch {Target.health} HP")

        time.sleep(3)
        if isinstance(Target, Enemy) and Target.health > 0:
            Target.attack(self)

    def die(self):
        print("Du bist gestorben\nViel Glück beim nächsten Mal")
        time.sleep(5)
        quit()

    def print_player_info(self):


        print("*", end="")
        for char in self.name:
            print("-", end="")
        for char in str(self.health):
            print("-", end="")
        for char in str(self.location.name):
            print("-", end="")
        for char in self.main_weapon.name:
            print("-", end="")
        for char in str(self.gold):
            print("-", end="")
        for char in str(self.hunger):
            print("-", end="")

        print("---------------------------------------*")

        print("| ", end="")
        print(self.name, end="")
        print(" | ", end="")
        print(self.health, " HP", end="")
        print(" | ", end="")
        print(first_letter_uppercase(self.location.name), end="")
        print(" | ", end="")
        print(self.main_weapon.name, end="")
        print(" | ", end="")
        print(self.gold, " Gold", end="")
        print(" | ", end="")
        print(self.hunger, " Sättigung", end="")
        print(" |")
        self.show_inventory(True)



    def show_inventory(self, called_by_ppi):
        if len(self.inventory) != 0:
            if not called_by_ppi:
                print(f"Inventar von {self.name}:")

            temp_array = []
            for element in self.inventory:
                temp_array.append(first_letter_uppercase(element.name))
            print_string_array_beautiful(temp_array)

        else:
            print(f"Das Inventar von {self.name} ist leer")

    def check_if_in_inventory(self, item):

        if len(self.inventory) != 0:
            if isinstance(item, str):
                for element in self.inventory:
                    if element.name.lower().strip() == item.lower().strip():
                        in_inventory = True
                        break
                else:
                    in_inventory = False
            elif isinstance(item, Item):
                for element in self.inventory:
                    if element.name.lower().strip() == item.name.lower().strip():
                        in_inventory = True
                        break
                else:
                    in_inventory = False
        else:
            in_inventory = False
        return in_inventory

    def find_Item(self, item):
        if isinstance(item, str):
            for element in self.inventory:
                if element.name.lower().strip() == item.lower().strip():
                    item = element
                    return item
            else:
                print("Dieses Item existiert nicht")
        else:
            return item



    def add_item_to_inventory(self, item):

        if Item.check_if_exists(self, item):
            item = Item.find_object(item)
            if item.check_if_in_subarea(self):
                self.inventory.append(item)

                for element in self.subarea.items:
                    if element.name.lower().strip() == item.name.lower().strip():
                        self.subarea.items.remove(element)
                Item.all_currently_existing_items.remove(item)


                print(first_letter_uppercase(item.name)+" wurde zum Inventar von "+self.name+" hinzugefügt")
        else:
            print("Dieses Item existiert nicht")




    def remove_item_from_inventory(self, item, called_by_cmw):

        if self.check_if_in_inventory(item):
            item = self.find_Item(item)
            self.inventory.remove(item)
            Item.all_currently_existing_items.append(item)

            if not called_by_cmw:
                self.subarea.items.append(item)
                print(f"{item.name} wurde abgelegt")
        else:
            print(f"{self.name} besitzt dieses Item nicht")

    def increase_Gold(self, gold):
        print(f"{self.name} hat {gold} Gold bekommen")
        self.gold += gold

    def decrease_Gold(self, gold):
        if self.gold >= gold:
            print(f"{self.name} hat {gold} Gold verloren")
            self.gold -= gold
            return True
        else:
            print(f"{self.name} hat nicht genuegend Gold")
            return False

    def change_location(self, destination):

        is_ferry = False
        temp = True
        if isinstance(destination, Special_Location):
            if isinstance(self.location, Special_Location):
                time.sleep(2)
                print(f"{self.name} muss 10 Gold bezahlen um ein Schiff nutzen zu können")
                temp = self.decrease_Gold(10)
                is_ferry = True
                time.sleep(3)
                if not temp:
                    return 1
        if temp:
            print(self.name+" begibt sich nach "+first_letter_uppercase(destination.name))
            for _ in range(10):
                time.sleep(1)
                if not is_ferry:
                    print("Wandern....")
                    temp = random.randint(1, 20)
                    if temp == 1:
                        robber1 = Robber()
                        print("Ein Räuber greift an")

                        battle_end = False
                        while True:

                            if battle_end:
                                break

                            print("Was moechtest du tun?")
                            print("1: Angreifen")
                            print("2: Fliehen")
                            inp = input()
                            if inp == "1":
                                while robber1.health >= 0 and self.health >= 0:
                                    time.sleep(2)
                                    self.health -= robber1.attack_damage
                                    print(f"Du hast noch {self.health} HP")
                                    if self.health <= 0:
                                        self.die()
                                    time.sleep(2)
                                    robber1.health -= self.main_weapon.damage
                                    print(f"Der Raeuber hat nur noch {robber1.health} HP")

                                print("Der Kampf ist vorbei")
                                battle_end = True

                            elif inp == "2":
                                temp1 = random.randint(1, 2)
                                if temp1 == 1:
                                    print(f"{self.name} konnte fliehen")
                                    break
                                elif temp1 == 2:
                                    print(f"{self.name} konnte leider nicht fliehen")
                                    print()
                                    robber1.steal_item(self)
                                    break
                            else:
                                print("Bitte gib 1 oder 2 ein")

                        else:
                            print(self.name+" kann dich nicht verstehen\nWas möchtest du tun?")
                else:
                    print("Schiff fahren....")


            print(self.name+" ist in "+ first_letter_uppercase(destination.name) + " angekommen")
            self.location = destination
            if len(destination.subareas) != 0:
                self.subarea = destination.subareas[0]

    def change_subarea(self, destination):

        for element in self.location.subareas:
            if element.name.lower().strip() == destination.lower().strip():
                destination = element
                self.subarea = destination
                print(self.name, "geht zu ", first_letter_uppercase(destination.name))

                break
        else:
            print("Dieser Ort existiert hier nicht")


    def change_main_weapon(self, new_weapon):
        for element in self.inventory:
            if element.name.lower().strip() == new_weapon.lower().strip():
                new_weapon = element

                if isinstance(new_weapon, Weapon):
                    self.inventory.append(self.main_weapon)
                    self.main_weapon = new_weapon
                    self.remove_item_from_inventory(new_weapon, True)
                    print(f"{new_weapon.name} wurde als Hauptwaffe ausgewaehlt")

                elif not isinstance(new_weapon, Weapon):
                    print(f"{new_weapon.name} ist keine Waffe")

                break
        else:
            print("Du besitzt dieses Item nicht")

    def change_armor(self, new_armor):
        for element in self.inventory:
            if element.name.lower().strip() == new_armor.lower().strip():
                new_armor = element

                if isinstance(new_armor, Armor):
                    self.inventory.append(self.armor)
                    self.health -= self.armor.protection
                    self.armor = new_armor
                    self.remove_item_from_inventory(new_armor, True)
                    print(f"{new_armor.name} wurde angelegt")
                    self.health += new_armor.protection
                    #80 is the default health value for a player, i know its bad practice but anyway
                    self.max_health = 80 + new_armor.protection

                elif not isinstance(new_armor, Armor):
                    print(f"{new_armor.name} ist keine Rüstung")

                break
        else:
            print("Du besitzt dieses Item nicht")

    def eat_food(self, food):
        if self.check_if_in_inventory(food):
            food = self.find_Item(food)
            if isinstance(food, Food):
                self.hunger += food.saturation
                print(f"{self.name} hat {food.saturation} Saettigung erhalten")
                self.remove_item_from_inventory(food, True)
            else:
                print(f"{self.name} kann das nicht essen")

    def explore_location(self):
        print(f"{self.name} erkundet die Umgebung")
        time.sleep(2)
        if len(self.location.subareas) != 0:
            sub = []

            for element in self.location.subareas:
                sub.append(first_letter_uppercase(element.name))
            print_string_array_beautiful(sub)

        else:
            print("Es gibt nichts Besonderes in der näheren Umgebung")

    def look_around(self):

        print(f"{self.name} schaut sich um")
        time.sleep(2)
        print(f"{self.name} findet:")
        things = []
        for element in self.subarea.enemies:
            things.append(first_letter_uppercase(element.name))

        for element in self.subarea.npc:
            things.append(first_letter_uppercase(element.name))

        for element in self.subarea.items:
            things.append(first_letter_uppercase(element.name))

        for element in self.subarea.chests:
            things.append(first_letter_uppercase(element.name))

        print_string_array_beautiful(things)



    def speak_to_npc(self, npc):

        for element in self.subarea.npc:
            if element.name.lower().strip() == npc.lower().strip():
                npc = element
                npc.show_dialogue(self)
                break
        else:
            print("Das ist keine Person")

    def open_chest(self, chest):

        for element in self.subarea.chests:
            if element.name.lower().strip() == chest.lower().strip():
                chest = element
                print(f"{self.name} oeffnet die Kiste")
                for element in chest.content:
                    print(self.name," erhaelt ", first_letter_uppercase(element.name))
                    self.inventory.append(element)

                self.subarea.chests.remove(chest)
                break
        else:
            print("Dies ist keine Kiste")

    def drink(self, potion, locations):
        if self.check_if_in_inventory(potion):
            potion = self.find_Item(potion)

            if isinstance(potion, Healing_Potion):
                time.sleep(2)
                if (self.health + potion.healing) <= self.max_health:
                    print(f"{self.name} hat {potion.healing} HP geheilt")
                    self.health += potion.healing
                elif (self.health + potion.healing) > self.max_health:
                    overhealing = self.health + potion.healing - self.max_health
                    self.health += potion.healing - overhealing
                    print(f"{self.name} hat {potion.healing - overhealing} HP geheilt")

                self.inventory.remove(potion)

            elif isinstance(potion, Teleportation_Potion):
                while True:
                    print("Waehle einen Ort aus, an den du reisen moechtest:")
                    destination = input()
                    for element in locations:
                        if element.name.lower().strip() == destination.lower().strip():
                            destination = element
                            self.location = destination
                            print(f"{self.name} erscheint in {first_letter_uppercase(destination.name)}")
                            self.inventory.remove(potion)
                            break
                    else:
                        print("Das ist kein Ort")

                    break


            else:
                print("Dies ist kein Trank")
        else:
            print("Du besitzt dieses Item nicht")





if __name__ == "__main__":

    print("Bitte oeffne die Datei \"Spiel.py\"")
    time.sleep(10)

