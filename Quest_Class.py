#Quest
from Item_Class import *

class Quest:

    all_open_quests = []

    all_killed_enemies = {"Feuergeist": 0, "Wassergeist": 0, "Erdgeist": 0, "Luftgeist": 0, "Wolf": 0, "Baer": 0, "grosse Waldspinne": 0, }
    all_gathered_items = {}
    all_visited_locations = {}
    #TODO append all enemies, items and locations, which are necessary for a quest

    def __init__(self, name):
        self.name = name
        Quest.all_open_quests.append(self)


    @staticmethod
    def show_all_quests():
        for element in Quest.all_open_quests:
            print(element.name)
        #TODO

    @staticmethod
    def check_all_conditions():
        for element in Quest.all_open_quests:
            element.check_condition
            if element.condition:
                element.get_reward()

    def check_condition(self):
        raise NotImplementedError

    def get_reward(self):
        raise NotImplementedError



class Gather_Ten_Rocks(Quest):
    #TODO you cant do this Quest because you cant pick up stones
    def __init__(self):
        super().__init__("Sammle Zehn Steine")
        #TODO Delete this Quest




class Kill_All_Ghosts(Quest):

    def __init__(self):
        super().__init__("Besiege alle Elementgeister")
        self.condition = False


    def check_condition(self):

        if Quest.all_killed_enemies["Feuergeist"] > 0:
            if Quest.all_killed_enemies["Wassergeist"] > 0:
                if Quest.all_killed_enemies["Erdgeist"] > 0:
                    if Quest.all_killed_enemies["Luftgeist"] > 0:
                        self.condition = True


    def get_reward(self, player):

        if self.condition:
            print(f"{player.name} hat die Quest \"{self.name}\" abgeschlossen")
            player.inventory.append(Element_Armor())
            print(f"{player.name} hat eine {Element_Armor().name} erhalten")
            Quest.all_open_quests.remove(self)


class Kill_One_Wolf(Quest):

    def __init__(self):
        super().__init__("Besiege einen Wolf")
        self.condition = False

    def check_condition(self):
        if Quest.all_killed_enemies["Wolf"] >= 1:
            self.condition = True

    def get_reward(self, player):

        if self.condition:
            print(f"{player.name} hat die Quest \"{self.name}\" abgeschlossen")
            player.gold -= 2
            print(f"{player.name} hat 2 Gold erhalten")

#TODO Quests wont be saved, pls implement

#Here i create an instance of every quest to have them append to all_quests
quest = Kill_All_Ghosts()
quest = Kill_One_Wolf()

