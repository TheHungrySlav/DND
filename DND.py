# Dungeons and Dragons

def DND():
    # Libraries
    import random
    import Weapons
    from DND_dice import dice

    # Character Creation
    class Character:
        def __init__(self,name,char_class,race,background,proficiency,AC,initiative,speed,HPmax,strength,dexterity,constitution,intelligence,wisdom,charisma):
            self.name = name
            self.char_class = char_class
            self.race = race
            self.background = background
            self.proficiency = proficiency
            self.AC = AC
            self.initiative = initiative
            self.speed = speed
            self.HPmax = HPmax
            self.strength = strength
            self.dexterity = dexterity
            self.constitution = constitution
            self.intelligence = intelligence
            self.wisdom = wisdom
            self.charisma = charisma

    user = Character(' ',' ',' ',0,0,0,0,0,0,0,0,0,0,0,0) # There has to be a better way lol
    user.name = input('Youre finally awake traveler, What is your name?: ')
    user.race = input('What is your race?: ')
    user.background = input('What is your background?: ')
    user.char_class = input('What is your class?: ')
    
    print('Welcome ',user.name,'to the world of [insert]! Adventure Awaits!')

    #Kyle = Character('Dick Zepplin','human','soldier',2,11,2,30,13,18,14,16,14,10,10)
    

    # Character class
    class Character_class:
        def __init__(self,char_class):
            self.char_class = char_class

    class money:
        def __init__(self,copper,silver,gold,platinum):
            self.copper = copper
            self.silver = silver
            self.gold = gold
            self.platinum = platinum

    # Need help with inventory system, maybe a dictionary?
    # inventory = {'weapons':Weapons.battleaxe,'copper':money.copper,'silver':money.silver,'gold':money.gold,'platinum':money.platinum}

    # Battle Mechanics Demo
    '''
    print('Youve been ambushed! Roll for initiative')
    modifier = 2
    initiative = dice('D20') + modifier
    if initiative >= 10:
        print('You attack first!:')
        print(' ')
        damage = dice(Weapons.battleaxe.dice)
        print('You do ',damage,Weapons.battleaxe.damage_type,' damage!')
    elif initiative < 10:
        print('The enemy attacks first!:')
        print(' ')
        damage = dice(Weapons.dagger.dice)
        print('The enemy inflicts ',damage,Weapons.dagger.damage_type,' damage!')
    '''


DND()