import time
import sys
from Classes import *
from Enemy_Class import *
from Player_Class import *
from Item_Class import *
from NPC_Class import *
from Locations_Class import *
#from Quest_Class import *





time.sleep(3)
print("Herzlich Willkommen zu Trivalia")
time.sleep(2)
player_name = input_player_name()
time.sleep(2)

while True:
    print("Moechtest du dir das Tutorial anschauen?")
    print("1: Ja")
    print("2: Nein")
    inp = input()
    if inp == "1":
        show_tutorial()
        break
    elif inp == "2":
        print()
        break
    else:
        print("Bitte gib 1 oder 2 ein")


while True:
    print("Moechtest du dir die Vorgeschichte anhoeren?")
    print("1: Ja")
    print("2: Nein")
    inp = input()
    if inp == "1":
        show_introduction(player_name)
        break
    elif inp == "2":
        print("Dann viel Spass beim Spielen")
        break
    else:
        print("Bitte gib 1 oder 2 ein")





#Create Player
player1 = Player(player_name, 80, [Apple(), Potato()], starting_point, Player_Hut(), Small_Dagger(), 20, Clothes(), 50)








print("Um das Spiel zu beginnen, tippe einen Befehl ein: ")
#Game Loop
while True:

    #Quest.check_all_conditions()

    player1.hunger -= 1

    if player1.health < player1.max_health:
        player1.heal(5)

    #Main input
    temp = input().lower().strip()


    if temp == "info":
        get_info()
    elif temp == "ende":
        while True:
            print("Sicher, dass du nicht noch speichern willst?")
            print("1: Ja")
            print("2: Nein")
            inp = input()
            if inp == "1":
                quit()
            elif inp == "2":
                print("Dann lege mit \"speichern\" einen Speicherstand an")
                break
            else:
                print()


    elif player1.health <= 0:
        player1.die()

    elif "sprechen" in temp and "(" in temp:
        prompt = get_prompt(temp)
        player1.speak_to_npc(prompt[1])

    elif "reisen" in temp and "(" in temp:
        print()
        prompt = get_prompt(temp)
        for location in player1.location.nearest_destinations:
            if prompt[1] == location.name:
                player1.change_location(location)
                break
        else:
            if prompt[1].lower().strip() in Location.generate_string_array_of_locations():
                print("Dieser Ort ist zu weit entfernt")
            elif prompt[1] == player1.location.name:
                print("Du befindest dich bereits in "+first_letter_uppercase(player1.location.name))
            else:
                print(f"{player1.name} kennt diesen Ort nicht")

    elif "waffewaehlen" in temp and "(" in temp:
        prompt = get_prompt(temp)
        player1.change_main_weapon(prompt[1])

    elif "ruestungwaehlen" in temp and "(" in temp:
        prompt = get_prompt(temp)
        player1.change_armor(prompt[1])

    elif "aufheben" in temp and "(" in temp:
        prompt = get_prompt(temp)
        player1.add_item_to_inventory(prompt[1])

    elif temp == "quest":
        Quest.show_all_quests()

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
        print("Wie möchtest du deinen Speicherstand nennen? ")
        print("Wenn du doch nicht speichern möchtest, tippe \"abbrechen\"")
        temp = input()
        if temp.lower().strip() == "abbrechen":
            print("Es wurde kein Speicherstand erstellt")
        elif " " in temp:
            print("Du darfst keine Leerzeichen verwenden")
            temp = input("Wie möchtest du deinen Speicherstand nennen? ")
        else:
            create_save_file(temp, player1)

    elif temp == "laden":
        savefiles = show_save_files()
        print("Welchen Speicherstand möchtest du laden?")
        print("Wenn du keinen Speicherstand laden möchtest, tippe \"abbrechen\"")
        temp = input()
        if temp.lower().strip() == "abbrechen":
            print("Es wurde kein Speicherstand geladen")
        elif temp in savefiles:
            temp = "Save_Files/"+temp

            variables = []
            values = []
            for variable in list(locals().keys()):
                variables.append(variable)
            for value in list(locals().values()):
                values.append(value)

            load_save_file(temp, player1, variables, values)
        else:
            print("Du kannst diesen Speicherstand nicht laden")

    elif "essen" in temp and "(" in temp:
        prompt = get_prompt(temp)
        player1.eat_food(prompt[1])

    elif temp == "erkunden":
        player1.explore_location()

    elif temp == "umschauen":
        player1.look_around()



    elif "gehen" in temp and "(" in temp:
        prompt = get_prompt(temp)
        player1.change_subarea(prompt[1])

    elif "oeffnen" in temp and "(" in temp:
        prompt = get_prompt(temp)
        player1.open_chest(prompt[1])

    elif "angreifen" in temp and "(" in temp:
        prompt = get_prompt(temp)
        player1.attack(prompt[1], player1.main_weapon)

    elif "lexikon" in temp and "(" in temp:
        prompt = get_prompt(temp)
        print("Diese Funktion ist momentan noch nicht implementiert")
        #TODO pls implement
        #get_item_info(prompt[1])


    elif "trinken" in temp and "(" in temp:
        prompt = get_prompt(temp)
        player1.drink(prompt[1], Location.locations)


    else:
        print(f"{player1.name} kann dich nicht verstehen\nVersuche es mit einem anderen Befehl\nFür eine Übersicht, gib info ein")

    if player1.hunger <= 0:
        print(f"{player1.name} ist am Verhungern")
        player1.take_damage(15)

