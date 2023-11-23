import random
import time
from Item_Class import *
from Functions import *


class NPC:

    all_currently_existing_npcs = []

    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.dialogue = random.randint(1, 3)
        NPC.all_currently_existing_npcs.append(self)

    def die(self):
        print(f"{self.name} ist gestorben")

    def show_dialogue(self):
        raise NotImplementedError("Nicht implementiert")





class Farmer(NPC):

    def __init__(self):
        super().__init__("Bauer", 30)

    def show_dialogue(self, player):


        if self.dialogue == 1:
            print("Die Sonne steht heute gut, findest du nicht auch?")
        elif self.dialogue == 2:
            print("Ich habe dich hier noch nie gesehen")
            time.sleep(1)
            print("Von woher kommst du?")
            while True:
                print("1: Ich komme von hinter den Bergen")
                print("2: Ich bin ein Reisender aus Atyr")
                temp = input()
                if temp == "1":
                    print("Oh, du bist weit gereist")
                    time.sleep(1)
                    print("Du musst bestimmt hungrig sein")
                    print("Nimm eine Karotte von mir")
                    player.inventory.append(Carrot())
                    break
                elif temp == "2":
                    time.sleep(1)
                    print("Du kommst also aus der Hauptstadt")
                    time.sleep(1)
                    print("Dann wünsche ich dir viel Glück bei deiner weiteren Reise")
                    time.sleep(1)
                    break
                else:
                    print()
        elif self.dialogue == 3:
            print("Ich arbeite hier")

class Resident(NPC):
    def __init__(self):
        super().__init__("Bewohner", 20)


    def show_dialogue(self, player):


        if self.dialogue == 1:
            time.sleep(1)
            print("Was suchst du hier?")
        elif self.dialogue == 2:
            print("Wenn du nicht sofort das Haus verlässt, rufe ich die Stadtwache")
        elif self.dialogue == 3:
            print("Wer bist du?")


class Villager(NPC):
    def __init__(self):
        super().__init__("Dorfbewohner", 30)


    def show_dialogue(self, player):

        if self.dialogue == 1:
            time.sleep(1)
            print("Willkommen, Fremder in unserem Dorf")
        elif self.dialogue == 2:
            time.sleep(1)
            print("Guten Tag")
        elif self.dialogue ==3:
            time.sleep(1)
            print("Danke für deinen Besuch")
            time.sleep(1)
            print("Nimm bitte einen Apfel von mir")
            player.inventory.append(Apple())

class Priest(NPC):
    def __init__(self):
        super().__init__("Priester", 20)


    def show_dialogue(self, player):

        if self.dialogue == 1:
            time.sleep(1)
            print("Gesegnet seiest Du")
        elif self.dialogue == 2:
            print("Wie ist dein Name, mein Kind?")
            time.sleep(3)
            print(player.name, " heißt du also")
            time.sleep(2)
            print("Dann wuensche ich dir noch viel Erfolg auf deinem Weg")
        elif self.dialogue == 3:
            print("")

class Merchant(NPC):

    possible_products = {Wooden_Sword(): 10, Iron_Sword():20, Mace(): 30, Battle_Axe(): 40, Great_Dagger(): 20,
                         Leather_Armor():10, Chain_Armor(): 15, Iron_Armor(): 20,
                         Healing_Potion(): 10,
                         Apple(): 3, Carrot(): 5, Potato(): 4, Roast_Beef(): 10, Roast_Pork(): 10}
    def __init__(self):
        super().__init__("haendler", 40)
        self.offer = {}


        temp_products = Merchant.possible_products
        for _ in range(5):
            randomchoice = random.choice(list(temp_products.items()))
            temp_dict = {}

            temp_dict[randomchoice[0]] = randomchoice[1]
            self.offer.update(dict(temp_dict))

    def first_letter_uppercase(self, input):
        output = ""
        input = input.split(" ")

        for element in input:
            first_letter = element[0]
            first_letter = first_letter.upper()
            word = first_letter+element[1:]
            output = output+word+" "
        return output

    def show_offer(self):

        offer = self.offer
        print()
        print("Angebot")
        for element in offer:
            print(f"{self.first_letter_uppercase(element.name)}: {offer[element]} Gold")
        print()

    def sell_product(self, player):
        print("Was moechtest du kaufen?")
        print("Wenn du nichts kaufen moechtest, sag mir bitte \"Nichts\"")
        temp = input()
        if temp.lower().strip() == "nichts":
            time.sleep(2)
            print("Dir entgeht ein gutes Angebot")
            return 0

        for element in self.offer:
            if element.name.lower().strip() == temp.lower().strip():
                temp = element
                if self.offer[temp] > player.gold:
                    print("Du hast nicht genuegend Gold um das zu kaufen")
                else:
                    print("Eine gute Wahl")
                    player.decrease_Gold(self.offer[temp])
                    player.inventory.append(element)
                    time.sleep(2)
                    print("Es war mir eine Freude, mit dir Geschaefte zu machen")
                    time.sleep(2)
                    break
        else:
            print("Das verkaufe ich hier nicht")


    def show_dialogue(self, player):

        time.sleep(1)
        print("Du moechtest also etwas kaufen mein Freund")
        time.sleep(2)
        print("Da bist du bei mir genau richtig")
        time.sleep(2)
        self.show_offer()
        time.sleep(2)
        self.sell_product(player)

class Worker(NPC):
    def __init__(self):
        super().__init__("arbeiter", 40)

    def show_dialogue(self, player):
        print("Heute ist die Arbeit besonders schwer")


class Innkeeper(NPC):
    def __init__(self):
        super().__init__("wirt", 30)

    def show_dialogue(self, player):

        if self.dialogue == 1:
            print("Hier nimm ein Getraenk")
        elif self.dialogue == 2:
            while True:
                print("Bist du in meiner Taverne um zu trinken, oder dich zu pruegeln?")
                print("1: Pruegeln")
                print("2: Trinken")
                inp = input()
                if inp == "1":
                    time.sleep(2)
                    print("Dann scher dich weg")
                    time.sleep(1)
                    break
                elif inp == "2":
                    time.sleep(2)
                    print("Dann nimm ein Getränk")
                    break
                else:
                    print("Was für einen Unsinn redest du da?")
        elif self.dialogue == 3:
            print("Willkommen in meiner Kneipe")


class Town_Guard(NPC):
    def __init__(self):
        super().__init__("stadtwache", 80)


    def show_dialogue(self, player):

        if self.dialogue ==1:
            time.sleep(2)
            print("Ich bin hier um zu bewachen, nicht, um mit Leuten zu sprechen")
            time.sleep(2)
        elif self.dialogue == 2:
            time.sleep(2)
            print("Was moechtest du von mir?")
            time.sleep(2)
            print("Geh bitte weg")
        elif self.dialogue == 3:
            time.sleep(2)
            print("Wage es nicht, dich der großen Wache zu naehern")
            time.sleep(3)
            print("Du wirst es sonst bereuen")

class Miller(NPC):
    def __init__(self):
        super().__init__("mueller", 40)

    def show_dialogue(self, player):

        if self.dialogue == 1:
            time.sleep(2)
            print("Ich mahle das Korn")
        elif self.dialogue == 2:
            time.sleep(2)
            print("Was machst du in meiner Muehle?")
            time.sleep(2)
            print("Bitte verlasse dieses Gebaeude")
        elif self.dialogue == 3:
            time.sleep(2)
            print("Ich versuche hier Brot zu machen")
            time.sleep(1)
            print("Wenn ich fertig bin, gebe ich dir eins")


class Lumberman(NPC):
    def __init__(self):
        super().__init__("holzfaeller", 40)


    def show_dialogue(self, player):


        if self.dialogue == 1:
            time.sleep(2)
            print("Ich hacke Holz")
            time.sleep(2)
        elif self.dialogue == 2:
            time.sleep(2)
            print("Was willst du Fremder?")
            while True:
                print("1: Ich moechte Holz kaufen")
                print("2: Ich habe mich verlaufen")
                inp = input()
                if inp == "1":
                    time.sleep(2)
                    print("Ich verkaufe kein Holz an zwielichtige Gestalten")
                    time.sleep(2)
                    break
                elif inp == "2":
                    time.sleep(2)
                    print("Du hast dich also verlaufen")
                    time.sleep(2)
                    print("Egal wohin du wolltest, der Weg fuehrt auf jeden Fall nicht zu mir")
                    time.sleep(3)
                    break
                else:
                    print()
        elif self.dialogue == 3:
            time.sleep(2)
            print("Hallo Fremder")
            time.sleep(2)

class Miner(NPC):
    def __init__(self):
        super().__init__("bergarbeiter", 40)


    def show_dialogue(self, player):


        if self.dialogue == 1:
            time.sleep(2)
            print("Was machst du denn hier?")
            time.sleep(2)
            print("Wir sind hier in einer Mine, hier kann nicht einfach jeder hereinspazieren")
            time.sleep(3)
            print("Pass auf dich auf")
        elif self.dialogue == 2:
            time.sleep(2)
            print("Wir schuerfen hier schon seit Jahren")
            time.sleep(2)
            print("Aber das Erz wird immer weniger")
            time.sleep(2)
            print("Wir muessen immer tiefer graben, um etwas zu finden")
            time.sleep(3)
        elif self.dialogue == 3:
            time.sleep(2)
            print("Ich liebe es, nach Erz zu schuerfen")
            time.sleep(2)

class Gardener(NPC):
    def __init__(self):
        super().__init__("gaertner", 30)

    def show_dialogue(self, player):


        if self.dialogue == 1:
            time.sleep(2)
            print("Ich liebe, es, im Garten zu arbeiten")
            time.sleep(2)

            while True:
                print("Magst du Gaerten auch so wie ich?")
                print("1: Ja, ich liebe Gaerten")
                print("2: Nein, ich hasse Gaerten")
                inp = input()
                if inp == "1":
                    time.sleep(2)
                    print("Dann haben wir ja etwas gemeinsam")
                    time.sleep(2)
                    print("Wusstest du eigentlich, dass Kartoffeln früher auch Teufelsfrucht genannt wurden?")
                    time.sleep(3)
                    print("Oder, dass Tomaten eigentlich zu den Beeren gehören?")
                    time.sleep(3)
                    break

                elif inp=="2":
                    time.sleep(2)
                    print("Was wagst du es, mich so zu beleidigen?")
                    time.sleep(3)
                    print("Verlasse auf der Stelle meinen Garten")
                    time.sleep(2)
                    break
                else:
                    print()


        elif self.dialogue == 2:
            time.sleep(2)
            print("Ich habe gerade geerntet, hier hast du eine Kartoffel")
            time.sleep(2)
            player.inventory.append(Potato())
        elif self.dialogue == 3:
            time.sleep(2)
            print("Bei diesem Wetter gedeihen die Pflanzen ganz praechtig")


class Mushroom_Gatherer(NPC):
    def __init__(self):
        super().__init__("Pilzsammler", 30)


    def show_dialogue(self, player):


        if self.dialogue == 1:
            time.sleep(2)
            print("Ich suche hier Pilze")

        elif self.dialogue == 2:
            time.sleep(2)
            print("Hast du hier irgendwo Pilze gesehen?")
            time.sleep(2)
            print("Ich finde keine")
            while True:
                print("1: Es gibt hier keine Pilze")
                print("2: Dort drueben muessten welche sein")
                inp = input()
                if inp == "1":
                    print("Oh, das wusste ich nicht")
                    time.sleep(2)
                    print("Du musst dich ja sehr gut mit Pilzen auskennen")
                    time.sleep(2)
                    print("Hier nimm als Dank von mir einen Pilz")
                    time.sleep(5)
                    print("Ach ja, das hatte ich vergessen, ich habe ja noch gar keine Pilze gefunden")
                    break
                elif inp == "2":
                    time.sleep(2)
                    print("Vielen Dank")
                    time.sleep(2)
                    print("Ich werde mich dort drueben mal umschauen")
                    time.sleep(2)
                    break
                else:
                    time.sleep(2)

        elif self.dialogue == 3:
            time.sleep(2)
            print("Guck mal Fremder")
            time.sleep(2)
            print("Ich habe schon viele Pilze gesammelt")
            time.sleep(2)
            print("Schau, dort ist so ein schoener roter Pilz")
            time.sleep(2)
            print("Der hat sogar so schoene weisse Punkte")

class Traveller(NPC):
    def __init__(self):
        super().__init__("reisender", 40)


    def show_dialogue(self, player):


        if self.dialogue == 1:
            time.sleep(2)
            while True:
                print("Bist du auch ein Reisender wie Ich?")
                print("1: Ja")
                print("2: Nein")
                inp = input()
                if inp == "1":
                    time.sleep(2)
                    while True:
                        print("Woher kommst du denn?")
                        print("1: Von weit weit weg")
                        print("2: Von nebenan")
                        inp2 = input()
                        if inp2 == "1":
                            time.sleep(2)
                            print("Dann wuensche ich dir noch eine gute Reise")
                            break
                        elif inp2 == "2":
                            time.sleep(2)
                            print("Dann hast du den Grossteil deiner Reise noch vor dir")
                            time.sleep(2)
                            break
                        else:
                            print()
                    break
                elif inp == "2":
                    time.sleep(2)
                    print("Jeder von uns ist auf seine Art ein Reisender")
                    time.sleep(3)
                    print("Denn ist das Leben nicht eine einzige grosse Reise?")
                    time.sleep(2)
                    break
        elif self.dialogue == 2:
            time.sleep(2)
            print("Hallo Fremder")
            time.sleep(2)
            print("Ich habe leider keine Zeit")
            time.sleep(2)
            print("Ich muss weiter reisen")
            time.sleep(2)

        elif self.dialogue == 3:
            time.sleep(2)
            print("Ich komme von weit her, und habe vieles gesehen")
            time.sleep(2)
            print("Warst du schonmal im Nebelgebirge?")
            time.sleep(2)
            print("Ich war dort")
            time.sleep(2)
            print("Legenden besagen, dass im Norden eine zerstörte Stadt liegt")
            time.sleep(3)
            print("Niemand weiss, warum sie zerstört ist")
            time.sleep(2)
            print("Manche behaupten, sie waere in einem Krieg mit Atyr gefallen")
            time.sleep(3)
            print("Andere sagen, es haette etwas mit dem Berg des Feuers zu tun")
            time.sleep(3)
            print("Ich habe die Stadt mit eigenen Augen gesehen")
            time.sleep(2)

if __name__ == "__main__":

    print("Bitte oeffne die Datei \"Spiel.py\"")
    time.sleep(10)
    
