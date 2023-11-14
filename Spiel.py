import time
from Classes import *
from Enemy_Class import *
from Player_Class import *
from Functions import *
from Variables import *
import sys
from Item_Class import *
from NPC_Class import *




player_name = input_player_name()
show_introduction(player_name)
#difficulty = input_difficulty()

#Create Locations

atyr = Location("atyr", [], [])
customs_house = Location("zollhaus", [], [])
small_village = Location("kleines dorf", [], [])
starting_point = Location("hütte von "+player_name, [], [])
spruce_forest = Location("fichtenwald", [Wolf], [])
devils_reef = Location("teufelsriff", [], [])


forest_crossing = Location("waldkreuzung", [], [])
river_mouth = Location("mündung", [], [])
seagull_rock = Location("möwenfelsen", [], [])
sentry = Location("wachposten", [], [])
stone_cliffs = Location("steinklippen", [], [])
yerin = Location("yerin", [], [])

old_pirate_island = Special_Location("alte pirateninsel", [], [])
port_of_atyr = Special_Location("hafen von atyr", [], [])
ferry = Special_Location("fährhäuschen1", [], [])
ferry2 = Special_Location("fährhäuschen2", [], [])






#Initialize attributes

customs_house.initialize_location([], [yerin, ferry2])

forest_crossing.initialize_location([], [atyr, yerin, seagull_rock])

starting_point.initialize_location([Small_Hut(), Garden()], [spruce_forest, small_village, river_mouth])
spruce_forest.initialize_location([], [ferry, starting_point])
small_village.initialize_location([], [starting_point])
seagull_rock.initialize_location([], [stone_cliffs, forest_crossing])
sentry.initialize_location([], [yerin])

river_mouth.initialize_location([], [starting_point])

stone_cliffs.initialize_location([], [atyr, port_of_atyr, seagull_rock])

ferry.initialize_location([], [ferry2, spruce_forest])

ferry2.initialize_location([], [ferry, customs_house])

old_pirate_island.initialize_location([], [port_of_atyr])

port_of_atyr.initialize_location([], [old_pirate_island, atyr, stone_cliffs])

atyr.initialize_location([], [port_of_atyr,stone_cliffs, forest_crossing])

yerin.initialize_location([], [customs_house, sentry, forest_crossing])




dolch = Small_Dagger()
rüstung = Clothes()
armor2 = Leather_Armor()


#Create Player
player1 = Player(player_name, 80, [], starting_point, dolch, 40, rüstung, 50)



player1.inventory.append(Carrot())
player1.inventory.append(Pumpkin())
player1.inventory.append(Chicken_Soup())
player1.inventory.append(Roast_Beef())
player1.print_player_info()

wolf = Wolf()
wolf2 = Wolf()
schwert = Close_Combat_Weapon("Schwert", 50)

apfel = Apple()
apfel1 = Apple()
stock2 = Item("Stock")

stock = Item("Stock")

player1.inventory.append(apfel)

player1.add_item_to_inventory(schwert)
player1.add_item_to_inventory(apfel)
player1.add_item_to_inventory(armor2)


player1.show_inventory(False)
player1.print_player_info()

npc = Farmer()
npc.show_dialogue(player1)

load_save_file("speichern", player1)
#Game Loop
while True:


    player1.hunger -= 1

    temp = input().lower().strip()

    if temp == "info":
        get_info()
    elif temp == "ende":
        quit()

    elif "reisen" in temp and "(" in temp:
        print()
        prompt = get_prompt(temp)
        for location in player1.location.nearest_destinations:
            if prompt[1] == location.name:
                player1.change_location(location)
                break
        else:
            if prompt[1] in Location.locations:
                print("Dieser Ort ist zu weit entfernt")
            elif prompt[1] == player1.location.name:
                print("Du befindest dich bereits in "+first_letter_uppercase(player1.location.name))
            else:
                print(player1.name+" kennt diesen Ort nicht")

    elif "waffewählen" in temp and "(" in temp:
        prompt = get_prompt(temp)
        player1.change_main_weapon(prompt[1])

    elif "rüstungwählen" in temp and "(" in temp:
        prompt = get_prompt(temp)
        player1.change_armor(prompt[1])

    elif "aufheben" in temp and "(" in temp:
        prompt = get_prompt(temp)
        player1.add_item_to_inventory(prompt[1])

    elif "ablegen" in temp and "(" in temp:
        prompt = get_prompt(temp)
        player1.remove_item_from_inventory(prompt[1], False)

    elif temp == "inventar":
        player1.show_inventory(False)

    elif temp == "spielerinfo":
        player1.print_player_info()

    elif temp == "karte":
        show_map()

    elif temp == "speichern":

        temp = input("Wie möchtest du deinen Speicherstand nennen? ")
        if " " in temp:
            print("Du darfst keine Leerzeichen verwenden")
            temp = input("Wie möchtest du deinen Speicherstand nennen? ")
        else:
            create_save_file(temp, player1)

    elif "essen" in temp and "(" in temp:
        prompt = get_prompt(temp)
        player1.eat_food(prompt[1])

    elif temp == "erkunden":
        player1.explore_location()

    else:
        print(player1.name+ " kann dich nicht verstehen\nVersuche es mit einem anderen Befehl\nFür eine Übersicht, gib info ein")

    if player1.hunger <= 0:
        print(player1.name," ist am Verhungern")
        player1.take_damage(15)