import pygame
import random
import math
import colorsys
from Player import *

pygame.init()

running = True
SCREENWIDTH = 1200
SCREENHEIGHT = 675
win = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption("The Adventures of a Peasant")
clock = pygame.time.Clock()

# MUSIC INFO - THE WALLS OF EBONHAWKE, A LAND RESTORED, LOGANS JOURNEY, THE TENGU WALL, TYRIA REBORN,
# DAWN IN SHAEMOOR, OUT OF THE DREAM, HERITAGE OF HUMANITY, THE SEA OF SORROWS
pygame.mixer.music.load("music_playlist.wav")
musicIsPaused = False

# COLORS
red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (230, 230, 0)
lightblue = (20, 20, 255)
green = (0, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)
beige = (207, 185, 151)
button_grey = (241, 241, 241)
button_hovergrey = (215, 215, 215)
orange = (255, 165, 0)
darkorange = (235, 145, 0)
darkgrey = (100, 100, 100)

# Armor Types
# farmer/peasant/nothing, leather, chainmail, heavy iron, ???
# each will have its own durabilities/points(?) and armor worth

# Swords/Weapons

player_name = "peasant"
max_health = 100
armor = ['None', 'None', 'None', 'None']
difficulty = 2
# 1 = ez, 2 = normal 3 = hard 4(?) = impossible

nameCreated = False
gameRunning = False


def pause():
    global musicIsPaused
    pygame.mixer.music.pause()
    musicIsPaused = True


def unpause():
    global musicIsPaused
    pygame.mixer.music.unpause()
    musicIsPaused = False



def switchBattle():
    global musicIsPaused
    if (musicIsPaused):
        pygame.mixer.music.unpause()
    pygame.mixer.music.stop()
    pygame.mixer.music.load("battle.wav")
    pygame.mixer.music.play(-1)
    musicIsPaused = False


def switchAmbient():
    global musicIsPaused
    if (musicIsPaused):
        pygame.mixer.music.unpause()
    pygame.mixer.music.stop()
    pygame.mixer.music.load("music_playlist.wav")
    pygame.mixer.music.play(-1)
    musicIsPaused = False


class Menu:
    def __init__(self, window):
        pass

    def blit_text(self, surface, rect, text, pos, font, color=pygame.Color('black')):
        words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
        space = font.size(' ')[0]  # The width of a space.
        max_width, max_height = surface.get_size()
        x, y = pos
        for line in words:
            for word in line:
                word_surface = font.render(word, 0, color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = pos[0]
                    y += word_height
                    rect.height += word_height
                surface.blit(word_surface, (x, y))
                x += word_width + space
            x = pos[0]
            y += word_height

    def mainMenu(self):
        global gameRunning
        menu = True

        outline_factor = 5
        outline_color = (255, 215, 0)
        button_start_x = 450
        button_start_y = 275
        button_start_width = 300
        button_start_height = 70
        button_start = pygame.Rect(button_start_x, button_start_y, button_start_width, button_start_height)
        button_start_outline = pygame.Rect(button_start_x - outline_factor, button_start_y - outline_factor,
                                           button_start_width + 2 * outline_factor,
                                           button_start_height + 2 * outline_factor)

        button_options_x = 450
        button_options_y = 375
        button_options_width = 300
        button_options_height = 70
        button_options = pygame.Rect(button_options_x, button_options_y, button_options_width, button_options_height)
        button_options_outline = pygame.Rect(button_options_x - outline_factor, button_options_y - outline_factor,
                                             button_options_width + 2 * outline_factor,
                                             button_options_height + 2 * outline_factor)

        button_title_x = 450
        button_title_y = 475
        button_title_width = 300
        button_title_height = 70
        button_title = pygame.Rect(button_title_x, button_title_y, button_title_width, button_title_height)
        button_title_outline = pygame.Rect(button_title_x - outline_factor, button_title_y - outline_factor,
                                           button_title_width + 2 * outline_factor,
                                           button_title_height + 2 * outline_factor)

        button_exit_x = 450
        button_exit_y = 575
        button_exit_width = 300
        button_exit_height = 70
        button_exit = pygame.Rect(button_exit_x, button_exit_y, button_exit_width, button_exit_height)
        button_exit_outline = pygame.Rect(button_exit_x - outline_factor, button_exit_y - outline_factor,
                                          button_exit_width + 2 * outline_factor,
                                          button_exit_height + 2 * outline_factor)

        text_font = pygame.font.SysFont('Comic Sans MS', 40)
        title_font = pygame.font.SysFont('Comic Sans MS', 70)

        # text_largetitle = title_font.render('The Adventures of A Peasant', True, black)
        text_start = text_font.render('Start Game', True, black)
        text_options = text_font.render('Options', True, black)
        text_title = text_font.render('Credits', True, black)
        text_exit = text_font.render('Quit', True, black)

        # text_largetitle_rect = text_largetitle.get_rect(center=(round(SCREENWIDTH / 2), 100))
        text_start_rect = text_start.get_rect(center=button_start.center)
        text_options_rect = text_options.get_rect(center=button_options.center)
        text_title_rect = text_title.get_rect(center=button_title.center)
        text_exit_rect = text_exit.get_rect(center=button_exit.center)

        backgroundImg = pygame.image.load("icon/png/start.png")
        backgroundImg = pygame.transform.scale(backgroundImg, (SCREENWIDTH, SCREENHEIGHT))

        while menu:
            mouse = pygame.mouse.get_pos()

            button_start_color = button_grey
            button_options_color = button_grey
            button_title_color = button_grey
            button_exit_color = button_grey

            if (button_start_x <= mouse[0] <= button_start_x + button_start_width and
                    button_start_y <= mouse[1] <= button_start_y + button_start_height):
                button_start_color = button_hovergrey
            elif (button_options_x <= mouse[0] <= button_options_x + button_options_width and
                  button_options_y <= mouse[1] <= button_options_y + button_options_height):
                button_options_color = button_hovergrey
            elif (button_title_x <= mouse[0] <= button_title_x + button_title_width and
                  button_title_y <= mouse[1] <= button_title_y + button_title_height):
                button_title_color = button_hovergrey
            elif (button_exit_x <= mouse[0] <= button_exit_x + button_exit_width and
                  button_exit_y <= mouse[1] <= button_exit_y + button_exit_height):
                button_exit_color = button_hovergrey

            pygame.display.update()
            win.fill(beige)

            pygame.draw.rect(win, outline_color, button_start_outline)
            pygame.draw.rect(win, outline_color, button_options_outline)
            pygame.draw.rect(win, outline_color, button_title_outline)
            pygame.draw.rect(win, outline_color, button_exit_outline)

            win.blit(backgroundImg, (0,0))

            pygame.draw.rect(win, button_start_color, button_start)
            pygame.draw.rect(win, button_options_color, button_options)
            pygame.draw.rect(win, button_title_color, button_title)
            pygame.draw.rect(win, button_exit_color, button_exit)

            # win.blit(text_largetitle, text_largetitle_rect)
            win.blit(text_start, text_start_rect)
            win.blit(text_options, text_options_rect)
            win.blit(text_title, text_title_rect)
            win.blit(text_exit, text_exit_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if (button_start_x <= mouse[0] <= button_start_x + button_start_width and
                            button_start_y <= mouse[1] <= button_start_y + button_start_height):
                        gameRunning = True
                        self.getName()
                    elif (button_options_x <= mouse[0] <= button_options_x + button_options_width and
                          button_options_y <= mouse[1] <= button_options_y + button_options_height):
                        self.options()
                    elif (button_title_x <= mouse[0] <= button_title_x + button_title_width and
                          button_title_y <= mouse[1] <= button_title_y + button_title_height):
                        self.credits()
                    elif (button_exit_x <= mouse[0] <= button_exit_x + button_exit_width and
                          button_exit_y <= mouse[1] <= button_exit_y + button_exit_height):
                        self.exit()

    def credits(self):
        isInCredits = True

        outlineborder = 10

        returnImg = pygame.image.load('icon/png/return.png')

        font = pygame.font.SysFont('Arial', 20)
        titlefont = pygame.font.SysFont('trebuchetms', 30)

        screen_rect_x = 200
        screen_rect_y = 100
        screen_rect_width = 800
        screen_rect_height = 475
        screen_rect = pygame.Rect(screen_rect_x, screen_rect_y, screen_rect_width, screen_rect_height)

        screen_outline_x = screen_rect_x - outlineborder
        screen_outline_y = screen_rect_y - outlineborder
        screen_outline_width = screen_rect_width + 2 * outlineborder
        screen_outline_height = screen_rect_height + 2 * outlineborder
        screen_outline = pygame.Rect(screen_outline_x, screen_outline_y, screen_outline_width, screen_outline_height)

        button_return_x = 230
        button_return_y = 130
        button_return_width = 50
        button_return_height = 50
        button_return = pygame.Rect(button_return_x, button_return_y, button_return_width, button_return_height)

        margin = 20
        # button_musicambient_x = screen_rect_x + margin + 100
        # button_musicambient_y = 200
        # button_musicambient_width = 200
        # button_musicambient_height = 50
        # button_musicambient = pygame.Rect(button_musicambient_x, button_musicambient_y, button_musicambient_width,
        #                                   button_musicambient_height)
        #
        # button_musicbattle_x = button_musicambient_x + margin + button_musicambient_width
        # button_musicbattle_y = button_musicambient_y
        # button_musicbattle_width = button_musicambient_width
        # button_musicbattle_height = button_musicambient_height
        # button_musicbattle = pygame.Rect(button_musicbattle_x, button_musicbattle_y, button_musicbattle_width,
        #                                  button_musicbattle_height)

        title_text = titlefont.render('Credits', True, black)
        title_rect = title_text.get_rect(center=(round(screen_rect.center[0]), 150))
        return_text = font.render('Return', True, black)
        return_rect = return_text.get_rect(center=(button_return.center[0], button_return.center[1] - 35))

        musicType = font.render("All Music (all 46 minutes) come from Guild Wars 2. Don't like it, sucks for you.",
                                True,
                                black)
        musicType_rect = musicType.get_rect(topleft=(round(screen_rect_x + margin), 225))

        musicType2 = font.render("Jk - there's a music button.", True, black)
        musicType2_rect = musicType2.get_rect(topleft=(round(screen_rect_x + margin), 250))

        code = font.render("All code is from me, with some help with pygame from Stack Overflow and websites.", True,
                           black)
        code_rect = code.get_rect(topleft=(round(screen_rect_x + margin), 275))

        code2 = font.render("This took a long time, especially since it was solo. I hope you like it!", True,
                            black)
        code2_rect = code2.get_rect(topleft=(round(screen_rect_x + margin), 300))

        author = font.render("-Staas Lin", True,
                             black)
        author_rect = author.get_rect(topleft=(round(screen_rect_x + margin), 325))

        # ambient_text = font.render('Ambient/Adventure', True, black)
        # ambient_rect = ambient_text.get_rect(center=button_musicambient.center)
        # battle_text = font.render('Battle', True, black)
        # battle_rect = battle_text.get_rect(center=button_musicbattle.center)

        while isInCredits:
            mouse = pygame.mouse.get_pos()

            returncolor = button_grey
            ambientcolor = button_grey
            battlecolor = button_grey

            if (button_return_x <= mouse[0] <= button_return_x + button_return_width and
                    button_return_y <= mouse[1] <= button_return_y + button_return_height):
                returncolor = button_hovergrey
            # elif (button_musicambient_x <= mouse[0] <= button_musicambient_x + button_musicambient_width and
            #       button_musicambient_y <= mouse[1] <= button_musicambient_y + button_musicambient_height):
            #     ambientcolor = button_hovergrey
            # elif (button_musicbattle_x <= mouse[0] <= button_musicbattle_x + button_musicbattle_width and
            #       button_musicbattle_y <= mouse[1] <= button_musicbattle_y + button_musicbattle_height):
            #     battlecolor = button_hovergrey

            pygame.draw.rect(win, orange, screen_outline)
            pygame.draw.rect(win, white, screen_rect)
            pygame.draw.rect(win, returncolor, button_return)
            # pygame.draw.rect(win, ambientcolor, button_musicambient)
            # pygame.draw.rect(win, battlecolor, button_musicbattle)

            returnImg = pygame.transform.scale(returnImg, (button_return_width, button_return_height))
            win.blit(returnImg, (button_return_x, button_return_y))

            win.blit(title_text, title_rect)
            # win.blit(return_text, return_rect)
            win.blit(musicType, musicType_rect)
            win.blit(musicType2, musicType2_rect)
            win.blit(code, code_rect)
            win.blit(code2, code2_rect)
            win.blit(author, author_rect)
            # win.blit(ambient_text, ambient_rect)
            # win.blit(battle_text, battle_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass
                    if (button_return_x <= mouse[0] <= button_return_x + button_return_width and
                            button_return_y <= mouse[1] <= button_return_y + button_return_height):
                        return
                    # elif (button_musicambient_x <= mouse[0] <= button_musicambient_x + button_musicambient_width and
                    #       button_musicambient_y <= mouse[1] <= button_musicambient_y + button_musicambient_height):
                    #     switchAmbient()
                    # elif (button_musicbattle_x <= mouse[0] <= button_musicbattle_x + button_musicbattle_width and
                    #       button_musicbattle_y <= mouse[1] <= button_musicbattle_y + button_musicbattle_height):
                    #     switchBattle()
                    #     if musicIsPaused:
                    #         musicIsPaused = False
                    #         unpause()
                    #     elif not musicIsPaused:
                    #         musicIsPaused = True
                    #         pause()
                    # elif (button_options_x <= mouse[0] <= button_options_x + button_options_width and
                    #         button_options_y <= mouse[1] <= button_options_y + button_options_height):
                    #     self.options()
            pygame.display.update(screen_outline)

    def getName(self):
        global nameCreated, gameRunning, player_name
        nameCreated = False
        name = ""
        font = pygame.font.Font(None, 30)
        directionfont = pygame.font.SysFont('Comic Sans MS', 50)
        minidirectionfont = pygame.font.SysFont('Comic Sans MS', 30)

        direction = directionfont.render('Type out Your Name!', True, black)
        minidirection = minidirectionfont.render('(press enter when done!)', True, black)

        underline = pygame.Rect(win.get_rect().center[0] - 300, win.get_rect().center[1] + 10, 600, 1)

        while nameCreated == False:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.unicode.isalpha():
                        name += event.unicode
                    elif event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    elif event.key == pygame.K_RETURN:
                        nameCreated = True
                        gameRunning = True
                        if len(name) > 0:
                            p1.name = name  # else default is peasant
                        self.startGame()
                elif event.type == pygame.QUIT:
                    self.exit()

            win.fill(beige)
            block = font.render(name, True, (0, 0, 0))
            rect = block.get_rect()
            rect.center = win.get_rect().center

            direction_rect = direction.get_rect(center=(round(SCREENWIDTH / 2), rect.center[1] - 300))
            minidirection_rect = minidirection.get_rect(center=(round(SCREENWIDTH / 2), rect.center[1] - 225))
            win.blit(direction, direction_rect)
            win.blit(minidirection, minidirection_rect)

            pygame.draw.rect(win, black, underline)

            win.blit(block, rect)
            pygame.display.update()

    def startGame(self):
        global gameRunning

        text = p1.name.capitalize() + "! Welcome to The Adventures of a Peasant" + \
               ". This game is a text-based game, featuring you, a peasant! Your goal is " \
               "to collect some decent gear and defeat the horrible dragon who has been terrorizing this land. You " \
               "will have various options that light up when you can use them. Your commands are: Explore, Combat, " \
               "Flee, Trade, Yes, No, Meat, and Potion. You can also click that backpack on the side to see your " \
               "inventory. If you don't like the music or want to change it, you can click on the Pause or Options button."

        exploreImg = pygame.image.load("icon/png/map.png")
        combatImg = pygame.image.load("icon/png/attack.png")
        fleeImg = pygame.image.load("icon/png/flee.png")
        tradeImg = pygame.image.load("icon/png/trade.png")
        yesImg = pygame.image.load("icon/png/yes.png")
        noImg = pygame.image.load("icon/png/no.png")
        foodImg = pygame.image.load("icon/png/food.png")
        drinkImg = pygame.image.load("icon/png/drink.png")

        pauseImg = pygame.image.load("icon/png/pause.png")
        optionsImg = pygame.image.load("icon/png/gear.png")
        inventoryImg = pygame.image.load("icon/png/inventory.png")

        hpImg = pygame.image.load("icon/png/hpinvert.png")
        attackImg = pygame.image.load("icon/png/attackinvert.png")
        defenseImg = pygame.image.load("icon/png/defenseinvert.png")
        goldImg = pygame.image.load("icon/png/goldinvert.png")
        playerImg = pygame.image.load("icon/png/playerinverted.png")

        textfont = pygame.font.SysFont('couriernew', 20)
        statfont = pygame.font.SysFont('Helvetica', 30)
        buttonfont = pygame.font.SysFont('Arial', 50)

        explore_text = textfont.render('Explore', True, black)
        combat_text = textfont.render('Combat', True, black)
        flee_text = textfont.render('Flee', True, black)
        trade_text = textfont.render('Trade', True, black)
        yes_text = textfont.render('Yes', True, black)
        no_text = textfont.render('No', True, black)
        meat_text = textfont.render('Meat', True, black)
        potion_text = textfont.render('Potion', True, black)

        iconsize = 50
        spacing = 10
        textwidth = 150
        textheight = 50

        button_area_spacing = 10
        button_spacing = 20

        button_inventory_x = 30
        button_inventory_y = 300
        button_inventory_width = 100
        button_inventory_height = 100
        button_inventory = pygame.Rect(button_inventory_x, button_inventory_y, button_inventory_width,
                                       button_inventory_height)

        button_pause_x = 30
        button_pause_y = 170
        button_pause_width = 100
        button_pause_height = 100
        button_pause = pygame.Rect(button_pause_x, button_pause_y, button_pause_width, button_pause_height)

        button_options_x = 30
        button_options_y = 430
        button_options_width = 100
        button_options_height = 100
        button_options = pygame.Rect(button_options_x, button_options_y, button_options_width, button_options_height)

        rect_console_x = 150
        rect_console_y = 150
        rect_console_width = 1000
        rect_console_height = 475
        rect_console = pygame.Rect(rect_console_x, rect_console_y, rect_console_width, rect_console_height)

        rect_adventure_x = 150
        rect_adventure_y = 150
        rect_adventure_width = 1000
        rect_adventure_height = 450
        rect_adventure = pygame.Rect(rect_adventure_x, rect_adventure_y, rect_adventure_width, rect_adventure_height)
        intermediate = pygame.surface.Surface((1000, 10000))
        scroll_y = 0

        rect_spacing_x = 0
        rect_spacing_y = 120
        rect_spacing_width = SCREENWIDTH
        rect_spacing_height = 30
        rect_spacing = pygame.Rect(rect_spacing_x, rect_spacing_y, rect_spacing_width, rect_spacing_height)

        rect_buttonarea_x = rect_console_x + button_area_spacing
        rect_buttonarea_y = 450
        rect_buttonarea_width = rect_console_width - 2 * button_area_spacing
        rect_buttonarea_height = rect_console_height - 300 - button_area_spacing
        rect_buttonarea = pygame.Rect(rect_buttonarea_x, rect_buttonarea_y, rect_buttonarea_width,
                                      rect_buttonarea_height)

        # BUTTONS - explore/walk, fight/attack, talk/trade(?), y/n(?), action/pickup(?)
        # SUBSETS - Return - 1st, Explore - West, East, towards town(?)/into forest(?), Fight- (Right/Left(?), Block, Flee(?), etc

        button_width = 100
        button_height = 100
        button_y = 500

        button_explore_x = rect_buttonarea_x + button_spacing
        button_explore_y = button_y
        button_explore_width = button_width
        button_explore_height = button_height
        button_explore = pygame.Rect(button_explore_x, button_explore_y, button_explore_width, button_explore_height)

        button_combat_x = button_explore_x + button_width + button_spacing
        button_combat_y = button_y
        button_combat_width = button_width
        button_combat_height = button_height
        button_combat = pygame.Rect(button_combat_x, button_combat_y, button_combat_width, button_combat_height)

        button_flee_x = button_combat_x + button_width + button_spacing
        button_flee_y = button_y
        button_flee_width = button_width
        button_flee_height = button_height
        button_flee = pygame.Rect(button_flee_x, button_flee_y, button_flee_width, button_flee_height)

        button_trade_x = button_flee_x + button_width + button_spacing
        button_trade_y = button_y
        button_trade_width = button_width
        button_trade_height = button_height
        button_trade = pygame.Rect(button_trade_x, button_trade_y, button_trade_width, button_trade_height)

        button_yes_x = button_trade_x + button_width + button_spacing
        button_yes_y = button_y
        button_yes_width = button_width
        button_yes_height = button_height
        button_yes = pygame.Rect(button_yes_x, button_yes_y, button_yes_width, button_yes_height)

        button_no_x = button_yes_x + button_width + button_spacing
        button_no_y = button_y
        button_no_width = button_width
        button_no_height = button_height
        button_no = pygame.Rect(button_no_x, button_no_y, button_no_width, button_no_height)

        button_food_x = button_no_x + button_width + button_spacing
        button_food_y = button_y
        button_food_width = button_width
        button_food_height = button_height
        button_food = pygame.Rect(button_food_x, button_food_y, button_food_width, button_food_height)

        button_drink_x = button_food_x + button_width + button_spacing
        button_drink_y = button_y
        button_drink_width = button_width
        button_drink_height = button_height
        button_drink = pygame.Rect(button_drink_x, button_drink_y, button_drink_width, button_drink_height)

        rect_stats_x = 0
        rect_stats_y = 0
        rect_stats_width = 1200
        rect_stats_height = 120
        rect_stats = pygame.Rect(rect_stats_x, rect_stats_y, rect_stats_width, rect_stats_height)

        hp_rect_x = rect_stats_x + iconsize + 2 * spacing
        hp_rect_y = rect_stats_y + spacing
        hp_rect_width = textwidth
        hp_rect_height = textheight
        hp_rect = pygame.Rect(hp_rect_x, hp_rect_y, hp_rect_width, hp_rect_height)

        attack_rect_x = hp_rect_x + iconsize + 2 * spacing + hp_rect_width
        attack_rect_y = hp_rect_y
        attack_rect_width = textwidth
        attack_rect_height = textheight
        attack_rect = pygame.Rect(attack_rect_x, attack_rect_y, attack_rect_width, attack_rect_height)

        defense_rect_x = attack_rect_x + iconsize + 2 * spacing + attack_rect_width
        defense_rect_y = hp_rect_y
        defense_rect_width = textwidth
        defense_rect_height = textheight
        defense_rect = pygame.Rect(defense_rect_x, defense_rect_y, defense_rect_width, defense_rect_height)

        gold_rect_x = defense_rect_x + iconsize + 2 * spacing + defense_rect_width
        gold_rect_y = hp_rect_y
        gold_rect_width = textwidth
        gold_rect_height = textheight
        gold_rect = pygame.Rect(gold_rect_x, gold_rect_y, gold_rect_width, gold_rect_height)

        name_rect_x = gold_rect_x + iconsize + 2 * spacing + gold_rect_width
        name_rect_y = hp_rect_y
        name_rect_width = textwidth
        name_rect_height = textheight
        name_rect = pygame.Rect(name_rect_x, name_rect_y, name_rect_width, name_rect_height)

        while gameRunning:
            mouse = pygame.mouse.get_pos()

            '''Status Bar Text Fields'''
            stat_name_text = statfont.render(str(p1.name), True, white)
            stat_hp_text = statfont.render(str(p1.hp), True, white)
            stat_attack_text = statfont.render(str(p1.weapon.attack), True, white)
            stat_defense_text = statfont.render(str(p1.defense.total), True, white)
            stat_gold_text = statfont.render(str(p1.gold), True, white)
            stat_level_text = statfont.render(str(p1.level), True, white)

            '''Status Bar Icon Positioning'''
            temp = stat_hp_text.get_rect(center=hp_rect.center)
            temp = stat_attack_text.get_rect(center=attack_rect.center)
            temp = stat_defense_text.get_rect(center=defense_rect.center)
            temp = stat_gold_text.get_rect(center=gold_rect.center)
            temp = stat_name_text.get_rect(center=name_rect.center)
            intermediate_rect = intermediate.get_rect(topleft=(150, 150))
            # intermediate_rect.x = 100
            # intermediate_rect.y = 100

            '''Button Colors'''
            inv_color = button_grey
            pause_color = button_grey
            options_color = button_grey

            '''Action Button Colors: DEFAULT'''
            explore_color = orange
            combat_color = button_grey
            flee_color = button_grey
            trade_color = button_grey
            yes_color = button_grey
            no_color = button_grey
            food_color = button_grey
            drink_color = button_grey

            '''Action Button Colors: BY STATUS'''
            if (p1.status == 'normal'):
                flee_color = button_grey
                food_color = orange
                drink_color = orange
            elif (p1.status == 'combat'):
                explore_color = button_grey
                combat_color = orange
                flee_color = orange
            elif (p1.status == 'witchhut' or p1.status == 'accepttrade' or p1.status == 'gold' or p1.status == 'bandit?' or p1.status == 'bossfight'):
                yes_color = orange
                no_color = orange
            elif (p1.status == 'village'):
                trade_color = orange

            '''Button UI Settings'''
            if (button_inventory_x <= mouse[0] <= button_inventory_x + button_inventory_width and
                    button_inventory_y <= mouse[1] <= button_inventory_y + button_inventory_height):
                inv_color = button_hovergrey

            elif (button_pause_x <= mouse[0] <= button_pause_x + button_pause_width and
                  button_pause_y <= mouse[1] <= button_pause_y + button_pause_height):
                pause_color = button_hovergrey

            elif (button_options_x <= mouse[0] <= button_options_x + button_options_width and
                  button_options_y <= mouse[1] <= button_options_y + button_options_height):
                options_color = button_hovergrey

            elif (button_explore_x <= mouse[0] <= button_explore_x + button_explore_width and
                  button_explore_y <= mouse[1] <= button_explore_y + button_explore_height):
                if explore_color == orange:
                    explore_color = darkorange
                elif explore_color == button_grey:
                    explore_color = button_hovergrey

            elif (button_combat_x <= mouse[0] <= button_combat_x + button_combat_width and
                  button_combat_y <= mouse[1] <= button_combat_y + button_combat_height):
                if combat_color == orange:
                    combat_color = darkorange
                elif combat_color == button_grey:
                    combat_color = button_hovergrey

            elif (button_flee_x <= mouse[0] <= button_flee_x + button_flee_width and
                  button_flee_y <= mouse[1] <= button_flee_y + button_flee_height):
                if flee_color == orange:
                    flee_color = darkorange
                elif flee_color == button_grey:
                    flee_color = button_hovergrey

            elif (button_trade_x <= mouse[0] <= button_trade_x + button_trade_width and
                  button_trade_y <= mouse[1] <= button_trade_y + button_trade_height):
                if trade_color == orange:
                    trade_color = darkorange
                elif trade_color == button_grey:
                    trade_color = button_hovergrey

            elif (button_yes_x <= mouse[0] <= button_yes_x + button_yes_width and
                  button_yes_y <= mouse[1] <= button_yes_y + button_yes_height):
                if yes_color == orange:
                    yes_color = darkorange
                elif yes_color == button_grey:
                    yes_color = button_hovergrey

            elif (button_no_x <= mouse[0] <= button_no_x + button_no_width and
                  button_no_y <= mouse[1] <= button_no_y + button_no_height):
                if no_color == orange:
                    no_color = darkorange
                elif no_color == button_grey:
                    no_color = button_hovergrey

            elif (button_food_x <= mouse[0] <= button_food_x + button_food_width and
                  button_food_y <= mouse[1] <= button_food_y + button_food_height):
                if food_color == orange:
                    food_color = darkorange
                elif food_color == button_grey:
                    food_color = button_hovergrey

            elif (button_drink_x <= mouse[0] <= button_drink_x + button_drink_width and
                  button_drink_y <= mouse[1] <= button_drink_y + button_drink_height):
                if drink_color == orange:
                    drink_color = darkorange
                elif drink_color == button_grey:
                    drink_color = button_hovergrey

            win.fill(beige)

            pygame.draw.rect(win, white, rect_console)
            win.blit(intermediate, (intermediate_rect.x, intermediate_rect.y + scroll_y))
            intermediate.fill(black)
            self.blit_text(intermediate, intermediate_rect, text, (intermediate_rect.x, intermediate_rect.y), textfont,
                           white)

            pygame.draw.rect(win, black, rect_stats)
            pygame.draw.rect(win, beige, rect_spacing)
            pygame.draw.rect(win, darkgrey, rect_buttonarea)

            pygame.draw.ellipse(win, inv_color, button_inventory, 100)
            pygame.draw.ellipse(win, pause_color, button_pause, 100)
            pygame.draw.ellipse(win, options_color, button_options, 100)

            pygame.draw.rect(win, explore_color, button_explore)
            pygame.draw.rect(win, combat_color, button_combat)
            pygame.draw.rect(win, flee_color, button_flee)
            pygame.draw.rect(win, trade_color, button_trade)
            pygame.draw.rect(win, yes_color, button_yes)
            pygame.draw.rect(win, no_color, button_no)
            pygame.draw.rect(win, food_color, button_food)
            pygame.draw.rect(win, drink_color, button_drink)

            exploreImg = pygame.transform.scale(exploreImg, (button_explore_width, button_explore_height))
            combatImg = pygame.transform.scale(combatImg, (button_combat_width, button_combat_height))
            fleeImg = pygame.transform.scale(fleeImg, (button_flee_width, button_flee_height))
            tradeImg = pygame.transform.scale(tradeImg, (button_trade_width, button_trade_height))
            yesImg = pygame.transform.scale(yesImg, (button_yes_width, button_yes_height))
            noImg = pygame.transform.scale(noImg, (button_no_width, button_no_height))
            foodImg = pygame.transform.scale(foodImg, (button_food_width, button_food_height))
            drinkImg = pygame.transform.scale(drinkImg, (button_drink_width, button_drink_height))

            pauseImg = pygame.transform.scale(pauseImg, (button_pause_width, button_pause_height))
            optionsImg = pygame.transform.scale(optionsImg, (button_options_width, button_options_height))
            inventoryImg = pygame.transform.scale(inventoryImg, (button_inventory_width, button_inventory_height))

            hpImg = pygame.transform.scale(hpImg, (iconsize, iconsize))
            attackImg = pygame.transform.scale(attackImg, (iconsize, iconsize))
            defenseImg = pygame.transform.scale(defenseImg, (iconsize, iconsize))
            goldImg = pygame.transform.scale(goldImg, (iconsize, iconsize))
            playerImg = pygame.transform.scale(playerImg, (iconsize, iconsize))

            win.blit(exploreImg, (button_explore_x, button_explore_y))
            win.blit(combatImg, (button_combat_x, button_combat_y))
            win.blit(fleeImg, (button_flee_x, button_flee_y))
            win.blit(tradeImg, (button_trade_x, button_trade_y))
            win.blit(yesImg, (button_yes_x, button_yes_y))
            win.blit(noImg, (button_no_x, button_no_y))
            win.blit(foodImg, (button_food_x, button_food_y))
            win.blit(drinkImg, (button_drink_x, button_drink_y))

            win.blit(pauseImg, (button_pause_x, button_pause_y))
            win.blit(optionsImg, (button_options_x, button_options_y))
            win.blit(inventoryImg, (button_inventory_x, button_inventory_y))

            win.blit(hpImg, (hp_rect_x - spacing - iconsize, hp_rect_y))
            win.blit(attackImg, (attack_rect_x - spacing - iconsize, attack_rect_y))
            win.blit(defenseImg, (defense_rect_x - spacing - iconsize, defense_rect_y))
            win.blit(goldImg, (gold_rect_x - spacing - iconsize, gold_rect_y))
            win.blit(playerImg, (name_rect_x - spacing - iconsize, name_rect_y))

            win.blit(stat_hp_text, hp_rect)
            win.blit(stat_attack_text, attack_rect)
            win.blit(stat_defense_text, defense_rect)
            win.blit(stat_gold_text, gold_rect)
            win.blit(stat_name_text, name_rect)

            win.blit(explore_text, (button_explore.topleft[0] + 10, button_explore.topleft[1] - 25))
            win.blit(combat_text, (button_combat.topleft[0] + 10, button_combat.topleft[1] - 25))
            win.blit(flee_text, (button_flee.topleft[0] + 10, button_flee.topleft[1] - 25))
            win.blit(trade_text, (button_trade.topleft[0] + 10, button_trade.topleft[1] - 25))
            win.blit(yes_text, (button_yes.topleft[0] + 10, button_yes.topleft[1] - 25))
            win.blit(no_text, (button_no.topleft[0] + 10, button_no.topleft[1] - 25))
            win.blit(meat_text, (button_food.topleft[0] + 10, button_food.topleft[1] - 25))
            win.blit(potion_text, (button_drink.topleft[0] + 10, button_drink.topleft[1] - 25))

            for event in pygame.event.get():
                if (p1.hp <= 0):
                    self.gameLose()

                if event.type == pygame.QUIT:
                    self.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if (button_inventory_x <= mouse[0] <= button_inventory_x + button_inventory_width and
                            button_inventory_y <= mouse[1] <= button_inventory_y + button_inventory_height):
                        result = p1.returnInventory()
                        # text += result
                        if result == None:
                            pass
                        else:
                            text = result
                    elif (button_pause_x <= mouse[0] <= button_pause_x + button_pause_width and
                          button_pause_y <= mouse[1] <= button_pause_y + button_pause_height):
                        self.pause()
                    elif (button_explore_x <= mouse[0] <= button_explore_x + button_explore_width and
                          button_explore_y <= mouse[1] <= button_explore_y + button_explore_height):
                        result = p1.explore()
                        # text += result
                        if result == None:
                            pass
                        else:
                            text = result

                    elif (button_combat_x <= mouse[0] <= button_combat_x + button_combat_width and
                          button_combat_y <= mouse[1] <= button_combat_y + button_combat_height):
                        result = p1.directAttack()
                        if result == None:
                            pass
                        elif result == True:
                            self.gameWin()
                        else:
                            text = result

                    elif (button_flee_x <= mouse[0] <= button_flee_x + button_flee_width and
                          button_flee_y <= mouse[1] <= button_flee_y + button_flee_height):
                        result = p1.flee()
                        # text += result
                        if result == None:
                            pass
                        else:
                            text = result

                    elif (button_trade_x <= mouse[0] <= button_trade_x + button_trade_width and
                          button_trade_y <= mouse[1] <= button_trade_y + button_trade_height):
                        result = p1.trade()
                        # text += result
                        if result == None:
                            pass
                        else:
                            text = result

                    elif (button_yes_x <= mouse[0] <= button_yes_x + button_yes_width and
                          button_yes_y <= mouse[1] <= button_yes_y + button_yes_height):
                        result = p1.yes()
                        # text += result
                        if result == None:
                            pass
                        else:
                            text = result

                    elif (button_no_x <= mouse[0] <= button_no_x + button_no_width and
                          button_no_y <= mouse[1] <= button_no_y + button_no_height):
                        result = p1.no()
                        # text += result
                        if result == None:
                            pass
                        else:
                            text = result

                    elif (button_food_x <= mouse[0] <= button_food_x + button_food_width and
                          button_food_y <= mouse[1] <= button_food_y + button_food_height):
                        result = p1.use('meat')
                        # text += result
                        if result == None:
                            pass
                        else:
                            text = result

                    elif (button_drink_x <= mouse[0] <= button_drink_x + button_drink_width and
                          button_drink_y <= mouse[1] <= button_drink_y + button_drink_height):
                        x = self.drinkMenu()
                        if (x != 'Returned'):
                            result = p1.use(x)
                            if result == None:
                                pass
                            else:
                                text = result

                    elif (button_options_x <= mouse[0] <= button_options_x + button_options_width and
                          button_options_y <= mouse[1] <= button_options_y + button_options_height):
                        self.options()

                    if (event.button == 4) and (rect_console_x <= mouse[0] <= rect_console_x + rect_console_width and
                                                rect_console_y <= mouse[1] <= rect_console_y + rect_console_height):
                        scroll_y = min(scroll_y + 15, 0)
                    elif (event.button == 5) and (rect_console_x <= mouse[0] <= rect_console_x + rect_console_width and
                                                  rect_console_y <= mouse[1] <= rect_console_y + rect_console_height):
                        scroll_y = max(scroll_y - 15, -300)

                if event.type == pygame.K_i:
                    pass

            pygame.display.update()

    def drinkMenu(self):

        x = 'Returned'
        isSelecting = True

        returnImg = pygame.image.load('icon/png/return.png')

        titlefont = pygame.font.SysFont('trebuchetms', 40)
        buttonfont = pygame.font.SysFont('Arial', 20)

        title_text = titlefont.render('What potion are you using?', True, black)
        health_text = buttonfont.render('Health Pot', True, black)
        strength_text = buttonfont.render('Strength Pot', True, black)
        mystery_text = buttonfont.render('Mystery Pot', True, black)

        outlineborder = 10

        screen_rect_x = 200
        screen_rect_y = 100
        screen_rect_width = 800
        screen_rect_height = 475
        screen_rect = pygame.Rect(screen_rect_x, screen_rect_y, screen_rect_width, screen_rect_height)

        screen_outline_x = screen_rect_x - outlineborder
        screen_outline_y = screen_rect_y - outlineborder
        screen_outline_width = screen_rect_width + 2 * outlineborder
        screen_outline_height = screen_rect_height + 2 * outlineborder
        screen_outline = pygame.Rect(screen_outline_x, screen_outline_y, screen_outline_width, screen_outline_height)

        button_return_x = 230
        button_return_y = 130
        button_return_width = 50
        button_return_height = 50
        button_return = pygame.Rect(button_return_x, button_return_y, button_return_width, button_return_height)

        button_health_x = 300
        button_health_y = 400
        button_health_width = 150
        button_health_height = 70
        button_health = pygame.Rect(button_health_x, button_health_y, button_health_width, button_health_height)

        button_strength_x = 470
        button_strength_y = 400
        button_strength_width = 150
        button_strength_height = 70
        button_strength = pygame.Rect(button_strength_x, button_strength_y, button_strength_width,
                                      button_strength_height)

        button_mystery_x = 640
        button_mystery_y = 400
        button_mystery_width = 150
        button_mystery_height = 70
        button_mystery = pygame.Rect(button_mystery_x, button_mystery_y, button_mystery_width, button_mystery_height)

        title_rect = title_text.get_rect(center=(600, 150))
        health_rect = health_text.get_rect(center=button_health.center)
        strength_rect = strength_text.get_rect(center=button_strength.center)
        mystery_rect = mystery_text.get_rect(center=button_mystery.center)

        while isSelecting:
            mouse = pygame.mouse.get_pos()

            healthcolor = button_grey
            strengthcolor = button_grey
            returncolor = button_grey
            mysterycolor = button_grey

            if (button_return_x <= mouse[0] <= button_return_x + button_return_width and
                    button_return_y <= mouse[1] <= button_return_y + button_return_height):
                returncolor = button_hovergrey
            elif (button_health_x <= mouse[0] <= button_health_x + button_health_width and
                  button_health_y <= mouse[1] <= button_health_y + button_health_height):
                healthcolor = button_hovergrey
            elif (button_strength_x <= mouse[0] <= button_strength_x + button_strength_width and
                  button_strength_y <= mouse[1] <= button_strength_y + button_strength_height):
                strengthcolor = button_hovergrey
            elif (button_mystery_x <= mouse[0] <= button_mystery_x + button_mystery_width and
                  button_mystery_y <= mouse[1] <= button_mystery_y + button_mystery_height):
                mysterycolor = button_hovergrey

            pygame.draw.rect(win, yellow, screen_outline)
            pygame.draw.rect(win, white, screen_rect)
            pygame.draw.rect(win, healthcolor, button_health)
            pygame.draw.rect(win, strengthcolor, button_strength)
            pygame.draw.rect(win, mysterycolor, button_mystery)
            pygame.draw.rect(win, returncolor, button_return)

            returnImg = pygame.transform.scale(returnImg, (button_return_width, button_return_height))

            win.blit(returnImg, (button_return_x, button_return_y))

            win.blit(title_text, title_rect)
            win.blit(health_text, health_rect)
            win.blit(strength_text, strength_rect)
            win.blit(mystery_text, mystery_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if (button_strength_x <= mouse[0] <= button_strength_x + button_strength_width and
                            button_strength_y <= mouse[1] <= button_strength_y + button_strength_height):
                        x = 'strength_pot'
                        return x

                    elif (button_health_x <= mouse[0] <= button_health_x + button_health_width and
                          button_health_y <= mouse[1] <= button_health_y + button_health_height):
                        x = 'health_pot'
                        return x

                    elif (button_mystery_x <= mouse[0] <= button_mystery_x + button_mystery_width and
                          button_mystery_y <= mouse[1] <= button_mystery_y + button_mystery_height):
                        x = 'mystery_pot'
                        return x

                    elif (button_return_x <= mouse[0] <= button_return_x + button_return_width and
                          button_return_y <= mouse[1] <= button_return_y + button_return_height):
                        return x

            pygame.display.update(screen_outline)

    def explore_subMenu(self):
        inMenu = True
        update_rect = pygame.Rect(150, 150, 1000, 475)

        # button_findTown_x = button_findTown_y = button_findTown_width = button_findTown_height = button_findTown =
        # pygame.Rect(button_findTown_x, button_findTown_y, button_findTown_width, button_findTown_height)
        #
        # button_continueWalking_x = button_continueWalking_y = button_continueWalking_width =
        # button_continueWalking_height = button_continueWalking = pygame.Rect(button_continueWalking_x,
        # button_continueWalking_y, button_continueWalking_width, button_continueWalking_height)

        while inMenu:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit()
                # if event.type == pygame.MOUSEBUTTONDOWN:

            pygame.display.update(update_rect)

    def pause(self):
        global musicIsPaused
        isPaused = True

        musicImg = pygame.image.load("icon/png/sound.png")
        muteImg = pygame.image.load("icon/png/mute.png")

        titlefont = pygame.font.SysFont('trebuchetms', 40)
        buttonfont = pygame.font.SysFont('Arial', 30)

        title_text = titlefont.render('Paused', True, black)
        options_text = buttonfont.render('Options', True, black)
        continue_text = buttonfont.render('Continue', True, black)

        outlineborder = 10

        screen_rect_x = 200
        screen_rect_y = 100
        screen_rect_width = 800
        screen_rect_height = 475
        screen_rect = pygame.Rect(screen_rect_x, screen_rect_y, screen_rect_width, screen_rect_height)

        screen_outline_x = screen_rect_x - outlineborder
        screen_outline_y = screen_rect_y - outlineborder
        screen_outline_width = screen_rect_width + 2 * outlineborder
        screen_outline_height = screen_rect_height + 2 * outlineborder
        screen_outline = pygame.Rect(screen_outline_x, screen_outline_y, screen_outline_width, screen_outline_height)

        button_options_x = 525
        button_options_y = 300
        button_options_width = 150
        button_options_height = 70
        button_options = pygame.Rect(button_options_x, button_options_y, button_options_width, button_options_height)

        button_continue_x = 525
        button_continue_y = 400
        button_continue_width = 150
        button_continue_height = 70
        button_continue = pygame.Rect(button_continue_x, button_continue_y, button_continue_width,
                                      button_continue_height)

        button_music_x = 525
        button_music_y = 200
        button_music_width = 50
        button_music_height = 50
        button_music = pygame.Rect(button_music_x, button_music_y, button_music_width, button_music_height)

        button_mute_x = 625
        button_mute_y = 200
        button_mute_width = 50
        button_mute_height = 50
        button_mute = pygame.Rect(button_mute_x, button_mute_y, button_mute_width, button_mute_height)

        title_rect = title_text.get_rect(center=(600, 150))
        options_rect = options_text.get_rect(center=button_options.center)
        continue_rect = continue_text.get_rect(center=button_continue.center)

        while isPaused:
            mouse = pygame.mouse.get_pos()

            optionscolor = button_grey
            musiccolor = orange
            mutecolor = button_grey
            continuecolor = button_grey

            if (musicIsPaused):
                mutecolor = orange
                musiccolor = button_grey
            elif (not musicIsPaused):
                mutecolor = button_grey
                musiccolor = orange

            if (button_options_x <= mouse[0] <= button_options_x + button_options_width and
                    button_options_y <= mouse[1] <= button_options_y + button_options_height):
                if optionscolor == orange:
                    optionscolor = darkorange
                elif optionscolor == button_grey:
                    optionscolor = button_hovergrey
            elif (button_music_x <= mouse[0] <= button_music_x + button_music_width and
                  button_music_y <= mouse[1] <= button_music_y + button_music_height):
                if musiccolor == orange:
                    musiccolor = darkorange
                elif musiccolor == button_grey:
                    musiccolor = button_hovergrey
            elif (button_mute_x <= mouse[0] <= button_mute_x + button_mute_width and
                  button_mute_y <= mouse[1] <= button_mute_y + button_mute_height):
                if mutecolor == orange:
                    mutecolor = darkorange
                elif mutecolor == button_grey:
                    mutecolor = button_hovergrey
            elif (button_continue_x <= mouse[0] <= button_continue_x + button_continue_width and
                  button_continue_y <= mouse[1] <= button_continue_y + button_continue_height):
                if continuecolor == orange:
                    continuecolor = darkorange
                elif continuecolor == button_grey:
                    continuecolor = button_hovergrey

            pygame.draw.rect(win, yellow, screen_outline)
            pygame.draw.rect(win, white, screen_rect)
            pygame.draw.rect(win, optionscolor, button_options)
            pygame.draw.rect(win, continuecolor, button_continue)
            pygame.draw.rect(win, mutecolor, button_mute)
            pygame.draw.rect(win, musiccolor, button_music)

            musicImg = pygame.transform.scale(musicImg, (button_music_width, button_music_height))
            muteImg = pygame.transform.scale(muteImg, (button_mute_width, button_mute_height))

            win.blit(musicImg, (button_music_x, button_music_y))
            win.blit(muteImg, (button_mute_x, button_mute_y))

            win.blit(title_text, title_rect)
            win.blit(options_text, options_rect)
            win.blit(continue_text, continue_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if (button_continue_x <= mouse[0] <= button_continue_x + button_continue_width and
                            button_continue_y <= mouse[1] <= button_continue_y + button_continue_height):
                        return
                    elif (button_mute_x <= mouse[0] <= button_mute_x + button_mute_width and
                          button_mute_y <= mouse[1] <= button_mute_y + button_mute_height):
                        pause()

                    elif (button_music_x <= mouse[0] <= button_music_x + button_music_width and
                          button_music_y <= mouse[1] <= button_music_y + button_music_height):
                        unpause()

                    elif (button_options_x <= mouse[0] <= button_options_x + button_options_width and
                          button_options_y <= mouse[1] <= button_options_y + button_options_height):
                        self.options()

            pygame.display.update(screen_outline)

    def options(self):
        isInOption = True

        outlineborder = 10

        returnImg = pygame.image.load('icon/png/return.png')

        font = pygame.font.SysFont('Arial', 20)
        titlefont = pygame.font.SysFont('trebuchetms', 30)

        screen_rect_x = 200
        screen_rect_y = 100
        screen_rect_width = 800
        screen_rect_height = 475
        screen_rect = pygame.Rect(screen_rect_x, screen_rect_y, screen_rect_width, screen_rect_height)

        screen_outline_x = screen_rect_x - outlineborder
        screen_outline_y = screen_rect_y - outlineborder
        screen_outline_width = screen_rect_width + 2 * outlineborder
        screen_outline_height = screen_rect_height + 2 * outlineborder
        screen_outline = pygame.Rect(screen_outline_x, screen_outline_y, screen_outline_width, screen_outline_height)

        button_return_x = 230
        button_return_y = 130
        button_return_width = 50
        button_return_height = 50
        button_return = pygame.Rect(button_return_x, button_return_y, button_return_width, button_return_height)

        margin = 20
        button_musicambient_x = screen_rect_x + margin + 100
        button_musicambient_y = 200
        button_musicambient_width = 200
        button_musicambient_height = 50
        button_musicambient = pygame.Rect(button_musicambient_x, button_musicambient_y, button_musicambient_width,
                                          button_musicambient_height)

        button_musicbattle_x = button_musicambient_x + margin + button_musicambient_width
        button_musicbattle_y = button_musicambient_y
        button_musicbattle_width = button_musicambient_width
        button_musicbattle_height = button_musicambient_height
        button_musicbattle = pygame.Rect(button_musicbattle_x, button_musicbattle_y, button_musicbattle_width,
                                         button_musicbattle_height)

        title_text = titlefont.render('Options', True, black)
        title_rect = title_text.get_rect(center=(round(screen_rect.center[0]), 150))
        return_text = font.render('Return', True, black)
        return_rect = return_text.get_rect(center=(button_return.center[0], button_return.center[1] - 35))

        musicType = font.render('Music Type: ', True, black)
        musicType_rect = musicType.get_rect(center=(round(screen_rect_x + margin + 50), 225))

        ambient_text = font.render('Ambient/Adventure', True, black)
        ambient_rect = ambient_text.get_rect(center=button_musicambient.center)
        battle_text = font.render('Battle [Caution:Loud]', True, black)
        battle_rect = battle_text.get_rect(center=button_musicbattle.center)

        while isInOption:
            mouse = pygame.mouse.get_pos()

            returncolor = button_grey
            ambientcolor = button_grey
            battlecolor = button_grey

            if (button_return_x <= mouse[0] <= button_return_x + button_return_width and
                    button_return_y <= mouse[1] <= button_return_y + button_return_height):
                returncolor = button_hovergrey
            elif (button_musicambient_x <= mouse[0] <= button_musicambient_x + button_musicambient_width and
                  button_musicambient_y <= mouse[1] <= button_musicambient_y + button_musicambient_height):
                ambientcolor = button_hovergrey
            elif (button_musicbattle_x <= mouse[0] <= button_musicbattle_x + button_musicbattle_width and
                  button_musicbattle_y <= mouse[1] <= button_musicbattle_y + button_musicbattle_height):
                battlecolor = button_hovergrey

            pygame.draw.rect(win, orange, screen_outline)
            pygame.draw.rect(win, white, screen_rect)
            pygame.draw.rect(win, returncolor, button_return)
            pygame.draw.rect(win, ambientcolor, button_musicambient)
            pygame.draw.rect(win, battlecolor, button_musicbattle)

            returnImg = pygame.transform.scale(returnImg, (button_return_width, button_return_height))
            win.blit(returnImg, (button_return_x, button_return_y))

            win.blit(title_text, title_rect)
            # win.blit(return_text, return_rect)
            win.blit(musicType, musicType_rect)
            win.blit(ambient_text, ambient_rect)
            win.blit(battle_text, battle_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass
                    if (button_return_x <= mouse[0] <= button_return_x + button_return_width and
                            button_return_y <= mouse[1] <= button_return_y + button_return_height):
                        return
                    elif (button_musicambient_x <= mouse[0] <= button_musicambient_x + button_musicambient_width and
                          button_musicambient_y <= mouse[1] <= button_musicambient_y + button_musicambient_height):
                        switchAmbient()
                    elif (button_musicbattle_x <= mouse[0] <= button_musicbattle_x + button_musicbattle_width and
                          button_musicbattle_y <= mouse[1] <= button_musicbattle_y + button_musicbattle_height):
                        switchBattle()
                    #     if musicIsPaused:
                    #         musicIsPaused = False
                    #         unpause()
                    #     elif not musicIsPaused:
                    #         musicIsPaused = True
                    #         pause()
                    # elif (button_options_x <= mouse[0] <= button_options_x + button_options_width and
                    #         button_options_y <= mouse[1] <= button_options_y + button_options_height):
                    #     self.options()
            pygame.display.update(screen_outline)

    def gameLose(self):
        global p1
        inGameLose = True

		# lose = "The long-winded journey came to an abrupt end when the ability of a peasant demonstrated its true nature... nonexistent.. :( Nevertheless, your bravery to venture into these uncharted territories ill-equiped does not go unrecognized. This game was meant to give hope to all peasants; and I hope you will find the next game just as thrilling! Thank you and I hope to see you on your next adventure!!"
		
        # Images
        backgroundImg = pygame.image.load("icon/png/lose.png")
        backgroundImg = pygame.transform.scale(backgroundImg, (SCREENWIDTH, SCREENHEIGHT))
        # restartImg = pygame.image.load('icon/png/return.png')

        # Restart Button
        button_restart_x = SCREENWIDTH / 2
        button_restart_y = SCREENHEIGHT / 2 + 290
        button_restart_width = 100
        button_restart_height = 30
        button_restart = pygame.Rect(button_restart_x, button_restart_y, button_restart_width, button_restart_height)
        # restartImg = pygame.transform.scale(restartImg, (button_restart_width, button_restart_height))

        # Font/Text
        font = pygame.font.SysFont('Arial', 20)
        returntext = font.render("Restart", True, black)
        returntext_rect = returntext.get_rect(center=button_restart.center)

        # "Crash" Game over Screen
        screen_rect_x = 0
        screen_rect_y = 0
        screen_rect_width = SCREENWIDTH
        screen_rect_height = SCREENHEIGHT
        screen_rect = pygame.Rect(screen_rect_x, screen_rect_y, screen_rect_width, screen_rect_height)

        # Reset Player
        p1 = Player(win, 'normal', None, inventory, player_name, 0, 200, 100, max_health, Defense(), Utility.hand)

        while (inGameLose):
            mouse = pygame.mouse.get_pos()
            # Display
            pygame.draw.rect(win, (255, 255, 255, 20), screen_rect)
            win.blit(backgroundImg, (0, 0))
            pygame.draw.rect(win, white, button_restart)
            # win.blit(restartImg, (button_restart_x, button_restart_y))
            win.blit(returntext, returntext_rect)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if (button_restart_x <= mouse[0] <= button_restart_x + button_restart_width and
                            button_restart_y <= mouse[1] <= button_restart_y + button_restart_height):
                        self.mainMenu()

    def gameWin(self):
        global p1
        inGameWin = True

        # Images
        backgroundImg = pygame.image.load("icon/png/win-50.png")
        backgroundImg = pygame.transform.scale(backgroundImg, (SCREENWIDTH, SCREENHEIGHT))

        # "Crash" Game over Screen
        screen_rect_x = 0
        screen_rect_y = 0
        screen_rect_width = SCREENWIDTH
        screen_rect_height = SCREENHEIGHT
        screen_rect = pygame.Rect(screen_rect_x, screen_rect_y, screen_rect_width, screen_rect_height)

        # Reset Player
        p1 = Player(win, 'normal', None, inventory, player_name, 0, 200, 100, max_health, Defense(), Utility.hand)

        while inGameWin:
            mouse = pygame.mouse.get_pos()
            # Display
            pygame.draw.rect(win, (255, 255, 255, 20), screen_rect)
            win.blit(backgroundImg, (0,0))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit()

    def exit(self):
        isExiting = True

        outlineborder = 10

        screen_rect_x = 200
        screen_rect_y = 100
        screen_rect_width = 800
        screen_rect_height = 475
        screen_rect = pygame.Rect(screen_rect_x, screen_rect_y, screen_rect_width, screen_rect_height)

        screen_outline_x = screen_rect_x - outlineborder
        screen_outline_y = screen_rect_y - outlineborder
        screen_outline_width = screen_rect_width + 2 * outlineborder
        screen_outline_height = screen_rect_height + 2 * outlineborder
        screen_outline = pygame.Rect(screen_outline_x, screen_outline_y, screen_outline_width, screen_outline_height)

        font = pygame.font.SysFont('Comic Sans MS', 30)
        exit_text = font.render('Are you sure you wish to leave?', True, black)
        exit_rect = exit_text.get_rect(center=(round(screen_rect.center[0]), 250))

        button_yes_x = 300
        button_yes_y = 400
        button_yes_width = 250
        button_yes_height = 50
        button_yes = pygame.Rect(button_yes_x, button_yes_y, button_yes_width, button_yes_height)

        button_no_x = 650
        button_no_y = button_yes_y
        button_no_width = button_yes_width
        button_no_height = button_yes_height
        button_no = pygame.Rect(button_no_x, button_no_y, button_no_width, button_no_height)

        buttonfont = pygame.font.SysFont('Comic Sans MS', 40)
        yes_text = buttonfont.render('Exit', True, red)
        no_text = buttonfont.render('Cancel', True, green)
        yes_rect = yes_text.get_rect(center=(button_yes.center[0], button_yes.center[1]))
        no_rect = no_text.get_rect(center=(button_no.center[0], button_no.center[1]))

        while isExiting:
            yes_color = button_grey
            no_color = button_grey

            mouse = pygame.mouse.get_pos()

            pygame.draw.rect(win, lightblue, screen_outline)
            pygame.draw.rect(win, white, screen_rect)

            if (button_yes_x <= mouse[0] <= button_yes_x + button_yes_width and
                    button_yes_y <= mouse[1] <= button_yes_y + button_yes_height):
                yes_color = button_hovergrey
            elif (button_no_x <= mouse[0] <= button_no_x + button_no_width and
                  button_no_y <= mouse[1] <= button_no_y + button_no_height):
                no_color = button_hovergrey

            pygame.draw.rect(win, yes_color, button_yes)
            pygame.draw.rect(win, no_color, button_no)

            win.blit(exit_text, exit_rect)
            win.blit(yes_text, yes_rect)
            win.blit(no_text, no_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if (button_yes_x <= mouse[0] <= button_yes_x + button_yes_width and
                            button_yes_y <= mouse[1] <= button_yes_y + button_yes_height):
                        pygame.quit()
                        exit()
                    elif (button_no_x <= mouse[0] <= button_no_x + button_no_width and
                          button_no_y <= mouse[1] <= button_no_y + button_no_height):
                        return

            pygame.display.update(screen_outline)

    def displayExplore(self, scenario):
        if scenario == 1:
            pass
        elif scenario == 2:
            pass

    def display(self):
        pass


inventory = ['meat', 'meat']

p1 = Player(win, 'normal', None, inventory, player_name, 0, 250, 100, max_health, Defense(), Utility.hand)
m1 = Menu(win)

pygame.mixer.music.play(-1)
m1.mainMenu()

pygame.quit()
