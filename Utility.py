#####################################################
#  CLASS FOR ALL PLAYER UTILITY ATTRIBUTES
#  WEAPON, ARMOR, DEFENSE, UTILITY )
#####################################################
'''
LEGENDARY
- SWORD = ???
- AXE = ???
- DAGGER = ???
EPIC
- SWORD = 25
- AXE = 30
- DAGGER = 23
RARE 
- SWORD = 15
- AXE = 18
- DAGGER = 12
COMMON
- SWORD = 10
- AXE = 12
- DAGGER = 9
'''
#####################################################
class Weapon:
    def __init__(self, attack, rarity, type):
        self.attack = attack
        self.rarity = rarity
        self.type = type

    def getName(self):
        return self.rarity + " " + self.type


#####################################################

class Armor:
    def __init__(self, points, rarity, type):
        self.points = points
        self.rarity = rarity
        self.type = type

    def getName(self):
        return self.rarity + " " + self.type


#####################################################

class Defense:
    def __init__(self, helmet: Armor = None, chestplate: Armor = None, leggings: Armor = None, boots: Armor = None,
                 color=None):
        self.helmet = helmet
        self.chestplate = chestplate
        self.leggings = leggings
        self.boots = boots
        self.color = color
        self.total = self.calcDefense()

    def calcDefense(self):
        points = 0
        if (self.helmet != None):
            points += self.helmet.points
        if (self.chestplate != None):
            points += self.chestplate.points
        if (self.leggings != None):
            points += self.leggings.points
        if (self.boots != None):
            points += self.boots.points

        return points

    def add(self, selected: Armor):
        if selected.type == 'helmet':
            if self.helmet == None:
                self.helmet = selected
            elif self.helmet.points < selected.points:
                self.helmet = selected
        if selected.type == 'chestplate':
            if self.chestplate == None:
                self.chestplate = selected
            if self.chestplate.points < selected.points:
                self.chestplate = selected
        if selected.type == 'leggings':
            if self.leggings == None:
                self.leggings = selected
            if self.leggings.points < selected.points:
                self.leggings = selected
        if selected.type == 'boots':
            if self.boots == None:
                self.boots = selected
            if self.boots.points < selected.points:
                self.boots = selected
        self.total = self.calcDefense()

#####################################################

class Utility:
    ''' STATIC WEAPONS '''
    hand = Weapon(5, 'default', 'hand')

    common_sword = Weapon(10, 'common', 'sword')
    common_axe = Weapon(12, 'common', 'axe')
    common_dagger = Weapon(9, 'common', 'dagger')

    rare_sword = Weapon(15, 'rare', 'sword')
    rare_axe = Weapon(18, 'rare', 'axe')
    rare_dagger = Weapon(12, 'rare', 'dagger')

    epic_sword = Weapon(25, 'epic', 'sword')
    epic_axe = Weapon(30, 'epic', 'axe')
    epic_dagger = Weapon(23, 'epic', 'dagger')

    legendary_sword = Weapon(32, 'legendary', 'sword')
    legendary_axe = Weapon(40, 'legendary', 'axe')
    legendary_dagger = Weapon(38, 'legendary', 'dagger')

    ''' STATIC DEFENSE ARMOR PIECES '''
    common_helmet = Armor(5, 'common', 'helmet')
    common_chestplate = Armor(10, 'common', 'chestplate')
    common_leggings = Armor(9, 'common', 'leggings')
    common_boots = Armor(7, 'common', 'boots')

    rare_helmet = Armor(8, 'rare', 'helmet')
    rare_chestplate = Armor(15, 'rare', 'chestplate')
    rare_leggings = Armor(13, 'rare', 'leggings')
    rare_boots = Armor(10, 'rare', 'boots')

    epic_helmet = Armor(12, 'epic', 'helmet')
    epic_chestplate = Armor(23, 'epic', 'chestplate')
    epic_leggings = Armor(20, 'epic', 'leggings')
    epic_boots = Armor(15, 'epic', 'boots')

    legendary_helmet = Armor(15, 'legendary', 'helmet')
    legendary_chestplate = Armor(27, 'legendary', 'chestplate')
    legendary_leggings = Armor(24, 'legendary', 'leggings')
    legendary_boots = Armor(18, 'legendary', 'boots')
