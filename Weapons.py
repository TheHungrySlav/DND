class Weapons:
    def __init__(self,cost_num,money_type,damage_type,weight,dice):
        self.cost = cost_num
        self.money_type = money_type
        self.damage_type = damage_type
        self.weight = weight
        self.dice = dice


# Weapons List
club = Weapons(1,'sp','bludgeoning',2,'D4')
dagger = Weapons(2,'gp','piercing',1,'D4')
greatclub = Weapons(2,'gp','bludgeoning',10,'D8')
handaxe = Weapons(5,'gp','slashing',2,'D6')
javelin = Weapons(5,'sp','piercing',2,'D6')
light_hammer = Weapons(2,'gp','bludgeoning',2,'D4')
mace = Weapons(5,'gp','bludgeoning',4,'D6')
quarterstaff = Weapons(2,'sp','bludgeoning',4,'D6')
sickle = Weapons(1,'gp','slashing',2,'D4')
spear = Weapons(1,'gp','piercing',3,'D6')
crossbow_light = Weapons(25,'gp','piercing',5,'D8')
dart = Weapons(5,'cp','piercing',0.25,'D4')
shortbow = Weapons(25,'gp','piercing',2,'D6')
sling = Weapons(1,'sp','bludgeoning',0,'D4')
battleaxe = Weapons(10,'gp','slashing',4,'D8')
flail = Weapons(10,'gp','bludgeoning',2,'D8')
glaive = Weapons(20,'gp','slashing',6,'D10')
greataxe = Weapons(30,'gp','slashing',7,'D12')
greatsword = Weapons(50,'gp','slashing',6,'D6')
halberd = Weapons(20,'gp','slashing',6,'D10')
lance = Weapons(10,'gp','piercing',6,'D12')
longsword = Weapons(15,'gp','slashing',3,'D8')
maul = Weapons(10,'gp','bludgeoning',10,'D6')
morningstar = Weapons(15,'gp','piercing',4,'D8')
pike = Weapons(5,'gp','piercing',2,'D8') 
rapier = Weapons(25,'gp','piercing',2,'D8')
scimitar = Weapons(25,'gp','slashing',3,'D6')
shortsword = Weapons(10,'gp','piercing',2,'D6')
trident = Weapons(5,'gp','piercing',4,'D6')
war_pick = Weapons(5,'gp','piercing',2,'D8')
warhammer = Weapons(15,'gp','bludgeoning',2,'D8')
whip = Weapons(2,'gp','slashing',3,'D4')
# blowgun = Weapons(10,'gp','piercing',1,)
crossbow_hand = Weapons(75,'gp','piercing',3,'D6')
crossbow_heavy = Weapons(50,'gp','piercing',18,'D10')
longbow = Weapons(50,'gp','piercing',2,'D8')
# net = Weapons(1,'gp',' ',3)