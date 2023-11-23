class Abiliti :
    def __init__(self , type , dmg ,isAoe) -> None:
        self.type = type
        self.dmg = dmg
        self.isAoe = isAoe
        


class RPGCharacter:
    def __init__(self, name, character_class, level, weapon, abilities, strength, agility, intelligence, toughness, race):
        self.name = name
        self.character_class = character_class
        self.level = level
        self.weapon = weapon
        self.abilities = abilities
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.toughness = toughness
        self.race = race

    def __str__(self):
        return f"{self.name} - {self.character_class} (Level {self.level}) with {self.weapon}, Abilities: {self.abilities}, " \
                f"Strength: {self.strength}, Agility: {self.agility}, Intelligence: {self.intelligence}, " \
                f"Toughness: {self.toughness}, Race: {self.race}"

class RPGCharacterBuilder:
    def __init__(self, ):
        self.character = RPGCharacter("", "", 1, "", [], 25,25,25,25, "")

    def set_character_class(self, character_class):
        self.character.character_class = character_class
        return self

    def set_level(self, level):
        self.character.level = level
        return self

    def set_weapon(self, weapon):
        self.character.weapon = weapon
        return self

    def set_abilities(self, abilities):
        self.character.abilities = abilities
        return self

    def set_strength(self, strength):
        self.character.strength = strength
        return self

    def set_agility(self, agility):
        self.character.agility = agility
        return self

    def set_intelligence(self, intelligence):
        self.character.intelligence = intelligence
        return self

    def set_toughness(self, toughness):
        self.character.toughness = toughness
        return self

    def set_race(self, race):
        self.character.race = race
        return self

    def build(self):
        return self.character


class RPGCharacterDirector:
    
    def __init__(self) -> None:
        self.characterBuilder = RPGCharacterBuilder()
    
    def setStats(self ,level, agility , inteligence , strength , toughness) :
        if level *3 + 100 < agility +inteligence + strength + toughness :
            return False
        return True
    
    def construct_warrior(self):
        self.characterBuilder.set_character_class("Warrior").set_weapon("Sword") \
        .set_abilities([Abiliti("physical" , 10 , False) , Abiliti("physical" , 5,True)])\
        
        
    def construct_mage(self ):
        self.characterBuilder.set_character_class("mage").set_weapon("road") \
        .set_abilities([Abiliti("fire" , 10 , False) , Abiliti("water" , 5,True)]) \
        
        
    def construct_rouge(self ):
        self.characterBuilder.set_character_class("rouge").set_weapon("knife") \
        .set_abilities([Abiliti("physical" , 20 , False) , Abiliti("physical" , 4,True)]) \
        
        
    def construct_hunter(self ):
        self.characterBuilder.set_character_class("hunter").set_weapon("bow") \
        .set_abilities([Abiliti("physical" , 10 , False) , Abiliti("fire" , 15,False)]) \
        
    def build(self):
        return self.characterBuilder.build()



dir = RPGCharacterDirector()    
act = input("""Weclome to character builder
        the first stem is to choose class of your character
        1 - warior
        2 - mage 
        3 - rouge
        4 - hunter 
    """)
if act == "1" :
    dir.construct_warrior()
elif act =="2" :
    dir.construct_mage()
elif act =="3" :
    dir.construct_rouge()
elif act =="4" :
    dir.construct_hunter()
act =input("now enter race: ")
dir.characterBuilder.set_race(act)

while(True):
    act = input("""now the finall steps enter in this order
                level , agitlity , strength , touhness
                the combined amount of statts should be equal 100 + 3*level
            """)    
    stats = act.split(",")
    lvl = stats[0].strip()
    lvl = int(lvl)

    agility = int(stats[1].strip())

    inteligence = int(stats[2].strip())
    
    strength = int(stats[3].strip())

    toughness = int(stats[4].strip())
    
    if dir.setStats(lvl , agility , inteligence, strength , toughness) :
        break
    
res = dir.build()
print(res)