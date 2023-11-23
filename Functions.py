#Functions
import time
import os



from Enemy_Class import *
from Locations_Class import *


import sys

def show_introduction(playername):
    time.sleep(2)
    print(f"{playername} wacht auf")
    time.sleep(2)
    print("Draussen scheint die Sonne")
    time.sleep(2)
    print(f"Auf einmal verspuert {playername} einen unerklärlichen Drang, die Huette zu verlassen und die Welt zu erkunden")
    time.sleep(3)
    print()

def show_tutorial():
    time.sleep(2)
    print("Dies ist ein Text-Adventure")
    time.sleep(2)
    print("Das bedeutet, alles findet in Text-Form statt")
    time.sleep(2)
    print("Deinen Charakter kannst du mithilfe verschiedener Befehle steuern")
    time.sleep(3)
    print("Eine Uebersicht aller Befehle bekommst du, wenn du \"info\" eingibst")
    time.sleep(3)

def input_player_name():
    print("Wie moechtest du genannt werden?")
    player_name = str(input())
    return player_name





def input_difficulty():

    while True:
        print("Welchen Schwierigkeitsgrad moechtest du spielen?\n1: Einfach\n2: Mittel\n3: Schwer")

        inp = int(input())

        if inp == 1:
            difficulty = "Einfach"
            break
        elif inp == 2:
            difficulty = "Mittel"
            break
        elif inp == 3:
            difficulty = "Schwer"
            break
        else:
            print("Falsche Eingabe")
    return difficulty

def first_letter_uppercase(input):
    output = ""
    input = input.split(" ")

    for element in input:
        first_letter = element[0]
        first_letter = first_letter.upper()
        word = first_letter+element[1:]
        output = output+word+" "
    return output

def get_info():
    print()
    print("Hier findest du eine Liste aller Befehle: ")
    print()
    print("ablegen: Item aus dem Inventar entfernen")
    print("angreifen(Gegner): Einen Gegner angreifen")
    print("aufheben: Item zum Inventar hinzufügen")
    print("ende: Spiel beenden")
    print("erkunden: Naehere Umgebung offenlegen")
    print("essen(Nahrung): Hunger stillen")
    print("gehen: Innerhalb eines Ortes die Gegend wechseln")
    print("info: Übersicht aller Befehle")
    print("inventar: Inventar anzeigen")
    print("karte: Landkarte anzeigen")
    print("laden: Speicherstand laden")
    #print("lexikon(Gegenstand): Zeigt Informationen zu einem bestimmten Gegenstand an")
    print("oeffnen(Kiste): Kisten oeffnen")
    print("quest: Quests anzeigen")
    print("reisen(Zielort): Zu einem bestimmten Ort reisen")
    print("ruestungwaehlen(ruestung): Ruestung anlegen")
    print("speichern: Deinen aktuellen Spielstand speichern")
    print("spielerinfo: Informationen über den Spieler")
    print("sprechen(Person): Mit einer Person sprechen")
    print("trinken(Trank): Ein Getraenk oder Zaubertrank trinken")
    print("umschauen: Die Gegend nach Items, Gegnern etc. absuchen")
    print("waffewaehlen(waffe): Waffe als Hauptwaffe ausruesten")
    print()


def get_prompt(input):

    input_array = input.split("(")
    input_array[1] = input_array[1].replace(")", "")
    return input_array


def show_map():

    print("*-------------------------------------------------------------------------------------------------------------------------------------------------------------------*")
    print("| /-\  /\  /\ ° /\  /---\  /\  /---\  ° /\ °   ° /\   _   °  Nebelgebirge       °    °        Hinterland    °    /\   °     °      °     °        °        °        |")
    print("|/   \/-/\/--/\/--\/ /-\ \/--\/     /\ /--\/-\ °/--\ / \  /\  X*  °       °    °         °      X        /\     /  \     °      Stadtmauer /\ °    °   °      °     |")
    print("|  /\ \/  /\/--\/\ \/   \/ /\ \  /\/--\/\ /-\ \//\  /   \/ /\   *****  °     °    /()\       °    **  ° /  \/\ /    \  °       °  *X***   |\/|X Verlassener Palast° |")
    print("| /  \/  /  \  /--\/ /\/\ /--\ \/-//\  \ /   \//--\/-/\--\/\-\  °    X Die Oede  /    \  °      °   ** / /\ \ /      \     ° ||------||***    */\|\   °        °    |")
    print("|/    \ /    \/    \/  \ /    \/ //--\  /  /\ /    \/  \ /  \ \   °   **     °  /      \     °        ***X Steinbruch  °       ** °       ***X Ruinenstadt °        |")
    print("|WWWWWWWWWWW\/     /   X/      \//    \/  /  \  /\  /\  / /\ \ \     °  ** °   /   X    \        °      *     ° Schlachtfeld **  °   °  ^/\ * /|°***   °       °    |")
    print("|WWWWWW\***********Diamantenmine/      \ /    \/  \/  \/ /  \ \  °        *   ° ***  Vulkan °      °    *   °   ********X****   /\      °  * /|  ^  *****  °        |")
    print("|WWWWW\*/WWWWWWWWWWWWWWWWWWWWWWWWWWW\   /      \X /    \/    \       °     X****   °   °       °     °   * *****    °     °  /\/  \  °     *|--|  °    ° ***     °  |")
    print("|WWWW\ *  /WWWWWWWWWWWWWWWWWWWWWWWWW\/WWWWWWWWW\ *Todesschlucht  °      ° * Geroellfelder   °     °  *****X Die Passage /\  /  \  /\  °  °  |/\|     °   °  ** °    |")
    print("|WWW\  X Holzfäller /WWWWWWWWWWWWWWWWWWW\ 000000 *   °      °       °  ***   °      °  ° /| X******** °   *   °      ° /  \/  __\/  \   °  ° X* Stadttor ° /\ *  °  |")
    print("|-\°/W\ *** /WWWWWWWWW\   OOOOOOOOOOOOOOOOOOOOO  *   *********  °  ****          °        Dorfruinen     ° *      °   /    \_/~//    \ °   °  *    °   /\ //\\* /\  |")
    print("| ~\°  /WW\*****/WWWWWWWWWWW\ 00000000000000000 * *** °       ****X*******   °        °        °       °   *  °       °   _/~_/X Quelle  °   *XAusguck/  \  X* /  \ |")
    print("|~  \----\°     *****  ° /WWWW\Wasserfall00000 ***   °     °     Grenzturm****   °        °       °       *     °       _/~_/   ******/WWW\**/WW\  Verlassene Minen |")
    print("|  ~  ~~  |   °   °  *  °   /WWWW\ X/WWWWW\***X Huegelland      °        °    *****     °      °  *******X Grasfelder  /~ /    /WWWWW\*** */WWWWWWWWWWWWWWWWWW\  °  |")
    print("|   ~  /\~ \-------\°*    °   /WWWW\*******  * °     °   /WWWWWWWWWWWWWWWWWWW\     ******    °   *   °    *****  °     \ ~\_  °  /WWWWWW\*/WWWWWWWWWWWWWWWWWWWWWWWW\|")
    print("| ~~  ~~ /\ ~~~/\~/\|X Teufelsriff /WWWWWWW\*    °  /WWWWWWWWWWWWWW\ 000000000000000000  ******** 00000    °   *    °   \_ ~\  °   /WWWW\*/WWWWWWWWWWWWWWWWWWWWWWWWW|")
    print("|   ~ ~~/\/W\ /\~/\ | *   °       °        *   °       /WWWWWWW\ 0000Waldfestung0000000000000000000    °     /\* °      ° \ ~\  °   /WWWW*/WWWWWWWW\***X Dunkelwald/|")
    print("|~~    ~~  /WWW\ /\ /  *       °      °    *       °     °    00000000*X0000000000000000000   °     °      /\Letol   ° __/ ~ /   /WWWWWWW\*/WWWW\***/WWWWWWWWWWWWWWW|")
    print("|  ~     ~~     ~  |  ° * stuermige Küste°  * Bauernhof      ° 0******00***000000000000    °     °     °  /\***X/\°    / ~ _/  °  /WWWWWWW\X*****/WWWWWWWWWWWWWWW\  |")
    print("|     ~  ~  ~~    ~ \°  X********  °   ° ***X*   °        °  ***00000000000***000000  °   **********Muehle**  /\/\  ° / ~ /   Verlorener Wald/WW\**/WWWWWWWWWWW\   °|")
    print("| ~~        ~   ~    \---°   °  *********  °  **   /\  °   **  °     000000000***0000*****   °  ^^^^***X^^^^^  °   ° | ~ / °   °°  °   /WWWWWWWWWW\**/WWWWWWWW\  °  |")
    print("|     ~~   ~  ~    ~      \-----\°      °     ° */\ /\*****      °   °  00000    X***00000 °   ° ^^^^^^^**^^^^^  °   \ ~ \__    °    °     °    °    *  °   °   °  °|")
    print("|        ~           ~~      ~   |  °     °    /\*Yto*/\      °       00000000*Lichtung00000 °  ^^^^^^^^^^**^^^^^   ° \__ ~ \--__   °   ° °  °   °  *    °  ^   ^°  |")
    print("|   ~      ~~~   ~         ~  ~~  \   °      °  /\*X*/\    °     ° 0000000**** 0000000000000000 °^^^^^^^^^^^**^^^ °   °  \--\__~ \   °°   °  ° °  °   *     °   °   |")
    print("|       ~    ~~        ~      ~    |      °   °     *  °      ° 000000X***0000000000000000000  °   ° ^^^^^^^^^**Faehrhaeuschen2\~ \Faehrhaeuschen1/\/\X Aytol   °   |")
    print("|        ~~        ____      ~~     \ °         °    *    °     °  00Alter Wachturm0000000000000000000000   ° ° *   °   ° ***X*|**|*X   ° ^   °°  /\**/\   °      ° |")
    print("|    ~        ~   /  ° \~       ~~   |     °    ||---/\----||        °  000000000000000000000000000000   °   Zollhaus****** __/ ~ |  **/WWWWWWWWW\**/\/\       °    |")
    print("|        ~~      / /WW\ \---\~     ~  \ °    ° // /\/\*/\/\/|\    °     °    °   00000000 |-| Wachposten    °   ***X* __/--/ ~ __/ /WW\**/WWWWW\**/WWWWWWWWWWWWWW\  |")
    print("|   ~      ~  /_/ /WWWWWW\° |   ~~    / ° °   || /\/\X Atyr/|\||*****************   00000 | | 000 X**  °°   **** __-/ ~ ___/-/ ° /WWWWWW\***/\**/WWWWWWWWWWWW\   °  |")
    print("|       ~~    \° /WWWWWWW\ /  ~     ~ |     ° |/\/\/\ */\/\/\//    *    ^   °   ******  00000000 °   **/\ **    _/ ~  ~ /  °  ^°  /WWWWWWWW\*X/\Fichtenwald/WWWW\ ° |")
    print("|   ~   ~    ~ \____X_____/    ~~~    \  °     \||---/*\|--||/   °  *   °°     °  0 00****00000    ° /\*X*/\   /  ~  ~ /  Muendung^ /WWWWWWW\*/WWWWWWWWWWWWW\   °   |")
    print("| Alte Pirateninsel *       ~~      ~  \--\  °    °  Hafen von Atyr *       °   0000000000*0000  ° /\Yerin/\  / ~   ~ |  X  °   ° /WWWWWWWW\*/WWWWWWWWWWW\   °    ° |")
    print("|    ~~      ~       **    ~    ~~     ~~  \-----\  /-X-------\  °  *   °    0000000000000 X**00  ° **/\/\  / ~   ~  /  ° **** /WWWWW\/WWW\*/WWWWWWWWW\  °      °   |")
    print("|        ~         ~~  ***          ~~     ~   ~  \/  *  ~     |   *     °  000Waldkreuzung*00******   ° /-/    ~    | °   °  ****/WWWWW\**/WWWWWWWWWWWWWW\  °  ^  °|")
    print("|   ~~~      ~~      ~~   **** ~    ~    ~~    ~~   ***    ~  / ° *   °    ° 00000  000000*0000000   °  /   ~     ~  |   ^  /WWWW\*****X* Deine Huette/WWWWW\  °    |")
    print("|         ~~      ~      ~   ******   ~   *********** ~ /----/ ° * ************   °    00*00  00   ° /-/  ~   ~~     \ °°  ° ° /WWWW\*/WWWWWWWWWWWWWWWWW\   °     ° |")
    print("|  ~     ~~   ~  ~~    ~   ~~     ********* ~     ~~    |    °  ***  °   °     ***   °  *   °  ° /--/    ~~      ~    \_  °   ^   °  *     °      ^°      °     °   |")
    print("|     ~     ~       ~        ~     ~~   ~      ~~      /Steinklippen/-------\  °  **  **  ° /---/   ~~       ~~     ~   \  °   °    **       ^     °   °    ^^      |")
    print("| ~~     ~     ~         ~~       ~         ~     ~   /  X /___/---/   ~  ~  \----\ *X /---/   ~       ~~        ~~      \__ ° ^  °   **    °    __  °^   °     °  _|")
    print("|     ~     ~     ~    ~      ~~~     ~~      ~~     |\___/ |_/   ~~     ~    ~    \--/Moewenfelsen~       ~         ~      \__ °   °  ********X ||/\/\/\    °  __/ |")
    print("|      ~~~        ~~~    ~       ~~        ~~        \|___|/  ~~      ~~    ~   ~~    ~  ~~    ~       ~~        ~~     ~      \__  kleines Dorf/\/\/\/[]\ °___/  ~ |")
    print("|  ~~        ~~       ~      ~        ~~     ~   ~~    ~~     ~   ~~     ~   ~     ~~    ~       ~~~~      ~       ~~      ~~     \_____   °°   ____   °  _/    ~~  |")
    print("|    ~    ~      ~~       ~~      ~       ~      ~         ~~         ~   ~      ~      ~    ~         ~       ~      ~~       ~     ~  \__  __/ ~  \____/  ~     ~ |")
    print("|      ~      ~~       ~       ~      ~~      ~~       ~        ~~~       ~~       ~~      ~     ~~       ~~       ~       ~~     ~    ~~  \/  ~   ~~    ~    ~~    |")
    print("*-------------------------------------------------------------------------------------------------------------------------------------------------------------------*")


def create_save_file(filename, player1):



    for dirs, subdirs, files in os.walk("Save_Files"):
        for file in files:
            if filename+".txt" == file:
                print("Dieser Speicherstand existiert schon")
                break

        else:
            with open("Save_Files\\"+filename+".txt", "x") as file:

                file.write("player1.name=")
                file.write(str(player1.name))
                file.write("\n")
                file.write("player1.health=")
                file.write(str(player1.health))
                file.write("\n")
                file.write("player1.inventory=")
                inventory = []
                for element in player1.inventory:
                    inventory.append(element.name)

                file.write(str(inventory))
                file.write("\n")
                file.write("player1.location=")
                file.write(str(player1.location.name))
                file.write("\n")
                file.write("player1.subarea=")
                file.write(str(player1.subarea.name))
                file.write("\n")
                file.write("player1.main_weapon=")
                file.write(str(player1.main_weapon.name))
                file.write("\n")
                file.write("player1.gold=")
                file.write(str(player1.gold))
                file.write("\n")
                file.write("player1.armor=")
                file.write(str(player1.armor.name))
                file.write("\n")
                file.write("player1.hunger=")
                file.write(str(player1.hunger))
                file.write("\n")
                file.write("player1.max_health=")
                file.write(str(player1.max_health))
                file.write("\n")

                print("Dein Spielstand wurde erfolgreich gespeichert")
                file.close()

def show_save_files():
    print("Speicherstaende:")
    path = "Save_Files"
    savefiles = []
    for dirs, subdirs, files in os.walk(path):
        for file in files:
            file = file.split(".")
            savefiles.append(file[0])

    print_string_array_beautiful(savefiles)
    return savefiles



def read_save_file(filename):
    array = []
    with open(filename+".txt", "r") as file:
        for lines in file:
            value = lines.split("=")
            value = value[1].strip()
            array.append(value)

        return array

def find_object_by_name(class_name):
    #Doesnt know why but its working
    import inspect, sys

    modules = ["Item_Class", "Player_Class"]
    for module_name in modules:
        module = sys.modules[module_name]

        for name, obj in inspect.getmembers(module):
            if inspect.isclass(obj):
                attributes = getattr(obj, "__init__", None)
                signature = inspect.signature(attributes)
                if len(signature.parameters) == 1:
                    num1 = obj().name.lower().strip()
                    num2 = class_name.lower().strip()
                    if obj().name.lower().strip()==class_name.lower().strip():
                        obj = obj()
                        return obj

def find_location(class_name, variables, values):

    for element in values:
        if isinstance(element, Location) or isinstance(element, Sub_Area):
            if class_name.lower().strip() == element.name.lower().strip():
                obj = element
                return obj



def load_save_file(filename, player, variables, values):




    array = read_save_file(filename)
    player.name = array[0]
    player.health = int(array[1])

    inventory = array[2]
    inventory = inventory.replace("[", "")
    inventory = inventory.replace("]", "")
    inventory = inventory.replace("'", "")
    inventory = inventory.split(",")

    temp_ar = []
    for element in inventory:
        temp_ar.append(find_object_by_name(element))
    player.inventory = temp_ar

    player.location = find_location(array[3], variables, values)
    player.subarea = find_object_by_name(array[4])
    player.main_weapon = find_object_by_name(array[5])
    player.gold = int(array[6])
    player.armor = find_object_by_name(array[7])
    player.hunger = int(array[8])
    player.max_health = int(array[9])

    print("Speicherstand wurde erfolgreich geladen")
    time.sleep(3)
    return player


def print_string_array_beautiful(array):

    string = ""
    for element in array:
        string += "| "
        string += element
        string += " "
    string += "|"

    print("*", end="")
    for _ in range(len(string)-2):
        print("-", end="")
    print("*")

    print(string)

    print("*", end="")
    for _ in range(len(string)-2):
        print("-", end="")
    print("*")

def get_item_info(thing):
    #Does not have to be an Item, can also be an Entity or something else

    if isinstance(thing, Enemy()) and not isinstance(thing, Boss()):
        print("Name: ",thing.name)
        print("HP: ", thing.health)
        print("Schaden: ", thing.attack_damage)
        print("Belohnung: ", thing.gold, " Gold")
        #TODO please map all things here
    else:
        print("Diesen Gegenstand gibt es nicht")




if __name__ == "__main__":

    print("Bitte oeffne die Datei \"Spiel.py\"")
    time.sleep(10)

