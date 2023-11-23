from Classes import *
from Item_Class import *
from Enemy_Class import *
from NPC_Class import *

class Location:

    locations = []

    def __init__(self, name, subareas, nearest_destinations):
        self.name = name
        self.subareas = subareas
        self.nearest_destinations = nearest_destinations
        Location.locations.append(self)

    @staticmethod
    def generate_string_array_of_locations():
        loc_ar = []
        for element in Location.locations:
            loc_ar.append(element.name.lower().strip())
        return loc_ar

    #You need this method because the constructor needs objects as his arguments that do not exist at the time of the construction
    def initialize_location(self, subareas, nearest_destinations):

        for element in subareas:
            self.subareas.append(element)

        for element in nearest_destinations:
            self.nearest_destinations.append(element)

class Special_Location(Location):

    def __init__(self, name, subareas, nearest_destinations):
        super().__init__(name, subareas, nearest_destinations)

    def unlock_path(self, destination):
        self.nearest_destinations.append(destination)





class Sub_Area():


    def __init__(self, name, npc, enemies, items, chests):
        self.name = name
        self.npc = npc
        self.enemies = enemies
        self.items = items
        self.chests = chests

    def show_items(self):
        for element in self.items:
            print(element.name)

    def show_npc(self):
        for element in self.npc:
            print(element.name)

    def show_enemies(self):
        for element in self.enemies:
            print(element.name)

    def show_chests(self):
        for element in self.chests:
            print(element.name)

class Building(Sub_Area):

    def __init__(self, name, npc, enemies, items, chests):
        super().__init__(name, npc, enemies, items, chests)




class Player_Hut(Building):
    def __init__(self):
        super().__init__("Deine Huette", [], [], [], [Chest()])

class Small_Hut(Building):

    def __init__(self):
        temp = random.randint(1, 3)
        if temp ==1:
            super().__init__("kleine Huette", [], [], [], [Chest()])
        elif temp ==2:
            super().__init__("kleine Huette", [Resident()], [], [], [])
        elif temp ==3:
            super().__init__("kleine Huette", [Resident()], [], [], [Chest()])

class Half_Timbered_House(Building):

    def __init__(self):
        temp = random.randint(1, 3)
        if temp == 1:
            super().__init__("fachwerkhaus", [Resident()], [], [Book()], [Chest()])
        elif temp == 2:
            super().__init__("fachwerkhaus", [Resident(), Villager()], [Shelf()], [], [])
        elif temp == 3:
            super().__init__("fachwerkhaus", [], [], [Chair()], [Chest()])

class Marketplace(Sub_Area):

    def __init__(self):
        temp = random.randint(1, 3)
        if temp == 1:
            super().__init__("marktplatz", [Villager(), Merchant()], [], [], [Chest(), Chest()])
        elif temp == 2:
            super().__init__("marktplatz", [Merchant()], [Assasin()], [], [])
        elif temp == 3:
            super().__init__("marktplatz", [Merchant()], [], [], [Chest()])

class Warehouse(Building):

    def __init__(self):
        temp = random.randint(1, 3)
        if temp == 1:
            super().__init__("lagerhaus", [Worker()], [], [], [Chest(), Chest()])
        elif temp == 2:
            super().__init__("lagerhaus", [Worker()], [], [], [Chest()])
        elif temp == 3:
            super().__init__("lagerhaus", [], [Assasin()], [], [Chest(), Chest()])

class Church(Building):

    def __init__(self):
        temp = random.randint(1, 3)
        if temp == 1:
            super().__init__("kirche", [Priest()], [], [], [Chest(), Chest(), Chest()])
        elif temp == 2:
            super().__init__("kirche", [Priest(), Villager()], [], [], [Chest()])
        elif temp == 3:
            super().__init__("kirche", [Priest()], [], [], [Chest()])

class Tavern(Building):

    def __init__(self):
        temp = random.randint(1, 3)
        if temp == 1:
            super().__init__("gasthaus", [Innkeeper(), Villager()], [], [], [Chest()])
        elif temp == 2:
            super().__init__("gasthaus", [Innkeeper()], [Drunken_Sailor()], [], [])
        elif temp == 3:
            super().__init__("gasthaus", [Villager()], [], [], [Chest()])

class Gate(Building):

    def __init__(self):
        temp = random.randint(1, 3)
        if temp == 1:
            super().__init__("stadttor", [Town_Guard()], [], [], [])
        elif temp == 2:
            super().__init__("stadttor", [Worker()], [], [], [Chest()])
        elif temp == 3:
            super().__init__("stadttor", [Town_Guard(), Worker()], [], [], [])

class Ruined_Gate(Building):

    def __init__(self):

        temp = random.randint(1, 3)
        if temp == 1:
            super().__init__("verlassenes stadttor", [], [Skeleton()], [], [Chest()])
        elif temp == 2:
            super().__init__("verlassenes stadttor", [], [Skeleton()], [], [Chest()])
        elif temp == 3:
            super().__init__("verlassenes stadttor", [], [Skeleton()], [], [Chest()])

class Ruined_Tower(Building):

    def __init__(self):

        temp = random.randint(1, 3)
        if temp == 1:
            super().__init__("verlassener turm", [], [], [], [Chest()])
        elif temp == 2:
           super().__init__("verlassener turm", [], [], [], [Chest(), Chest()])
        elif temp == 3:
            super().__init__("verlassener turm", [], [], [], [Chest()])

class Ruined_Wall(Building):

    def __init__(self):

        temp = random.randint(1, 3)
        if temp == 1:
            super().__init__("verlassene stadtmauer", [], [Zombie()], [], [Chest()])
        elif temp == 2:
            super().__init__("verlassene stadtmauer", [], [Zombie(), Skeleton()], [], [Chest()])
        elif temp == 3:
            super().__init__("verlassene stadtmauer", [], [Skeleton()], [], [Chest()])

class Ruined_House(Building):

    def __init__(self):

        temp = random.randint(1, 3)
        if temp == 1:
            super().__init__("verlassenes Haus", [], [], [Stone()], [])
        elif temp == 2:
            super().__init__("verlassenes Haus", [], [], [], [Chest()])
        elif temp == 3:
            super().__init__("verlassenes Haus", [], [], [Stone()], [Chest()])


class Wall(Building):

    def __init__(self):
        temp = random.randint(1, 3)
        if temp == 1:
            super().__init__("stadtmauer", [Town_Guard(), Villager()], [], [], [])
        elif temp == 2:
            super().__init__("stadtmauer", [Town_Guard()], [], [], [])
        elif temp == 3:
            super().__init__("stadtmauer", [Worker()], [], [], [])

class Tower(Building):

    def __init__(self):
        temp = random.randint(1, 3)
        if temp == 1:
            super().__init__("turm", [Town_Guard()], [], [], [Chest()])
        elif temp == 2:
            super().__init__("turm", [Town_Guard(), Worker()], [], [], [Chest()])
        elif temp == 3:
            super().__init__("turm", [], [], [], [Chest(), Chest()])

class Fortress(Building):

    def __init__(self):
        temp = random.randint(1, 3)
        if temp == 1:
            super().__init__("festung", [], [Evil_Squad()], [], [Chest()])
        elif temp == 2:
            super().__init__("festung", [], [Evil_Heavy_Knight()], [], [Chest(), Chest()])
        elif temp == 3:
            super().__init__("festung", [], [Evil_Knight(), Evil_Knight()], [], [Chest()])

class Windmill(Building):

    def __init__(self):
        temp = random.randint(1, 3)
        if temp == 1:
            super().__init__("windmuehle", [Miller(), Farmer()], [], [], [Chest()])
        elif temp == 2:
            super().__init__("windmuehle", [Miller()], [], [], [Chest()])
        elif temp == 3:
            super().__init__("windmuehle", [], [Evil_Knight()], [], [])

class Farm_House(Building):

    def __init__(self):
        temp = random.randint(1, 3)
        if temp == 1:
            super().__init__("scheune", [Farmer(), Worker()], [], [], [Chest()])
        elif temp == 2:
            super().__init__("scheune", [Farmer()], [], [], [Chest()])
        elif temp == 3:
            super().__init__("scheune", [Worker()], [Evil_Knight()], [], [])

class Lumberjack(Building):

    def __init__(self):
        temp = random.randint(1, 3)
        if temp == 1:
            super().__init__("holzfaeller", [Lumberman(), Worker()], [], [], [Stick()])
        elif temp == 2:
            super().__init__("holzfaeller", [Lumberman()], [], [], [Stick()])
        elif temp == 3:
            super().__init__("holzfaeller", [Lumberman()], [Evil_Knight], [], [])

class Mine_Shaft(Building):

    def __init__(self):
        temp = random.randint(1, 3)
        if temp == 1:
            super().__init__("minenschacht", [Miner(), Worker()], [Bat()], [Stone()], [])
        elif temp == 2:
            super().__init__("minenschacht", [Miner()], [Bat()], [Stone()], [])
        elif temp == 3:
            super().__init__("minenschacht", [Miner()], [], [Stone()], [])

class Abandoned_Mine_Shaft(Building):

    def __init__(self):
        temp = random.randint(1, 3)
        if temp == 1:
            super().__init__("verlassener minenschacht", [], [Bat()], [Stone()], [])
        elif temp == 2:
            super().__init__("verlassener minenschacht", [], [Bat()], [Stone()], [])
        elif temp == 3:
            super().__init__("verlassener minenschacht", [], [], [Stone()], [])

class Dungeon(Building):

    def __init__(self):
        temp = random.randint(1, 3)
        if temp == 1:
            super().__init__("dungeon", [], [Mage(), Skeleton()], [Armor_of_Destiny()], [])
        elif temp == 2:
            super().__init__("dungeon", [], [Mountain_Troll(), Zombie()], [Armor_of_Destiny()], [])
        elif temp == 3:
            super().__init__("dungeon", [], [Earth_Ghost(), Skeleton()], [Victory_of_Atyr()], [])

class Witch_House(Building):

    def __init__(self):
        temp = random.randint(1, 3)
        if temp == 1:
            super().__init__("hexenhaus", [], [], [Healing_Potion()], [Chest()])
        elif temp == 2:
            super().__init__("hexenhaus", [], [], [Teleportation_Potion()], [Chest()])
        elif temp == 3:
            super().__init__("hexenhaus", [], [], [Healing_Potion()], [Chest()])

class Abandoned_Palace(Building):

    def __init__(self):
        temp = random.randint(1, 3)
        if temp == 1:
            super().__init__("verlassener palast", [], [Zombie(), Skeleton(), Zombie()], [], [Chest(), Chest(), Chest()])
        elif temp == 2:
            super().__init__("verlassener palast", [], [Zombie(), Skeleton()], [], [Chest(), Chest()])
        elif temp == 3:
            super().__init__("verlassener palast", [], [Zombie(), Mage(), Mage()], [], [Chest(), Victory_of_Atyr()])

class Field(Sub_Area):

    def __init__(self, name, npc, enemies, items, chests):
        super().__init__(name, npc, enemies, items, chests)

class Player_Garden(Field):
    def __init__(self):
        super().__init__("dein garten", [], [], [Apple(), Potato(), Carrot()], [])

class Garden(Field):

    def __init__(self):
        temp = random.randint(1, 3)
        if temp == 1:
            super().__init__("gemuesegarten", [Gardener()], [], [Apple(), Apple(), Potato(), Carrot(), Pumpkin()], [])
        elif temp == 2:
            super().__init__("gemuesegarten", [Gardener()], [], [Apple(), Potato(), Carrot()], [])
        elif temp == 3:
            super().__init__("gemuesegarten", [], [], [Apple(), Apple(), Potato()], [])

class Farmland(Field):

    def __init__(self):
        temp = random.randint(1, 3)
        if temp == 1:
            super().__init__("acker", [Farmer(), Worker()], [], [Potato(), Potato(), Potato(), Potato()], [])
        elif temp == 2:
            super().__init__("acker", [Farmer()], [], [Carrot(), Carrot(), Carrot(), Carrot()], [])
        elif temp == 3:
            super().__init__("acker", [Farmer()], [], [Pumpkin(), Pumpkin(), Pumpkin()], [])

class Grass_Field(Field):

    def __init__(self):
        temp = random.randint(1, 3)
        if temp == 1:
            super().__init__("grassfeld", [], [Evil_Cavalry()], [Grass()], [])
        elif temp == 2:
            super().__init__("grassfeld", [Traveller()], [], [Grass()], [])
        elif temp == 3:
            super().__init__("grassfeld", [], [Evil_Knight(), Evil_Knight()], [Grass()], [])

class Pasture(Field):

    def __init__(self):
        temp = random.randint(1, 3)
        if temp == 1:
            super().__init__("weide", [Farmer()], [], [Grass()], [])
        elif temp == 2:
            super().__init__("weide", [], [Evil_Squad()], [Grass()], [])
        elif temp == 3:
            super().__init__("weide", [Farmer()], [], [], [])

class Pond(Field):

    def __init__(self):
        temp = random.randint(1, 3)
        if temp == 1:
            super().__init__("teich", [], [], [Stone()], [])
        elif temp == 2:
            super().__init__("teich", [], [], [], [])
        elif temp == 3:
            super().__init__("teich", [Traveller()], [], [Stone()], [])

class Stream(Field):

    def __init__(self):
        temp = random.randint(1, 3)
        if temp == 1:
            super().__init__("bach", [], [], [Stone()], [])
        elif temp == 2:
            super().__init__("bach", [], [Barbarian()], [Stone()], [])
        elif temp == 3:
            super().__init__("bach", [], [], [Stone()], [])

class River(Field):

    def __init__(self):
        temp = random.randint(1, 3)
        if temp == 1:
            super().__init__("fluss", [Traveller()], [], [], [])
        elif temp == 2:
            super().__init__("fluss", [], [Drowned_Sailor()], [], [])
        elif temp == 3:
            super().__init__("fluss", [], [], [Stone()], [])


class Beach(Field):

    def __init__(self):
        temp = random.randint(1, 3)
        if temp == 1:
            super().__init__("strand", [], [], [Sand()], [])
        elif temp == 2:
            super().__init__("strand", [], [Drowned_Sailor()], [Sand()], [])
        elif temp == 3:
            super().__init__("strand", [], [], [Sand()], [])

class Cliffs(Field):

    def __init__(self):
        temp = random.randint(1, 3)
        if temp == 1:
            super().__init__("Steilkueste", [Traveller()], [], [Stone()], [])
        elif temp == 2:
            super().__init__("Steilkueste", [], [], [Stone(), Grass()], [])
        elif temp == 3:
            super().__init__("steilkueste", [], [], [Grass()], [])

class Reef(Field):

    def __init__(self):
        temp = random.randint(1, 3)
        if temp == 1:
            super().__init__("riff", [], [Drowned_Sailor()], [Stone()], [])
        elif temp == 2:
            super().__init__("riff", [Traveller()], [], [Grass()], [])
        elif temp == 3:
            super().__init__("riff", [], [Drowned_Sailor(), Drowned_Sailor()], [Stone()], [])

class Cave(Field):

    def __init__(self):
        temp = random.randint(1, 3)
        if temp == 1:
            super().__init__("hoehle", [], [Bat()], [Stone()], [])
        elif temp == 2:
            super().__init__("hoehle", [], [Bat(), Skeleton()], [], [])
        elif temp == 3:
            super().__init__("hoehle", [], [Bear()], [Stone()], [])

class Underground_Stream(Field):

    def __init__(self):
        temp = random.randint(1, 3)
        if temp == 1:
            super().__init__("unterirdischer Bach", [], [Bat()], [Stone()], [])
        elif temp == 2:
            super().__init__("unterirdischer Bach", [], [Bat(), Zombie()], [Stone()], [])
        elif temp == 3:
            super().__init__("unterirdischer Bach", [], [Zombie()], [Stone()], [])


class Forest(Field):

    def __init__(self):
        temp = random.randint(1,3)
        if temp ==1:
            super().__init__("wald", [Mushroom_Gatherer()], [Wolf()], [Grass(), Stick(), Stone()], [])
        elif temp ==2:
            super().__init__("wald", [Traveller()], [Wolf(), Wolf()], [Stick()], [])
        elif temp ==3:
            super().__init__("wald", [], [Wolf(), Wolf(), Wolf()], [Stick()], [])

class Dark_Forest(Field):
    def __init__(self):
        temp = random.randint(1, 3)
        if temp == 1:
            super().__init__("dunkelwald", [], [Great_Forest_Spider()], [Stick(), Stone()], [])
        elif temp == 2:
            super().__init__("dunkelwald", [], [Great_Forest_Spider(), Wolf()], [Stick()], [])
        elif temp == 3:
            super().__init__("dunkelwald", [], [Zombie()], [Stick()], [])

class Stump(Field):

    def __init__(self):
        temp = random.randint(1, 3)
        if temp == 1:
            super().__init__("Baumstumpf", [Mushroom_Gatherer()], [], [Stick()], [])
        elif temp == 2:
            super().__init__("Baumstumpf", [], [], [Stone()], [])
        elif temp == 3:
            super().__init__("Baumstumpf", [], [Barbarian()], [Stick(), Leaf()], [])

class Fallen_Tree(Field):

    def __init__(self):
        temp = random.randint(1, 3)
        if temp == 1:
            super().__init__("umgestuerzter Baum", [], [Bear()], [Leaf()], [])
        elif temp == 2:
            super().__init__("umgestuerzter Baum", [], [], [Stick(), Stone()], [])
        elif temp == 3:
            super().__init__("umgestuerzter Baum", [], [Mage()], [Stick()], [])

class Hill(Field):

    def __init__(self):
        temp = random.randint(1, 3)
        if temp == 1:
            super().__init__("Huegel", [Traveller()], [], [Grass()], [])
        elif temp == 2:
            super().__init__("Huegel", [], [Evil_Squad()], [Grass()], [])
        elif temp == 3:
            super().__init__("Huegel", [], [Evil_Heavy_Knight], [], [])

class Rock(Field):

    def __init__(self):
        temp = random.randint(1, 3)
        if temp == 1:
            super().__init__("Felsen", [], [Evil_Knight()], [Stone()], [])
        elif temp == 2:
            super().__init__("Felsen", [], [Barbarian()], [], [])
        elif temp == 3:
            super().__init__("Felsen", [], [Barbarian()], [Stone()], [])

class Mountain(Field):

    def __init__(self):
        temp = random.randint(1, 3)
        if temp == 1:
            super().__init__("Berg", [], [], [Stone()], [])
        elif temp == 2:
            super().__init__("Berg", [], [Air_Ghost()], [Stone()], [])
        elif temp == 3:
            super().__init__("Berg", [], [Mountain_Troll()], [Stone()], [])

class Canyon(Field):

    def __init__(self):
        temp = random.randint(1, 3)
        if temp == 1:
            super().__init__("Schlucht", [Traveller()], [Wolf()], [Stone()], [])
        elif temp == 2:
            super().__init__("Schlucht", [], [Evil_Cavalry()], [Stone()], [])
        elif temp == 3:
            super().__init__("Schlucht", [Traveller()], [Barbarian(), Barbarian()], [Stone()], [])


class Wastelands(Field):

    def __init__(self):
        temp = random.randint(1, 3)
        if temp == 1:
            super().__init__("Einoede", [], [], [Stone()], [])
        elif temp == 2:
            super().__init__("Einoede", [], [Evil_Heavy_Knight()], [], [])
        elif temp == 3:
            super().__init__("Einoede", [], [], [Stone()], [])

class Scree(Field):

    def __init__(self):
        temp = random.randint(1, 3)
        if temp == 1:
            super().__init__("Geroell", [Traveller()], [], [Stone()], [])
        elif temp == 2:
            super().__init__("Geroell", [], [Barbarian(), Barbarian()], [Stone()], [])
        elif temp == 3:
            super().__init__("Geroell", [], [], [Stone()], [])

class Battlefield(Field):

    def __init__(self):
        temp = random.randint(1,3)
        if temp == 1:
            super().__init__("Schlachtfeld", [], [Zombie()], [Stone()], [])
        elif temp == 2:
            super().__init__("Schlachtfeld", [], [Skeleton()], [Stone()], [])
        elif temp == 3:
            super().__init__("Schlachtfeld", [], [Zombie(), Skeleton()], [Stone()], [])

class Lava_Field(Field):

    def __init__(self):
        temp = random.randint(1,2)
        if temp == 1:
            super().__init__("Lavafeld", [], [Fire_Ghost()], [Devils_Sword()], [])
        elif temp == 2:
            super().__init__("Lavafeld", [], [Fire_Ghost()], [Devils_Armor()], [])



#Yes, I know, Chest is not a Location but it works this way so i dont care
class Chest():

    def __init__(self):

        self.name = "Kiste"
        self.content = []

        #Amount of items in the chest
        rand = random.randint(1, 5)

        for _ in range(rand):
            #Specific item selection
            rand_temp = random.randint(1, 62)
            if rand_temp in [1, 2, 3, 4, 5]:
                self.content.append(Apple())

            elif rand_temp in [6, 7, 8, 9]:
                self.content.append(Wooden_Sword())

            elif rand_temp in [10, 11, 12, 13]:
                self.content.append(Small_Dagger())

            elif rand_temp in [14, 15, 16, 17]:
                self.content.append(Carrot())

            elif rand_temp in [18, 19, 20]:
                self.content.append(Roast_Beef())

            elif rand_temp in [20, 21, 22]:
                self.content.append(Leather_Armor())

            elif rand_temp in [23, 24, 25]:
                self.content.append(Great_Dagger())

            elif rand_temp in [26, 27, 28, 29]:
                self.content.append(Potato())

            elif rand_temp in [30, 31, 32]:
                self.content.append(Pumpkin())

            elif rand_temp in [33, 34, 35]:
                self.content.append(Chicken_Soup())

            elif rand_temp in [36, 37]:
                self.content.append(Roast_Beef())

            elif rand_temp in [38, 39]:
                self.content.append(Roast_Pork())

            elif rand_temp in [40, 41, 42, 43, 44]:
                self.content.append(Wooden_Sword())

            elif rand_temp in [45, 46, 47, 48]:
                self.content.append(Iron_Sword())

            elif rand_temp in [49, 50, 51]:
                self.content.append(Mace())

            elif rand_temp in [52, 53]:
                self.content.append(Carrot())

            elif rand_temp in [54]:
                self.content.append(Battle_Axe())

            elif rand_temp in [55, 56, 57, 58, 59]:
                self.content.append(Small_Dagger())

            elif rand_temp in [60, 61, 62]:
                self.content.append(Great_Dagger())

            elif rand_temp in [63, 64]:
                self.content.append(Healing_Potion())

            elif rand_temp in [65, 66]:
                self.content.append(Teleportation_Potion())

            elif rand_temp in [67, 68]:
                self.content.append(Chain_Armor())

            elif rand_temp in [69, 70]:
                self.content.append(Iron_Armor())

            #Here you can append some other items that could spawn in a chest


    def show_content(self):
        for element in self.content:
            print(element.name)



#Create Locations

abandoned_palace = Location("verlassener palast", [], [])
abandoned_mines = Location("verlassene minen", [], [])
atyr = Location("atyr", [], [])
aytol = Location("aytol", [], [])
battlefield = Location("schlachtfeld", [], [])
border_tower = Location("grenzturm", [], [])
customs_house = Location("zollhaus", [], [])
forest_castle = Location("waldfestung", [], [])
small_village = Location("kleines dorf", [], [])
starting_point = Location("deine huette", [], [])
spruce_forest = Location("fichtenwald", [], [])
devils_reef = Location("teufelsriff", [], [])
dark_forest = Location("dunkelwald", [], [])
diamond_mine = Location("diamantenmine", [], [])
death_canyon = Location("todesschlucht", [], [])
farm = Location("bauernhof", [], [])
forest_crossing = Location("waldkreuzung", [], [])
grassland = Location("grasfelder", [], [])
glade = Location("lichtung", [], [])
hills = Location("huegelland", [], [])
lost_forest = Location("verlorener wald", [], [])
lookout = Location("ausguck", [], [])
letol = Location("letol", [], [])
lumberjack = Location("holzfaeller", [], [])
misty_mountains = Location("nebelgebirge", [], [])
old_watchtower = Location("alter wachturm", [], [])
outback = Location("hinterland", [], [])
passage = Location("die passage", [], [])
quarry = Location("steinbruch", [], [])
river_mouth = Location("muendung", [], [])
ruined_city = Location("ruinenstadt", [], [])
scree_fields = Location("geroellfelder", [], [])
seagull_rock = Location("moewenfelsen", [], [])
sentry = Location("wachposten", [], [])
stone_cliffs = Location("steinklippen", [], [])
stormy_coast = Location("stuermige Küste", [], [])
source = Location("quelle", [], [])
towngate = Location("stadttor", [], [])
town_wall = Location("stadtmauer", [], [])
village_ruins = Location("dorfruinen", [], [])
volcano = Location("vulkan", [], [])
wasteland = Location("die oede", [], [])
waterfall = Location("wasserfall", [], [])
windmill = Location("muehle", [], [])
yerin = Location("yerin", [], [])
yto = Location("yto", [], [])

#Create Special Locations
old_pirate_island = Special_Location("alte pirateninsel", [], [])
port_of_atyr = Special_Location("hafen von atyr", [], [])
ferry = Special_Location("faehrhaeuschen1", [], [])
ferry2 = Special_Location("faehrhaeuschen2", [], [])






#Initialize attributes

abandoned_mines.initialize_location([Abandoned_Mine_Shaft(), Cave(), Mountain()], [ruined_city])
abandoned_palace.initialize_location([Abandoned_Palace(), Ruined_Tower(), Ruined_House()], [ruined_city])
atyr.initialize_location([Marketplace(), Church(), Small_Hut(), Half_Timbered_House(), Tavern(), Warehouse(), Wall(), Gate(), Tower()], [port_of_atyr,stone_cliffs, forest_crossing, yto])
aytol.initialize_location([Marketplace(), Small_Hut(), Half_Timbered_House()], [spruce_forest, lost_forest])

border_tower.initialize_location([Tower(), Scree(), Grass_Field()], [hills, grassland, scree_fields])
battlefield.initialize_location([Battlefield(), Wastelands(), Scree()], [town_wall, passage])

customs_house.initialize_location([Half_Timbered_House(), Garden(), River()], [yerin, ferry2, windmill])

dark_forest.initialize_location([Dark_Forest(), Forest(), Stump(), Fallen_Tree(), Rock(), Cave()], [lost_forest])
devils_reef.initialize_location([Reef(), Cliffs(), Beach()], [stormy_coast, lumberjack])
death_canyon.initialize_location([Mountain(), Canyon(), Rock()], [hills])
diamond_mine.initialize_location([Mine_Shaft(), Mountain(), Underground_Stream(), Abandoned_Mine_Shaft()], [lumberjack])

farm.initialize_location([Farm_House(), Farmland(), Grass_Field(), Pasture()], [yto, stormy_coast, hills])
ferry.initialize_location([River(), Small_Hut()], [ferry2, spruce_forest])
ferry2.initialize_location([Small_Hut(), River()], [ferry, customs_house])
forest_crossing.initialize_location([Forest(), Stump()], [atyr, yerin, seagull_rock])
forest_castle.initialize_location([Dungeon(), Fortress()], [yto, glade])

glade.initialize_location([Forest()], [forest_castle, old_watchtower, windmill])
grassland.initialize_location([Grass_Field()], [letol, passage, border_tower])

hills.initialize_location([Hill(), Grass_Field(), Forest(), Stream(), Pasture()], [farm, waterfall, death_canyon, border_tower])

lost_forest.initialize_location([Dark_Forest(), Forest(), Rock(), Fallen_Tree()], [aytol, dark_forest, source, lookout])
lookout.initialize_location([Forest(), Hill(), Grass_Field], [source, lost_forest, towngate])
letol.initialize_location([Marketplace(), Church(), Half_Timbered_House()], [windmill, grassland])
lumberjack.initialize_location([Forest()], [devils_reef, diamond_mine])

misty_mountains.initialize_location([Mountain(), Rock()], [wasteland])

old_pirate_island.initialize_location([Beach(), Forest()], [port_of_atyr])
old_watchtower.initialize_location([Ruined_Tower(), Forest()], [glade])
outback.initialize_location([Scree()], [quarry])

passage.initialize_location([Scree(), Rock()], [battlefield, grassland, quarry, village_ruins])
port_of_atyr.initialize_location([Beach(), Small_Hut(), Tavern()], [old_pirate_island, atyr, stone_cliffs])

quarry.initialize_location([Mine_Shaft(), Mountain()], [outback, passage])

river_mouth.initialize_location([River(), Beach(), Grass_Field()], [starting_point])
ruined_city.initialize_location([Ruined_Gate(), Ruined_House(), Ruined_Wall(), Ruined_Tower()], [towngate, abandoned_mines, abandoned_palace, town_wall])

scree_fields.initialize_location([Scree(), Wastelands(), Rock()], [village_ruins, volcano, wasteland, border_tower])
starting_point.initialize_location([Player_Hut(), Player_Garden()], [spruce_forest, small_village, river_mouth])
spruce_forest.initialize_location([Forest(), Stump(), Fallen_Tree(), Rock()], [ferry, starting_point, aytol])
small_village.initialize_location([Marketplace(),Small_Hut(), Half_Timbered_House(), Church()], [starting_point])
seagull_rock.initialize_location([Rock(), Cliffs(), Beach()], [stone_cliffs, forest_crossing])
sentry.initialize_location([Tower(), Forest()], [yerin])
stone_cliffs.initialize_location([Cliffs(), Rock(), Grass_Field(), Pasture()], [atyr, port_of_atyr, seagull_rock])
stormy_coast.initialize_location([Cliffs(), Rock(), Grass_Field()], [farm, devils_reef])
source.initialize_location([Stream(), Pond(), Mountain()], [lost_forest, lookout])

towngate.initialize_location([Ruined_Gate], [lookout, ruined_city])
town_wall.initialize_location([Ruined_Wall], [battlefield, ruined_city])

village_ruins.initialize_location([Ruined_House], [passage, scree_fields])
volcano.initialize_location([Lava_Field()], [scree_fields])

windmill.initialize_location([Windmill(), Grass_Field(), Farmland()], [glade, letol, customs_house])
waterfall.initialize_location([Pond(), Stream(), Forest(), Cave()], [hills])
wasteland.initialize_location([Wastelands(), Rock(), Scree()], [scree_fields, misty_mountains])

yerin.initialize_location([Marketplace(), Church(), Half_Timbered_House(), Small_Hut(), Tavern()], [customs_house, sentry, forest_crossing])
yto.initialize_location([Marketplace(), Small_Hut()], [atyr, forest_castle, farm])


if __name__ == "__main__":

    print("Bitte oeffne die Datei \"Spiel.py\"")
    time.sleep(10)

