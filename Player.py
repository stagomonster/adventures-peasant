import random
import pygame
from Utility import *

bandithp = random.randint(20, 50)
animalhp = random.randint(5, 20)
dragonhp = 100
goblinhp = random.randint(15, 30)
houndhp = random.randint(10,25)
bowmanhp = random.randint(10,20)

banditatk = random.randint(15, 25)
animalatk = random.randint(5, 10)
dragonatk = 50
goblinatk = random.randint(20, 30)
houndatk = random.randint(10, 20)
bowmanatk = random.randint(20, 30)

count = 0;


class Player:
    def __init__(self, window, status, opponent, inventory, name: str, level, gold, hp, max_hp, defense: Defense,
                 weapon: Weapon):
        self.win = window
        self.status = status
        self.opponent = opponent
        self.inventory = inventory
        self.name = name
        self.level = level
        self.gold = gold
        self.hp = hp
        self.max_hp = max_hp
        self.defense = defense
        self.weapon = weapon

    def displayChar(self):
        pygame.draw
        # sprite? maybe only have armor shown in inventory screen?

    def addWeapon(self, selected):
        if self.weapon.attack < selected.attack:
            self.weapon = selected

    def giveHP(self, value):
        self.hp += value
        if (self.hp > self.max_hp):
            self.hp = self.max_hp

    def openExploreMenu(self):
        if (self.status == 'normal'):
            return True
        if (self.status == 'combat'):
            return "in combat"
        if (self.status == 'witchhut'):
            return "in witchhut"

    def explore(self):
        global count
        x = random.randint(0, 8)
        scenario = "You can't explore right now!"
        if (self.weapon.attack >= 23 and self.defense.total >= 26):
            x = random.randint(0, 9)

        if (self.status == 'normal'):
            if(count >= 12):
                x=9
            if (x == 0):
                self.status = 'combat'
                if (self.weapon.attack >= 23 and self.defense.total >= 26):
                    count += 1
                if (self.gold >= 300):
                    flee = "You know you have enough money to pay them off, but do you really want to give money to " \
                           "these men? Will you keep your dignity and battle, or lose your valor and honor for life? " \
                           "Yes to keep your dignity :D, or No to feel the guilt of succumbing to fear for the rest of " \
                           "your life. D:"
                    self.status = 'bandit?'
                else:
                    self.opponent = 'bandit'
                    flee = " You pat your pockets and see that you don't have enough money. I guess you'll have to " \
                           "fight, or flee then. "
                    self.status = 'combat'
                scenario = "After walking for a while, you meet a group of bandits. They ask you to give them 300 " \
                           "gold, or else." + flee
            elif (x == 1):
                if (self.gold >= 50):
                    self.status = 'witchhut'
                    scenario = "You stumble upon a dwelling of some sort. It seems old and rickety, but you decide to " \
                               "check it out. After entering, the door swings shut behind you. You see an old woman " \
                               "smiling at you from behind a table. 'Welcome to my humble hut', she says, chuckling, " \
                               "'While you're here, why not buy some potions? I sell health potions, strength potions, " \
                               "and a mystery potion. Each for 50 gold. Whatta say?' Will you accept this offer? "
                    if (self.weapon.attack >= 23 and self.defense.total >= 26):
                        count += 1
                else:
                    self.explore()
            elif (x == 2):
                self.status = 'normal'
                scenario = "You've trudged along for a few hours. Nothing to show for it except some cuts and " \
                           "bruises. You feel a bit tired and weary. Perhaps some food would help? "
                self.hp -= 5
                if (self.weapon.attack >= 23 and self.defense.total >= 26):
                    count += 1
            elif (x == 3):
                self.status = 'normal'
                scenario = "You are walking around the forest, when suddenly a compass falls from the sky. You gaze " \
                           "up at the heavens and a loud voice booms, 'CHEESE AND MEAT FOR THE NOBLE KNIGHT!' You " \
                           "laugh in wonder as platters of meat fall from the sky. Then you wake up. In the middle of " \
                           "the forest. Sad and hungry :( "
                if (self.weapon.attack >= 23 and self.defense.total >= 26):
                    count += 1
            elif (x == 4):
                self.status = 'gold'
                scenario = "After walking around in a cave for a while, you get the bright idea to use your eyes to " \
                           "actually look for stuff. Wow! You see a pile of something glittering. Dare you touch it? "
                if (self.weapon.attack >= 23 and self.defense.total >= 26):
                    count += 1
            elif (x == 5):
                self.status = 'combat'
                self.opponent = 'goblin'
                scenario = "You continue walking for a while before seeing a big pile of sweet sweet gold. Before you " \
                           "reach it, a goblin jumps down from a tree, with a spear pointed at you. Do you fight him? " \
                           "Fight or Flee. "
                if (self.weapon.attack >= 23 and self.defense.total >= 26):
                    count += 1
            elif (x == 6):
                self.status = 'village'
                scenario = "You walk around the area. After some time, you see a small village in the distance. You " \
                           "arrive at it and some villagers come by. It seems that they want to trade with you. Click " \
                           "the ol' trade button to do just that. "
                if (self.weapon.attack >= 23 and self.defense.total >= 26):
                    count += 1
            elif (x == 7):
                self.status = 'combat'
                scenario = "You try to look for a town, but after walking for hours, you get lost in a forest. Some " \
                           "wild animals rush at you. What do you do now? "
                self.opponent = 'animal'
                if (self.weapon.attack >= 23 and self.defense.total >= 26):
                    count += 1
            elif (x == 8):
                self.status = 'village'
                scenario = "You start walking around and around in the forest until you're so exhausted and tired " \
                           "that you start seeing double. In fact, your eyesight is so poor that you're even seeing " \
                           "villages. Wait! That IS a village! You run towards it, making sure to remember to do the " \
                           "same thing the next time you need a village. "
                if (self.weapon.attack >= 23 and self.defense.total >= 26):
                    count += 1
            elif (x == 9):
                self.status = 'bossfight'
                self.opponent = 'dragon'
                scenario = "You stumble upon the lair of the great dragon. He breaths a breath of fire at you from " \
                           "upon his massive treasure hoard. Dare you fight him to end the tyranny of this dragon? " \
                           "Yes or No."
                count = 0

        elif self.status == 'village':
            self.status = 'normal'
            scenario = "You leave the villagers behind :(. They wave at you, and you disappear into the wilderness."
        elif self.status == 'witchhut' or self.status == 'gold' or self.status == 'accepttrade' or self.status == 'bandit':
            scenario = "Yes or No. Very simple. Not Yes or No or Explore, just Yes or No. >:( "

        return scenario

    def directAttack(self):
        global bandithp, animalhp, goblinhp, dragonhp, houndhp, bowmanhp
        global banditatk, animalatk, dragonatk, goblinatk, houndatk, bowmanatk

        enemy = None
        endmessage = ""
        attack = ""
        loot = ""
        gold = ""
        lootmsg = ""

        save = {}
        armor_prot = False

        if (self.status == 'village'):
            y = random.randint(0, 2)
            if (y == 0):
                result = "You really want to attack some innocent villagers?"
            elif (y == 1):
                result = "The poor villagers die by your hand... Just kidding. Don't attack them >:("
            elif (y == 2):
                result = "Attack these innocent villagers? Options: No or No"
            return result

        if(self.status == 'notyetdragon'):
            self.bossFight()

        if(self.status == 'combat'):
            if (self.opponent == 'bandit'):
                enemy = bandithp
                x = "bandithp"
                restorehp = random.randint(20, 50)

            elif (self.opponent == 'hound'):
                enemy = houndhp
                x = "houndhp"
                restorehp = random.randint(5,25)

            elif (self.opponent == 'animal'):
                enemy = animalhp
                x = "animalhp"
                restorehp = random.randint(5, 20)

            elif (self.opponent == 'bowman'):
                enemy = bowmanhp
                x = "bowmanhp"
                restorehp = random.randint(10,20)

            elif (self.opponent == 'goblin'):
                enemy = goblinhp
                x = "goblinhp"
                restorehp = random.randint(5, 30)
            elif (self.opponent == 'dragon'):
                enemy = dragonhp
                x = "dragonhp"
                restorehp = 300
            y = random.randint(round(0.5 * self.weapon.attack), self.weapon.attack + 5)
            if (y < self.weapon.attack):
                scenario = "You feel a bit sluggish, and only manage to deal " + str(y) + " damage to the " + \
                           self.opponent + ". "
            elif (y == self.weapon.attack):
                scenario = "You deal a solid " + str(y) + " to the " + self.opponent + ". "
            elif (y > self.weapon.attack):
                scenario = "Feeling strong, you deal " + str(y) + " damage to the " + self.opponent + ". "
            enemy -= y
            if (enemy <= 0):
                exec("%s = %d" % (x, restorehp))
                self.status = 'normal'
                goldchance = random.randint(1,3)
                lootchance = random.randint(1,10)
                type = random.randint(1,2)
                weapon = random.randint(1,300)

                if(weapon<50):
                    weapon = Utility.common_sword
                elif(weapon<100):
                    weapon = Utility.common_axe
                elif(weapon<150):
                    weapon = Utility.common_dagger
                elif(weapon<180):
                    weapon = Utility.rare_sword
                elif(weapon<210):
                    weapon = Utility.rare_axe
                elif(weapon<240):
                    weapon = Utility.rare_dagger
                elif(weapon<260):
                    weapon = Utility.epic_sword
                elif(weapon<280):
                    weapon = Utility.epic_axe
                elif(weapon<=300):
                    weapon = Utility.epic_dagger

                armor = random.randint(1,400)
                if(armor<50):
                    armor = Utility.common_helmet
                elif(armor<100):
                    armor = Utility.common_chestplate
                elif(armor<150):
                    armor = Utility.common_leggings
                elif(armor<200):
                    armor = Utility.common_boots
                elif(armor<230):
                    armor = Utility.rare_helmet
                elif(armor<260):
                    armor = Utility.rare_chestplate
                elif(armor<290):
                    armor = Utility.rare_leggings
                elif(armor<320):
                    armor = Utility.rare_boots
                elif(armor<340):
                    armor = Utility.epic_helmet
                elif(armor<360):
                    armor = Utility.epic_chestplate
                elif(armor<380):
                    armor = Utility.epic_leggings
                elif(armor<=400):
                    armor = Utility.epic_boots

                if lootchance == 1:
                    if type == 1:
                        self.addWeapon(weapon)
                        loot = " You also looted a "+weapon.getName()+"!"
                    elif type == 2:
                        self.defense.add(armor)
                        loot = " You also looted a "+armor.getName()+"!"

                if(goldchance==1):
                    self.gold += 50
                    gold = " Also, you stole a nice 50 gold! "
                if (self.opponent == 'animal'):
                    self.inventory.append('meat')
                elif(self.opponent=='goblin'):
                    self.gold += 200
                lootmsg = loot+gold
                endmessage = "With a final blow, you defeat the " + self.opponent + "."+lootmsg

                if(self.opponent == 'dragon'):
                    return True

            elif (self.opponent == 'bandit'):
                bandithp -= y
                damage = random.randint(banditatk - round(0.5 * banditatk), round(1.5 * banditatk))
                damage -= self.defense.total
                if(damage <= 0):
                    armor_prot = True
                    damage = 0
                self.hp -= damage

            elif (self.opponent ==  'hound'):
                houndhp -= y
                damage = random.randint(houndatk - round(0.5*houndatk), round(1.5*houndatk))
                damage -= self.defense.total
                if(damage <= 0):
                    armor_prot = True
                    damage = 0
                self.hp -= damage

            elif (self.opponent == 'animal'):
                animalhp -= y
                damage = random.randint(animalatk - round(0.5 * animalatk), round(1.5 * animalatk))
                damage -= self.defense.total
                if(damage <= 0):
                    armor_prot = True
                    damage = 0
                self.hp -= damage

            elif (self.opponent == 'bowman'):
                bowmanhp -= y
                damage = random.randint(bowmanatk - round(0.5 * bowmanatk), round(1.5 * bowmanatk))
                damage -= self.defense.total
                if(damage <= 0):
                    armor_prot = True
                    damage = 0
                self.hp -= damage

            elif (self.opponent == 'goblin'):
                goblinhp -= y
                damage = random.randint(goblinatk - round(0.5 * goblinatk), round(1.5 * goblinatk))
                damage -= self.defense.total
                if(damage <= 0):
                    armor_prot = True
                    damage = 0
                self.hp -= damage

            elif (self.opponent == 'dragon'):
                dragonhp -= y
                damage = random.randint(dragonatk - round(0.5 * dragonatk), round(1.5 * dragonatk))
                damage -= self.defense.total
                if(damage <= 0):
                    armor_prot = True
                    damage = 0
                self.hp -= damage

            else:
                return "Error"
            if (enemy > 0):
                if(armor_prot == True):
                    defended = " But your armor is so epic it just blocks the attack damage :O"
                    damage = ""
                    attack = "They return a hit!"+defended
                else:
                    defended = ""
                    attack = "They return a hit of " + str(damage) + "!"+defended
            result = str(scenario + attack + endmessage)
            return result
        elif self.status == 'normal':
            return "Dude, chill. Who are you gonna whack, a tree?"
        else:
            return "I know you want to show off your fighting skills, but you can't attack right now."

    def flee(self):
        x = random.randint(0, 10)
        if (self.status == 'combat'):
            chance = random.randint(0, 3)
            armor = ""
            if (chance == 0):
                result = "You flee successfully!"
                self.status = 'normal'
            elif (chance == 1):
                result = "You run to a distance and escape them, but your stamina is low, and you feel real tired. (-5 HP)"
                self.status = 'normal'
                self.hp -= 5
            elif (chance == 2 or chance == 3):
                result = "You try to flee, but you're too slow. They hit you from behind!"
                damage = 10
                damage -= self.defense.total
                if(damage<= 0):
                    damage = 0
                    armor = " Luckily enough, your armor is strong and it blocks all damage :D"
                self.hp -= damage
                self.status = 'combat'
            return result+armor
        elif (self.status == 'village'):
            result = "The villagers seem bewildered by your quick escape, then shrug."
            self.status = 'normal'
            return result
        elif (self.status == 'notyetdragon'):
            result = "Smart choice. Or was it?"
            return result
        else:
            result = "What are you fleeing from? My incredible glory? I know man, its hard to bear a narrator being " \
                     "so stunning. "
            return result

    def trade(self):
        if (self.status == 'normal'):
            result = "You aren't at a village!"
        elif (self.status == 'village'):
            low = random.randint(1, 6)
            middle = random.randint(1, 6)
            high = random.randint(1, 6)
            if (self.gold >= 1000):
                if (high <= 2):
                    self.status = 'accepttrade'
                    self.opponent = 'h1'
                    result = "They are willing to offer a Epic weapon for 1000 gold. Do you wish to accept? Yes or " \
                             "No. "
                elif (high <= 5):
                    self.status = 'accepttrade'
                    self.opponent = 'h2'
                    result = "They are willing to offer a random Epic armor for 1000 gold. Do you wish to accept? Yes " \
                             "or No. "
                elif (high == 6):
                    self.status = 'accepttrade'
                    self.opponent = 'h3'
                    result = "They are willing to offer some a feast fit for kings for 1000 gold. Do you wish to " \
                             "accept? Yes or No. "
            elif (self.gold >= 500):
                if (middle <= 2):
                    self.status = 'accepttrade'
                    self.opponent = 'm1'
                    result = "They are willing to offer a Rare weapon for 500 gold. Do you wish to accept? Yes or " \
                             "No. "
                elif (middle <= 5):
                    self.status = 'accepttrade'
                    self.opponent = 'm2'
                    result = "They are willing to offer a random Rare armor for 500 gold. Do you wish to accept? Yes " \
                             "or No. "
                elif (middle == 6):
                    self.status = 'accepttrade'
                    self.opponent = 'm3'
                    result = "They are willing to offer some nice meats for 500 gold. Do you wish to accept? Yes or " \
                             "No. "
            elif (self.gold >= 50):
                if low <= 2:
                    self.status = 'accepttrade'
                    self.opponent = 'l1'
                    result = "They are willing to offer a Common weapon for 50 gold. Do you wish to accept? Yes or " \
                             "No. "
                elif (low <= 5):
                    self.status = 'accepttrade'
                    self.opponent = 'l2'
                    result = "They are willing to offer a random Common armor for 50 gold. Do you wish to accept? Yes " \
                             "or No. "
                elif (low == 6):
                    self.status = 'accepttrade'
                    self.opponent = 'l3'
                    result = "They are willing to offer some food for 50 gold. Do you wish to accept? Yes or No. "
            else:
                result = "You don't have enough gold! But its alright :) The villagers give a small gift of meat! :) " \
                         "Such kind villagers. "
                self.inventory.append('meat')
                self.status = 'normal'
        elif self.status == 'combat':
            result = "Mate, you're fighting, not the time to be showing off your dough right now."
        elif self.status == 'witchhut':
            result = "Yes or No. Not ooooooo lookie here at this trade button, there's totally not a YES and NO button."

        else:
            result = "You can't trade right now!"

        return result

    def yes(self):
        if (self.status == 'accepttrade'):
            if (self.opponent == 'h1'):
                weapon = random.randint(1, 3)
                selected = None
                if (weapon == 1):
                    selected = Utility.epic_sword
                elif (weapon == 2):
                    selected = Utility.epic_axe
                elif (weapon == 3):
                    selected = Utility.epic_dagger
                self.opponent = None
                self.status = 'normal'
                self.gold -= 1000
                self.addWeapon(selected)
                scenario = "You give up your 1000 gold, and gasp at the awesome new "+selected.getName()+" you just " \
                                                                                                         "got. Pretty" \
                                                                                                         " epic. " \
                                                                                                         "Didja see " \
                                                                                                         "what I did " \
                                                                                                         "there? " \
                                                                                                         "Didja see " \
                                                                                                         "that? "


            if (self.opponent == 'h2'):
                armor = random.randint(1, 4)
                selected = ''
                if (armor == 1):
                    selected = Utility.epic_helmet

                elif (armor == 2):
                    selected = Utility.epic_chestplate

                elif (armor == 3):
                    selected = Utility.epic_leggings

                elif (armor == 4):
                    selected = Utility.epic_boots

                self.opponent = None
                self.status = 'normal'
                self.gold -= 1000
                self.defense.add(selected)

                scenario = "You hand over the gold, and look over your new " + selected.getName() + "! Woah, this is " \
                                                                                                    "top tier gear " \
                                                                                                    "mate! That was " \
                                                                                                    "some gold worth " \
                                                                                                    "spent. "
            if (self.opponent == 'h3'):
                self.opponent = None
                self.status = 'normal'
                self.gold -= 1000
                self.inventory.append('meat')
                self.inventory.append('meat')
                self.inventory.append('meat')
                self.inventory.append('meat')
                self.inventory.append('meat')
                self.inventory.append('meat')
                self.inventory.append('meat')
                self.inventory.append('meat')
                self.inventory.append('meat')
                self.inventory.append('meat')
                self.inventory.append('meat')
                self.inventory.append('meat')
                self.inventory.append('meat')
                self.inventory.append('meat')
                self.inventory.append('meat')
                scenario = "You give the bag ol gold to the villagers, and look inside the bag they give to you. " \
                           "15 MEATS?!?!?!?!?! THIS IS ENOUGH TO FEED YOU FOR... oh wait, about 1 day. "

            if (self.opponent == 'm1'):
                weapon = random.randint(1, 3)
                selected = None
                if (weapon == 1):
                    selected = Utility.rare_sword
                elif (weapon == 2):
                    selected = Utility.rare_axe
                elif (weapon == 3):
                    selected = Utility.rare_dagger

                self.opponent = None
                self.status = 'normal'
                self.gold -= 500
                self.addWeapon(selected)
                scenario = "You spend that 500 gold, and recieve a nice "+selected.getName()+". Pretty nice, " \
                                                                                             "actually. Not bad for " \
                                                                                             "500 gold. Not saying " \
                                                                                             "its good, but like, " \
                                                                                             "you know, its good. "

            if (self.opponent == 'm2'):
                armor = random.randint(1, 4)
                selected = ''
                if (armor == 1):
                    selected = Utility.rare_helmet

                elif (armor == 2):
                    selected = Utility.rare_chestplate

                elif (armor == 3):
                    selected = Utility.rare_leggings

                elif (armor == 4):
                    selected = Utility.rare_boots

                self.opponent = None
                self.status = 'normal'
                self.gold -= 500
                self.defense.add(selected)

                scenario = "You hand over the gold, and look over your new " + selected.getName() + "! Decent. I " \
                                                                                                    "mean, " \
                                                                                                    "at least it " \
                                                                                                    "don't have any " \
                                                                                                    "holes. That's an " \
                                                                                                    "A in my book. "
            if (self.opponent == 'm3'):
                self.opponent = None
                self.status = 'normal'
                self.gold -= 500
                self.inventory.append('meat')
                self.inventory.append('meat')
                self.inventory.append('meat')
                self.inventory.append('meat')
                self.inventory.append('meat')
                scenario = "You give the bag ol gold to the villagers, and look inside the bag they give to you. " \
                           "Woah, 5 meats! "

            if (self.opponent == 'l1'):
                weapon = random.randint(1, 3)
                selected = None
                if (weapon == 1):
                    selected = Utility.common_sword
                elif (weapon == 2):
                    selected = Utility.common_axe
                elif (weapon == 3):
                    selected = Utility.common_dagger
                self.opponent = None
                self.status = 'normal'
                self.gold -= 50
                self.addWeapon(selected)

                scenario = "Handing over the gold, you inspect your new weapon! The " + selected.getName() + " looks " \
                                                                                                                     "like a piece of sh- woah, not bad. I mean, its not awful. You should be glad you have a " \
                                                                                                                     "weapon at all, to think about it. "
            if (self.opponent == 'l2'):
                armor = random.randint(1, 4)
                selected = ''
                if (armor == 1):
                    selected = Utility.common_helmet

                elif (armor == 2):
                    selected = Utility.common_chestplate

                elif (armor == 3):
                    selected = Utility.common_leggings

                elif (armor == 4):
                    selected = Utility.common_boots

                self.opponent = None
                self.status = 'normal'
                self.gold -= 50
                self.defense.add(selected)

                scenario = "You hand over the gold, and look over your new " + selected.getName() + "! Wow so many holes! Oh " \
                                                                                                            "wait, that's bad. Too late! "
            if (self.opponent == 'l3'):
                self.opponent = None
                self.status = 'normal'
                self.gold -= 50
                self.inventory.append('meat')
                self.inventory.append('meat')
                scenario = "You give the gold to the villagers, and recieve a nice basket of meat. This will keep you " \
                           "full for yea- Wait, its just two pieces of meat?? Oh well, guess you'll just have to live" \
                           " on that. "

        elif (self.status == 'witchhut'):
            potion = random.randint(1, 3)
            if potion == 1:
                string = "dark red, almost as if it was blood."
                self.inventory.append('health_pot')
            elif (potion == 2):
                string = "some sort of green liquid. You shake the bottle, and it doesn't even move."
                self.inventory.append('strength_pot')
            elif (potion == 3):
                string = "a starry grey, twinkling with mystery."
                self.inventory.append('mystery_pot')
            scenario = "'Alrighty', the woman says, 'Oh, did I forget to mention? You don't get to choose which " \
                       "potion you receive.' Chuckling to herself, she hands you a potion. " + "It is " + string + " Whatever. You put it into your backpack and leave the crazy woman alone. "
            self.gold -= 50
            self.status = 'normal'
        elif (self.status == 'gold'):
            attack = random.randint(1, 3)
            if (attack == 1):
                scenario = "An arrow snipes you from across the cave. You turn around, and a bowman look right back, " \
                           "smiling mercilessly. "
                self.status = 'combat'
                self.opponent = 'bowman'
            else:
                scenario = "You cautiously walk forward, and dumb the shiny stuff into your backpack. You just got " \
                           "+100 gold, congrats :) "
                self.status = 'normal'
                self.gold += 100
        elif(self.status == 'bossfight'):
            scenario = "You walk toward the dragon, and towards your (probable) demise. If you win, you gain lots of " \
                       "glory and prestige. If you lose... gg mate "
            self.status = 'combat'
            self.opponent = 'dragon'
        elif(self.status == 'bandit?'):
            scenario = "You accept the challenge and walk up to fight with those rascals."
            self.status = 'combat'
            self.opponent = 'bandit'
        else:
            scenario = "What are you saying yes to, dummy?"

        return scenario

    def no(self):
        if (self.status == 'accepttrade'):
            self.status = 'normal'
            result = "The villagers back away, sad :( You leave the village in search of... I don't even know, " \
                     "why would you leave the village? Those poor poor villagers :(. "
        elif (self.status == 'witchhut'):
            self.status = 'normal'
            result = "She looks at you, surprised you would say no to her. She throws her hand toward you, " \
                     "and suddenly this ray of light smacks you right out of the house, out of the door, and into the" \
                     " woods. You stand up, seemingly unharmed, but rather dizzy, with no idea of your whereabouts."
        elif (self.status == 'combat'):
            result = "I'm sorry, but denial is not the way to avoid fighting."

        elif(self.status == 'gold'):
            result = "Sadly, you walk away from the cool shiny stuff, and return to the boring old forest :("
            self.status = 'normal'

        elif(self.status == 'bossfight'):
            result = "Ah, someone with intelligence. Congrats large brain, you just potentially saved your life. Or " \
                     "lost your chance for glory. Meh, whatever, you might find the dragon again sometime. "
            self.status = 'normal'

        elif(self.status == 'bandit?'):
            result = "You give up your gold, honor, and sense of self worth. "
            self.gold -= 300
            self.status = 'normal'
        else:
            result = "??? What are you saying no to? "
        return result

    def bossFight(self):
        result = "You still have time to leave before the dragon completely destroys you. Yes to proceed and almost " \
                 "certainly die, No to be an intellectual and stay alive. "
        self.status = 'bossfight'
        return result

    def use(self, item):
        if item in self.inventory:
            if (self.status == 'combat'):
                result = "You are in combat! You can't use an item right now!"
            if (item == 'meat'):
                bonus = "You gain +5 health!"
                self.inventory.remove('meat')
                if (self.hp == self.max_hp):
                    result = "You are at max health! No need to eat right now."
                    self.inventory.append('meat')
                elif (self.status == 'village'):
                    result = "You calmly eat the meat in front of the villagers. They look away in disg- they look " \
                             "away from the glory of your chewing mouth. " + bonus
                    self.giveHP(5)

                elif (self.status == 'normal'):
                    result = "The meat is pretty tough on your teeth. Suddenly you hear a cracking sound from your " \
                             "mouth. With horror you feel your teeth, looking for the one that cracked. It takes a " \
                             "minute or two, but then you realize that you still have all your teeth. It was just a " \
                             "bone. Man, you really do have an overactive imagination, huh. Anyways, you gain +5 " \
                             "health! "
                    self.giveHP(5)
                elif (self.status == 'dragon'):
                    result = "What are you, crazy?! The moment you take pull out that meat is the moment you get " \
                             "obliterated out of existence. "
            elif item == 'mystery_pot':
                effect = random.randint(1, 5)
                self.inventory.remove('mystery_pot')
                if effect == 1:
                    self.max_hp += 10
                    self.hp += 10
                    result = "You gain +10 Max Hp :O!!"
                elif effect == 2 or effect == 3:
                    self.hp -= 10
                    result = "You get smacked in the face by a magic hand and lose 10 hp :(."
                elif effect == 4:
                    self.gold += 100
                    result = "Out of thin air, a floating gold rock appears! You quickly grab it out of the air. " \
                             "Congrats! You just got +100 gold! "
                elif effect == 5:
                    self.status = 'combat'
                    self.opponent = 'hound'
                    result = "A pack of magical hounds POOF in front of you. They snarl at you. They look pretty " \
                             "terrifying, with those big teeth, and sharp eyes. Dare you fight them? "
            elif item == 'strength_pot':
                self.inventory.remove('strength_pot')
                self.weapon.attack += 10
                result = "After drinking the potion, you feel stronger! You just got +10 atk!!"

            elif item == 'health_pot':
                self.inventory.remove('health_pot')
                self.giveHP(10)
                result = "You quickly chug the reddish liquid, and feel invigorated! [+10hp]"
            else:
                result = "You can't use that right now!"
        else:
            result = "You don't have that item in your inventory!"

        return result

    def returnInventory(self):
        return str(self.inventory)

    # def equip_weapon(self, weapon):
    #     if self.weapon != None:
    #         self.unequip_weapon()
    #     self.weapon = weapon
    #     self.attack += weapon.attack
    #
    # def unequip_weapon(self):
    #     if self.weapon != None:
    #         self.attack -= self.weapon.attack
    #         self.weapon = None
    #
    # def equip_armor(self, armor, slot):
    #     if self.armor[slot] != None:
    #         self.unequip_armor(slot)
    #     self.armor[slot] = armor
    #     self.defense += armor.defense
    #
    # def unequip_armor(self, slot):
    #     if self.armor[slot] is not None:
    #         self.defense -= self.armor[slot].defense
    #         self.armor[slot] = None
