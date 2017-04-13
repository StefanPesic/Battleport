from functions import *
import pygame_textinput
from pygame_textinput import *
import psycopg2


''''Database login'''
connection = psycopg2.connect(host= "localhost", database="postgres", user= "postgres", password="WallSpeaker5" )
connection.autocommit = True
cur = connection.cursor()



''''ALL VARIABLES USED AS GLOBALS'''
the_player_1 = ""
the_player_2 = ""



''''This decides which player is turn'''
player1 = True

''''Card grab'''
the_player1_grab = True
the_player2_grab = True

specialboat1grab = 1
specialboat2grab = 1
specialboat3grab = 1
specialboat4grab = 1
specialboat5grab = 1
specialboat6grab = 1
specialboat7grab = 1
specialboat8grab = 1
specialboat9grab = 1

''''Booleans to have the card activate'''
card1bol = False
card2bol = False
card3bol = False
card4bol = False
card5bol = False
card6bol = False
card7bol = False
card8bol = False
card9bol = False
card10bol = False
card11bol = False
card12bol = False

''''trigger to activate boat'''
boat1bol = False
boat2bol = False
boat3bol = False
boat4bol = False
boat5bol = False
boat6bol = False
boat7bol = False
boat8bol = False


def the_player2winner():
    global the_player_1

    pygame.display.set_caption("Players")
    screen2 = pygame.display.set_mode((display_width1, display_height1))
    pygame.display.update()

    ''''Background image'''
    the_image2000 = "player1winner.png"
    screen_image2000 = pygame.display.set_mode((display_width1, display_height1))
    menu_image2000 = pygame.image.load(the_image2000)
    screen_image2000.blit(menu_image2000, (0, 0))

    ''''Fonts'''
    pygame.display.set_caption("Font")
    my_font = pygame.font.Font(None, 150)
    thewinner1_font = my_font.render(str(the_player_2 ), 5, black)

    ''''Mouse'''
    (MouseX, MouseY) = pygame.mouse.get_pos()

    players = True
    while players == True:

        for events in pygame.event.get():
            screen2.blit(thewinner1_font, (380, 250))
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_SPACE:
                    the_menufunction()

            elif events.type == pygame.MOUSEBUTTONDOWN:
                print(MouseX, MouseY)
                print("Mouse Button up")
            elif events.type == pygame.MOUSEBUTTONUP:
                print(MouseX, MouseY)
                print("Mouse Button down")

            elif events.type == pygame.MOUSEMOTION:
                print("mouse at " + " " + str(MouseX) + " " + str(MouseY))

            (MouseX, MouseY) = pygame.mouse.get_pos()

        pygame.display.update()

def the_player1winner():
    global the_player_1

    pygame.display.set_caption("Players")
    screen2 = pygame.display.set_mode((display_width1, display_height1))
    pygame.display.update()

    ''''Background image'''
    the_image2000 = "player1winner.png"
    screen_image2000 = pygame.display.set_mode((display_width1, display_height1))
    menu_image2000 = pygame.image.load(the_image2000)
    screen_image2000.blit(menu_image2000, (0, 0))


    ''''Fonts'''
    pygame.display.set_caption("Font")
    my_font = pygame.font.Font(None, 150)
    thewinner1_font = my_font.render(str(the_player_1), 5, black)




    ''''Mouse'''
    (MouseX, MouseY) = pygame.mouse.get_pos()

    players = True
    while players == True:


        for events in pygame.event.get():
            screen2.blit(thewinner1_font, (380, 250))
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_SPACE:
                    the_menufunction()

            elif events.type == pygame.MOUSEBUTTONDOWN:
                print(MouseX, MouseY)
                print("Mouse Button up")
            elif events.type == pygame.MOUSEBUTTONUP:
                print(MouseX, MouseY)
                print("Mouse Button down")

            elif events.type == pygame.MOUSEMOTION:
                print("mouse at " + " " + str(MouseX) + " " + str(MouseY))

            (MouseX, MouseY) = pygame.mouse.get_pos()

        pygame.display.update()



def the_gamefunction():
    global the_player_1
    global the_player_2
    global boat1bol
    global boat2bol
    global boat3bol
    global boat4bol
    global boat5bol
    global boat6bol
    global boat7bol
    global boat8bol
    global card1bol
    global card2bol
    global card3bol
    global card4bol
    global card5bol
    global card6bol
    global card7bol
    global card8bol
    global card9bol
    global card10bol
    global card11bol
    global card12bol
    global specialboat1grab
    global specialboat2grab
    global specialboat3grab
    global specialboat4grab
    global specialboat5grab
    global specialboat6grab
    global specialboat7grab
    global specialboat8grab
    global specialboat9grab
    global player1
    global the_player1_grab
    global the_player2_grab

    ''''FPS'''
    clock(60)


    ''''Music'''
    ''''GAME THEME'''
    pygame.mixer.music.load("goldberg.wav")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.4)

    ''''Canvas'''
    pygame.display.set_caption("Game")
    screen = pygame.display.set_mode((display_width1 , display_height1))
    pygame.display.update()

    the_image = "the_final_map.png"
    screen_image = pygame.display.set_mode((display_width1, display_height1), pygame.FULLSCREEN)
    menu_image =  pygame.image.load(the_image)
    screen_image.blit(menu_image,(0,0))

    ''''Sound effects'''
    effect1 = pygame.mixer.Sound('player_1.wav')
    effect2 = pygame.mixer.Sound('player_2.wav')
    effect3 = pygame.mixer.Sound('card_1.wav')
    effect4 = pygame.mixer.Sound('card_2.wav')
    effect5 = pygame.mixer.Sound('card_3.wav')
    effect6 = pygame.mixer.Sound('card_4.wav')
    effect7 = pygame.mixer.Sound('card_5.wav')
    effect8 = pygame.mixer.Sound('card_6.wav')
    effect9 = pygame.mixer.Sound('card_grab.wav')
    effect10 = pygame.mixer.Sound('card_limit_is_6.wav')
    effect11 = pygame.mixer.Sound('not_allowed.wav')
    effect12 = pygame.mixer.Sound('one_card_per_turn.wav')
    effect13 = pygame.mixer.Sound('special_card_1.wav')
    effect14 = pygame.mixer.Sound('special_card_2.wav')
    effect15 = pygame.mixer.Sound('special_card_3.wav')
    effect16 = pygame.mixer.Sound('special_card_4.wav')
    effect17 = pygame.mixer.Sound('special_card_available.wav')
    effect19 = pygame.mixer.Sound('boat_destroyed.wav')

    ''''Players image'''
    menu_image30 = pygame.image.load('player1_logo.png')
    menu_image31 = pygame.image.load('player2_logo.png')

    ''''Player stats'''
    menu_image32 = pygame.image.load('player1_stats.png')
    menu_image33 = pygame.image.load('player2_stats.png')

    ''''Background below player'''
    menu_image34 = pygame.image.load('below_players.png')

    ''''Fonts'''
    pygame.display.set_caption("Font")
    my_font = pygame.font.Font(None,50)
    my_font1 =  pygame.font.Font(None,39)


    class the_player_class:
        def __init__(self, name):
            self.Name = name
            self.score = 0
    player1winner = the_player_class(the_player_1)
    player2winner = the_player_class(the_player_2)


    ''''X,Y offensive range'''''
    class the_offensive_range:
        def __init__(self, rangeX, rangeY):
            self.rangeX = rangeX
            self.rangeY = rangeY

    ''''Defensive Range'''
    class the_defensive_range:
        def __init__(self, therangeY):
            self.therangeY = therangeY

    ''''Coordinate to track boat'''
    class coordinate:
        def __init__(self, corX, corY):
            self.corX = corX
            self.corY = corY

    ''''step tracker'''
    class steps:
        def __init__(self, maxsteps):
            self.steps = 0
            self.Maxsteps = maxsteps
        def stepadd(self):
          if self.steps <= self.Maxsteps - 1:
                return True
          else:
              return False
        def stepreset(self):
            self.steps = 0


    ''''boat class attributes and card methods'''
    class boat:
        def __init__(self, health, offensive_rangeX, offensive_rangeY, defensive_rangeY, the_corX, the_corY, the_maxsteps):
            self.health = health
            self.offensive_range = the_offensive_range(offensive_rangeX, offensive_rangeY)
            self.defensive_range = the_defensive_range(defensive_rangeY)
            self.damage = 1
            self.offensive_rangebol = True
            self.defensive_rangebol = False
            self.thecoordinate = coordinate(the_corX, the_corY)
            self.maxsteps = steps(the_maxsteps)
        def fmj_upgrade(self):
            self.damage = self.damage + 1
        def rifling(self):
            if self.offensive_rangebol == True:
                self.offensive_range.rangeX = self.offensive_range.rangeX + 1
                self.offensive_range.rangeY = self.offensive_range.rangeY + 1
            else:
                self.defensive_range.therangeY = self.defensive_range.therangeY + 1
        def advanced_rifling(self):
            if self.offensive_rangebol == True:
                self.offensive_range.rangeX = self.offensive_range.rangeX + 2
                self.offensive_range.rangeY = self.offensive_range.rangeY + 2
            else:
                self.defensive_range.therangeY = self.defensive_range.therangeY + 2
        ''''Defensive cards'''
        def reinforced_hull(self):
            self.health = self.health + 1
        ''''Help cards'''
        def extra_fuel(self):
            self.maxsteps.Maxsteps = self.maxsteps.Maxsteps + 2
        def rally(self):
            self.maxsteps.Maxsteps = self.maxsteps.Maxsteps + 1
        def andrenaline_rush(self):
            self.maxsteps.Maxsteps = self.maxsteps.Maxsteps * 2
        ''''special cards'''
        def repair(self):
            self.health = self.health + 4
        def flak_armor(self):
            self.health = self.health + 2
        def far_sight(self):
            if self.offensive_rangebol == True:
                self.offensive_range.rangeX = self.offensive_range.rangeX + 2
                self.offensive_range.rangeY = self.offensive_range.rangeY + 2
            else:
                self.defensive_range.therangeY = self.defensive_range.therangeY + 2
        def aluminum_hull(self):
            if self.offensive_rangebol == True:
                self.offensive_range.rangeX = self.offensive_range.rangeX + 1
                self.offensive_range.rangeY = self.offensive_range.rangeY + 1
            else:
                self.defensive_range.therangeY = self.defensive_range.therangeY + 1


    "Player 1 boats"
    fungo_saltire = boat(2, 2,2,3, None, None, 3)
    silver_whisper = boat(3,3,3,4,None, None, 2)
    sea_spirit = boat(3,3,3,4,None, None, 2)
    merapi = boat(4,4,4,5,None, None, 1)

    ''''Player 2 boats'''
    santa_bettina = boat(2, 2,2,3, None, None, 3)
    windsurf = boat(3,3,3,4,None, None, 2)
    intensity = boat(3,3,3,4,None, None, 2)
    amadea = boat(4,4,4,5,None, None, 1)




    ''''Mouse'''
    (MouseX, MouseY) = pygame.mouse.get_pos()



    ''''Special card grab'''
    specialboat1 = False
    specialboat2 = False
    specialboat3 = False
    specialboat4 = False
    specialboat5 = False
    specialboat6 = False
    specialboat7 = False
    specialboat8 = False



    ''''Sound to have the special card sound available only once'''
    sb1 = 1
    sb2 = 1
    sb3 = 1
    sb4 = 1
    sb5 = 1
    sb6 = 1
    sb7 = 1
    sb8 = 1

    #TODO add sound effect when attack, only have attack once turn per boat
    #TODO fix attacks for other boats too
    #TODO ADD BOAT ROTATION


    ''''Enemy trigger for attack'''
    boat1_trigger = False
    boat2_trigger = False
    boat3_trigger = False
    boat4_trigger = False
    boat5_trigger = False
    boat6_trigger = False
    boat7_trigger = False
    boat8_trigger = False

    ''''for the one attack per turn'''
    boat1_attack_turn = True
    boat2_attack_turn = True
    boat3_attack_turn = True
    boat4_attack_turn = True
    boat5_attack_turn = True
    boat6_attack_turn = True
    boat7_attack_turn = True
    boat8_attack_turn = True



    ''''The click and their decisions'''
    def the_map_click(posx,posy):
        if posx > menu_title.beginX and posx < menu_title.endX and posy > menu_title.beginY and posy < menu_title.endY:
            print("Menu")
            if events.type == pygame.MOUSEBUTTONDOWN and events.button == 1:
                pygame.mixer.music.stop()
                the_menufunction()

        elif posx > endturn_title.beginX and posx < endturn_title.endX and posy > endturn_title.beginY and posy < endturn_title.endY:
            if events.type == pygame.MOUSEBUTTONDOWN and events.button == 1:
                global player1
                global the_player1_grab
                global the_player2_grab
                if player1 == True:
                    player1 = False
                    the_player1_grab = True
                    effect2.play()

                elif player1 == False:
                    player1 = True
                    the_player2_grab = True
                    effect1.play()


        elif posx > nordeck_title.beginX and posx < nordeck_title.endX and posy > nordeck_title.beginY and posy < nordeck_title.endY:
            if events.type == pygame.MOUSEBUTTONDOWN and events.button == 1:
                if player1 == True and the_player1_grab == False:
                    effect12.play()
                elif player1 == True and the_player1_grab == True:
                    if len(player1_normalcards) < 7:
                        for key in normal_card_deck:
                            if key == random_normal_deck:
                                player1_normalcards.append(normal_card_deck[key])
                                effect9.play()
                                the_player1_grab = False

                if player1 == False and the_player2_grab == False :
                    effect12.play()
                elif player1 == False and the_player2_grab == True:
                    if len(player2_normalcards) < 7:
                        for key in normal_card_deck:
                            if key == random_normal_deck:
                                player2_normalcards.append(normal_card_deck[key])
                                effect9.play()
                                the_player2_grab = False

        elif posx > spcdeck_title.beginX and posx < spcdeck_title.endX and posy > spcdeck_title.beginY and posy < spcdeck_title.endY:
            global specialboat1grab
            global specialboat2grab
            global specialboat3grab
            global specialboat4grab
            global specialboat5grab
            global specialboat6grab
            global specialboat7grab
            global specialboat8grab

            if events.type == pygame.MOUSEBUTTONDOWN and events.button == 1:
                if player1 == True and specialboat1 == True and specialboat1grab == 1:
                    if len(player1_trapcards) < 5:
                        for key in special_card_deck:
                            if key == special_normal_deck:
                                player1_trapcards.append(special_card_deck[key])
                                specialboat1grab = 0
                                effect9.play()


                elif player1 == True and specialboat2 == True and specialboat2grab == 1:
                    if len(player1_trapcards) < 5:
                        for key in special_card_deck:
                            if key == special_normal_deck:
                                player1_trapcards.append(special_card_deck[key])
                                specialboat2grab = 0
                                effect9.play()

                elif player1 == True and specialboat3 == True and specialboat3grab == 1:
                    if len(player1_trapcards) < 5:
                        for key in special_card_deck:
                            if key == special_normal_deck:
                                player1_trapcards.append(special_card_deck[key])
                                specialboat3grab = 0
                                effect9.play()


                elif player1 == True and specialboat4 == True and specialboat4grab == 1:
                    if len(player1_trapcards) < 5:
                        for key in special_card_deck:
                            if key == special_normal_deck:
                                player1_trapcards.append(special_card_deck[key])
                                specialboat4grab = 0
                                effect9.play()


                elif player1 == False and specialboat5 == True and specialboat5grab == 1:
                    if len(player2_trapcards) < 5:
                        for key in special_card_deck:
                            if key == special_normal_deck:
                                player2_trapcards.append(special_card_deck[key])
                                specialboat5grab = 0
                                effect9.play()

                elif player1 == False and specialboat6 == True and specialboat6grab == 1:
                    if len(player2_trapcards) < 5:
                        for key in special_card_deck:
                            if key == special_normal_deck:
                                player2_trapcards.append(special_card_deck[key])
                                specialboat6grab = 0
                                effect9.play()

                elif player1 == False and specialboat7 == True and specialboat7grab == 1:
                    if len(player2_trapcards) < 5:
                        for key in special_card_deck:
                            if key == special_normal_deck:
                                player2_trapcards.append(special_card_deck[key])
                                specialboat7grab = 0
                                effect9.play()

                elif player1 == False and specialboat8 == True and specialboat8grab == 1:
                    if len(player2_trapcards) < 5:
                        for key in special_card_deck:
                            if key == special_normal_deck:
                                player2_trapcards.append(special_card_deck[key])
                                specialboat8grab = 0
                                effect9.play()

                else:
                    effect11.play()





        elif posx > playerhead_title.beginX and posx < playerhead_title.endX and posy > playerhead_title.beginY and posy < playerhead_title.endY: pass




    ''''Links methods to images'''
    def card_show(list):
        global card1bol
        global card2bol
        global card3bol
        global card4bol
        global card5bol
        global card6bol
        global card7bol
        global card8bol
        global card9bol
        global card10bol
        global card11bol
        global card12bol

        if list == "fmj_upgrade":
            menu_image20 = pygame.image.load('fmj_upgrade.png')
            screen.blit(menu_image20, (display_width1 * 0.769, display_height1 * 0.4276))
            card1bol = True
            card2bol = False
            card3bol = False
            card4bol = False
            card5bol = False
            card6bol = False
            card7bol = False
            card8bol = False
            card9bol = False
            card10bol = False
            card11bol = False
            card12bol = False

        elif list == "rifling":
            menu_image22 = pygame.image.load('rifling.png')
            screen.blit(menu_image22, (display_width1 * 0.769, display_height1 * 0.4276))
            card1bol = False
            card2bol = True
            card3bol = False
            card4bol = False
            card5bol = False
            card6bol = False
            card7bol = False
            card8bol = False
            card9bol = False
            card10bol = False
            card11bol = False
            card12bol = False

        elif list == "advanced_rifling":
            menu_image18 = pygame.image.load("rifling_plus.png")
            screen.blit(menu_image18, (display_width1 * 0.769, display_height1 * 0.4276))
            card1bol = False
            card2bol = False
            card3bol = True
            card4bol = False
            card5bol = False
            card6bol = False
            card7bol = False
            card8bol = False
            card9bol = False
            card10bol = False
            card11bol = False
            card12bol = False

        elif list == "reinforced_hull":
            menu_image10 = pygame.image.load("reinforced_hull.png")
            screen.blit(menu_image10, (display_width1 * 0.769, display_height1 * 0.4276))
            card1bol = False
            card2bol = False
            card3bol = False
            card4bol = True
            card5bol = False
            card6bol = False
            card7bol = False
            card8bol = False
            card9bol = False
            card10bol = False
            card11bol = False
            card12bol = False


        elif list == "backup":
            menu_image15 = pygame.image.load("backup.png")
            screen.blit(menu_image15, (display_width1 * 0.769, display_height1 * 0.4276))
            card1bol = False
            card2bol = False
            card3bol = False
            card4bol = False
            card5bol = True
            card6bol = False
            card7bol = False
            card8bol = False
            card9bol = False
            card10bol = False
            card11bol = False
            card12bol = False


        elif list == "extra_fuel":
            menu_image16 = pygame.image.load("extra_fuel.png")
            screen.blit(menu_image16, (display_width1 * 0.769, display_height1 * 0.4276))
            card1bol = False
            card2bol = False
            card3bol = False
            card4bol = False
            card5bol = False
            card6bol = True
            card7bol = False
            card8bol = False
            card9bol = False
            card10bol = False
            card11bol = False
            card12bol = False

        elif list == "rally":
            menu_image17 = pygame.image.load("rally.png")
            screen.blit(menu_image17, (display_width1 * 0.769, display_height1 * 0.4276))

            card1bol = False
            card2bol = False
            card3bol = False
            card4bol = False
            card5bol = False
            card6bol = False
            card7bol = True
            card8bol = False
            card9bol = False
            card10bol = False
            card11bol = False
            card12bol = False

        elif list == "andrenaline_rush":
            menu_image14 = pygame.image.load("adrenaline_rush.png")
            screen.blit(menu_image14, (display_width1 * 0.769, display_height1 * 0.4276))

            card1bol = False
            card2bol = False
            card3bol = False
            card4bol = False
            card5bol = False
            card6bol = False
            card7bol = False
            card8bol = True
            card9bol = False
            card10bol = False
            card11bol = False
            card12bol = False

        elif list == "repair":
            menu_image28 = pygame.image.load('repair.png')
            screen.blit(menu_image28, (display_width1 * 0.769, display_height1 * 0.4276))

            card1bol = False
            card2bol = False
            card3bol = False
            card4bol = False
            card5bol = False
            card6bol = False
            card7bol = False
            card8bol = False
            card9bol = True
            card10bol = False
            card11bol = False
            card12bol = False

        elif list == "flak_armor":
            menu_image25 = pygame.image.load('flake_armor.png')
            screen.blit(menu_image25, (display_width1 * 0.769, display_height1 * 0.4276))

            card1bol = False
            card2bol = False
            card3bol = False
            card4bol = False
            card5bol = False
            card6bol = False
            card7bol = False
            card8bol = False
            card9bol = False
            card10bol = True
            card11bol = False
            card12bol = False

        elif list == "far_sight":
            menu_image24 = pygame.image.load('far_sight.png')
            screen.blit(menu_image24, (display_width1 * 0.769, display_height1 * 0.4276))

            card1bol = False
            card2bol = False
            card3bol = False
            card4bol = False
            card5bol = False
            card6bol = False
            card7bol = False
            card8bol = False
            card9bol = False
            card10bol = False
            card11bol = True
            card12bol = False

        elif list == "aluminum_hull":
            menu_image23 = pygame.image.load('aluminum_hull.png')
            screen.blit(menu_image23, (display_width1 * 0.769, display_height1 * 0.4276))

            card1bol = False
            card2bol = False
            card3bol = False
            card4bol = False
            card5bol = False
            card6bol = False
            card7bol = False
            card8bol = False
            card9bol = False
            card10bol = False
            card11bol = False
            card12bol = True

        else:
            menu_image29 = pygame.image.load('empty_card.png')
            screen.blit(menu_image29, (display_width1 * 0.769, display_height1 * 0.4276))

    '''''The card decks'''
    normal_card_deck = {1: "fmj_upgrade", 2: "rifling", 3: "advanced_rifling", 4: "reinforced_hull",  5:
    "backup", 6: "extra_fuel", 7: "rally", 8: "andrenaline_rush"}

    special_card_deck = {1: "repair", 2: "flak_armor", 3: "far_sight", 4:
    "aluminum_hull"}

    '''''User Cards'''
    player1_normalcards = []
    player2_normalcards = []
    player1_trapcards = []
    player2_trapcards = []


    ''''boat images'''
    theboat1 =  pygame.image.load("p1boat_2square.png")
    theboat2 =  pygame.image.load("p1boat_2square.png")
    theboat3 =  pygame.image.load("p1boat_3square.png")
    theboat4 =  pygame.image.load("p1boat_4square.png")

    theboat5 =  pygame.image.load("p2boat_2square.png")
    theboat6 =  pygame.image.load("p2boat_3square.png")
    theboat7 =  pygame.image.load("p2boat_3square.png")
    theboat8 =  pygame.image.load("p2boat_4square.png")


    ''''Scale'''
    class boat_movement:
        def __init__(self, aleadx, aleady):
            self.leadx = aleadx
            self.leady = aleady

    aboat1 = boat_movement(display_width1 * 0.309, display_height1 * 0.867)
    aboat2 = boat_movement(display_width1 * 0.518, display_height1 * 0.867)
    aboat3 = boat_movement(display_width1 * 0.101, display_height1 * 0.824)
    aboat4 = boat_movement(display_width1 * 0.22, display_height1 * 0.781)

    aboat5 = boat_movement(display_width1 * 0.6083, display_height1 * 0.087)
    aboat6 = boat_movement(display_width1 * 0.488, display_height1 * 0.087)
    aboat7 = boat_movement(display_width1 * 0.2198, display_height1 * 0.087)
    aboat8 = boat_movement(display_width1 * 0.3985, display_height1 * 0.087)



    aboat11 = pygame.transform.rotate(theboat1, 0)
    aboat12 = pygame.transform.rotate(theboat1, 0)
    aboat13 = pygame.transform.rotate(theboat3, 0)
    aboat14 = pygame.transform.rotate(theboat4, 0)
    aboat15 = pygame.transform.rotate(theboat5, 0)
    aboat16 = pygame.transform.rotate(theboat6, 0)
    aboat17 = pygame.transform.rotate(theboat7, 0)
    aboat18 = pygame.transform.rotate(theboat8, 0)

    boat1dead = 1
    boat2dead = 1
    boat3dead = 1
    boat4dead = 1
    boat5dead = 1
    boat6dead = 1
    boat7dead = 1
    boat8dead = 1



    #TODO have p2 also the choice to activate a card
    ''''Card activation'''
    def activate_card():
        global the_player1_grab
        global the_player2_grab
        global boat1bol
        global boat2bol
        global boat3bol
        global boat4bol
        global boat5bol
        global boat6bol
        global boat7bol
        global boat8bol

        if card5bol == True:
            if player1 == True:
                if "backup" in player1_normalcards:
                    player1_normalcards.remove("backup")
                    the_player1_grab = True
            elif player1 == False:
                if "backup" in player2_normalcards:
                    player2_normalcards.remove("backup")
                    the_player2_grab = True
        if player1 == True:
            if boat1bol == True:
                if card1bol == True:
                    if "fmj_upgrade" in player1_normalcards:
                        player1_normalcards.remove("fmj_upgrade")
                        return getattr(fungo_saltire, "fmj_upgrade")()
                elif card2bol == True:
                    if "rifling" in player1_normalcards:
                        player1_normalcards.remove("rifling")
                        return getattr(fungo_saltire, "rifling")()
                elif card3bol == True:
                    if "advanced_rifling" in player1_normalcards:
                        player1_normalcards.remove("advanced_rifling")
                        return getattr(fungo_saltire, "advanced_rifling")()
                elif card4bol == True:
                    if "reinforced_hull" in player1_normalcards:
                        player1_normalcards.remove("reinforced_hull")
                        return getattr(fungo_saltire, "reinforced_hull")()
                elif card6bol == True:
                    if "extra_fuel" in player1_normalcards:
                        player1_normalcards.remove("extra_fuel")
                        return getattr(fungo_saltire, "extra_fuel")()
                elif card7bol == True:
                    if "rally" in player1_normalcards:
                        player1_normalcards.remove("rally")
                        return getattr(fungo_saltire, "rally")()
                elif card8bol == True:
                    if "andrenaline_rush" in player1_normalcards:
                        player1_normalcards.remove("andrenaline_rush")
                        return getattr(fungo_saltire, "andrenaline_rush")()
                    #trapcards
                elif card9bol == True:
                    if "repair" in player1_trapcards:
                        player1_trapcards.remove("repair")
                        return getattr(fungo_saltire, "repair")()
                elif card10bol == True:
                    if "flak_armor" in player1_trapcards:
                        player1_trapcards.remove("flak_armor")
                        return getattr(fungo_saltire, "flak_armor")()
                elif card11bol == True:
                    if "far_sight" in player1_trapcards:
                        player1_trapcards.remove("far_sight")
                        return getattr(fungo_saltire, "far_sight")()
                elif card12bol == True:
                    if "aluminum_hull" in player1_trapcards:
                        player1_trapcards.remove("aluminum_hull")
                        return getattr(fungo_saltire, "aluminum_hull")()
            elif boat2bol == True:
                if card1bol == True:
                    if "fmj_upgrade" in player1_normalcards:
                        player1_normalcards.remove("fmj_upgrade")
                        return getattr(silver_whisper, "fmj_upgrade")()
                elif card2bol == True:
                    if "rifling" in player1_normalcards:
                        player1_normalcards.remove("rifling")
                    return getattr(silver_whisper, "rifling")()
                elif card3bol == True:
                    if "advanced_rifling" in player1_normalcards:
                        player1_normalcards.remove("advanced_rifling")
                        return getattr(silver_whisper, "advanced_rifling")()
                elif card4bol == True:
                    if "reinforced_hull" in player1_normalcards:
                        player1_normalcards.remove("reinforced_hull")
                        return getattr(silver_whisper, "reinforced_hull")()

                elif card6bol == True:
                    if "extra_fuel" in player1_normalcards:
                        player1_normalcards.remove("extra_fuel")
                        return getattr(silver_whisper, "extra_fuel")()
                elif card7bol == True:
                    if  "rally" in player1_normalcards:
                        player1_normalcards.remove( "rally")
                        return getattr(silver_whisper, "rally")()
                elif card8bol == True:
                    if  "andrenaline_rush" in player1_normalcards:
                        player1_normalcards.remove( "andrenaline_rush")
                        return getattr(silver_whisper, "andrenaline_rush")()
                elif card9bol == True:
                    if "repair" in player1_trapcards:
                        player1_trapcards.remove("repair")
                        return getattr(silver_whisper, "repair")()
                elif card10bol == True:
                    if "flak_armor" in player1_trapcards:
                        player1_trapcards.remove("flak_armor")
                        return getattr(silver_whisper, "flak_armor")()
                elif card11bol == True:
                    if "far_sight" in player1_trapcards:
                        player1_trapcards.remove("far_sight")
                        return getattr(silver_whisper, "far_sight")()
                elif card12bol == True:
                    if "aluminum_hull" in player1_trapcards:
                        player1_trapcards.remove("aluminum_hull")
                        return getattr(silver_whisper, "aluminum_hull")()
            elif boat3bol == True:
                if card1bol == True:
                    if "fmj_upgrade" in player1_normalcards:
                        player1_normalcards.remove("fmj_upgrade")
                        return getattr(sea_spirit, "fmj_upgrade")()
                elif card2bol == True:
                    if "rifling" in player1_normalcards:
                        player1_normalcards.remove("rifling")
                        return getattr(sea_spirit, "rifling")()
                elif card3bol == True:
                    if "advanced_rifling" in player1_normalcards:
                        player1_normalcards.remove("advanced_rifling")
                        return getattr(sea_spirit, "advanced_rifling")()
                elif card4bol == True:
                    if "reinforced_hull" in player1_normalcards:
                        player1_normalcards.remove("reinforced_hull")
                        return getattr(sea_spirit, "reinforced_hull")()
                elif card6bol == True:
                    if  "extra_fuel" in player1_normalcards:
                         player1_normalcards.remove( "extra_fuel")
                         return getattr(sea_spirit, "extra_fuel")()
                elif card7bol == True:
                    if "rally" in player1_normalcards:
                        player1_normalcards.remove("rally")
                        return getattr(sea_spirit, "rally")()
                elif card8bol == True:
                    if "rally" in player1_normalcards:
                        player1_normalcards.remove("rally")
                        return getattr(sea_spirit, "andrenaline_rush")()
                elif card9bol == True:
                    if "repair" in player1_trapcards:
                        player1_trapcards.remove("repair")
                        return getattr(sea_spirit, "repair")()
                elif card10bol == True:
                    if "flak_armor" in player1_trapcards:
                        player1_trapcards.remove("flak_armor")
                        return getattr(sea_spirit, "flak_armor")()
                elif card11bol == True:
                    if  "far_sight" in player1_trapcards:
                        player1_trapcards.remove( "far_sight")
                        return getattr(sea_spirit, "far_sight")()
                elif card12bol == True:
                    if "aluminum_hull" in player1_trapcards:
                        player1_trapcards.remove("aluminum_hull")
                        return getattr(sea_spirit, "aluminum_hull")()
            elif the_player1_grab == True:
                if card1bol == True:
                    if "fmj_upgrade" in player1_normalcards:
                        player1_normalcards.remove("fmj_upgrade")
                        return getattr(merapi, "fmj_upgrade")()
                elif card2bol == True:
                    if "rifling" in player1_normalcards:
                        player1_normalcards.remove("rifling")
                        return getattr(merapi, "rifling")()
                elif card3bol == True:
                    if "advanced_rifling" in player1_normalcards:
                        player1_normalcards.remove("advanced_rifling")
                        return getattr(merapi, "advanced_rifling")()
                elif card4bol == True:
                    if  "reinforced_hull" in player1_normalcards:
                        player1_normalcards.remove( "reinforced_hull")
                        return getattr(merapi, "reinforced_hull")()
                elif card6bol == True:
                    if "extra_fuel" in player1_normalcards:
                        player1_normalcards.remove("extra_fuel")
                        return getattr(merapi, "extra_fuel")()
                elif card7bol == True:
                    if  "rally" in player1_normalcards:
                        player1_normalcards.remove( "rally")
                        return getattr(merapi, "rally")()
                elif card8bol == True:
                    if "andrenaline_rush" in player1_normalcards:
                        player1_normalcards.remove("andrenaline_rush")
                        return getattr(merapi, "andrenaline_rush")()
                elif card9bol == True:
                    if "repair" in player1_trapcards:
                        player1_trapcards.remove("repair")
                        return getattr(merapi, "repair")()
                elif card10bol == True:
                    if "flak_armor" in player1_trapcards:
                        player1_trapcards.remove("flak_armor")
                        return getattr(merapi, "flak_armor")()
                elif card11bol == True:
                    if "far_sight"in player1_trapcards:
                        player1_trapcards.remove("far_sight")
                        return getattr(merapi, "far_sight")()
                elif card12bol == True:
                    if  "aluminum_hull" in player1_trapcards:
                        player1_trapcards.remove( "aluminum_hull")
                        return getattr(merapi, "aluminum_hull")()
            elif boat5bol == True:
                if card1bol == True:
                    if "fmj_upgrade" in player1_normalcards:
                        player1_normalcards.remove("fmj_upgrade")
                        return getattr(santa_bettina, "fmj_upgrade")()
                elif card2bol == True:
                    if "rifling" in player1_normalcards:
                        player1_normalcards.remove("rifling")
                        return getattr(santa_bettina, "rifling")()
                elif card3bol == True:
                    if "advanced_rifling" in player1_normalcards:
                        player1_normalcards.remove("advanced_rifling")
                        return getattr(santa_bettina, "advanced_rifling")()
                elif card4bol == True:
                    if "reinforced_hull" in player1_normalcards:
                        player1_normalcards.remove("reinforced_hull")
                        return getattr(santa_bettina, "reinforced_hull")()
                elif card6bol == True:
                    if "extra_fuel" in player1_normalcards:
                        player1_normalcards.remove("extra_fuel")
                        return getattr(santa_bettina, "extra_fuel")()
                elif card7bol == True:
                    if "extra_fuel" in player1_normalcards:
                        player1_normalcards.remove("extra_fuel")
                        return getattr(santa_bettina, "rally")()
                elif card8bol == True:
                    if  "andrenaline_rush" in player1_normalcards:
                        player1_normalcards.remove( "andrenaline_rush")
                        return getattr(santa_bettina, "andrenaline_rush")()
                elif card9bol == True:
                    if "repair" in player1_trapcards:
                        player1_trapcards.remove("repair")
                        return getattr(santa_bettina, "repair")()
                elif card10bol == True:
                    if "flak_armor" in player1_trapcards:
                        player1_trapcards.remove("flak_armor")
                        return getattr(santa_bettina, "flak_armor")()
                elif card11bol == True:
                    if "far_sight" in player1_trapcards:
                        player1_trapcards.remove("far_sight")
                        return getattr(santa_bettina, "far_sight")()
                elif card12bol == True:
                    if "aluminum_hull" in player1_trapcards:
                        player1_trapcards.remove("aluminum_hull")
                        return getattr(santa_bettina, "aluminum_hull")()
            elif boat6bol == True:
                if card1bol == True:
                    if "fmj_upgrade" in player1_normalcards:
                        player1_normalcards.remove("fmj_upgrade")
                        return getattr(windsurf, "fmj_upgrade")()
                elif card2bol == True:
                    if "rifling" in player1_normalcards:
                        player1_normalcards.remove("rifling")
                        return getattr(windsurf, "rifling")()
                elif card3bol == True:
                    if "advanced_rifling" in player1_normalcards:
                        player1_normalcards.remove("advanced_rifling")
                        return getattr(windsurf, "advanced_rifling")()
                elif card4bol == True:
                    if "reinforced_hull" in player1_normalcards:
                        player1_normalcards.remove("reinforced_hull")
                        return getattr(windsurf, "reinforced_hull")()
                elif card6bol == True:
                    if "extra_fuel" in player1_normalcards:
                        player1_normalcards.remove("extra_fuel")
                        return getattr(windsurf, "extra_fuel")()
                elif card7bol == True:
                    if "rally" in player1_normalcards:
                        player1_normalcards.remove("rally")
                        return getattr(windsurf, "rally")()
                elif card8bol == True:
                    if "andrenaline_rush" in player1_normalcards:
                        player1_normalcards.remove("andrenaline_rush")
                        return getattr(windsurf, "andrenaline_rush")()
                elif card9bol == True:
                    if "repair" in player1_trapcards:
                        player1_trapcards.remove("repair")
                        return getattr(windsurf, "repair")()
                elif card10bol == True:
                    if "flak_armor" in player1_trapcards:
                        player1_trapcards.remove("flak_armor")
                        return getattr(windsurf, "flak_armor")()
                elif card11bol == True:
                    if "far_sight" in player1_trapcards:
                        player1_trapcards.remove("far_sight")
                        return getattr(windsurf, "far_sight")()
                elif card12bol == True:
                    if "aluminum_hull" in player1_trapcards:
                        player1_trapcards.remove("aluminum_hull")
                        return getattr(windsurf, "aluminum_hull")()
            elif boat7bol == True:
                if card1bol == True:
                    if "fmj_upgrade" in player1_normalcards:
                        player1_normalcards.remove("fmj_upgrade")
                        return getattr(intensity, "fmj_upgrade")()
                elif card2bol == True:
                    if "rifling" in player1_normalcards:
                        player1_normalcards.remove( "rifling")
                        return getattr(intensity, "rifling")()
                elif card3bol == True:
                    if "advanced_rifling" in player1_normalcards:
                        player1_normalcards.remove("advanced_rifling")
                        return getattr(intensity, "advanced_rifling")()
                elif card4bol == True:
                    if "reinforced_hull" in player1_normalcards:
                        player1_normalcards.remove("reinforced_hull")
                        return getattr(intensity, "reinforced_hull")()
                elif card6bol == True:
                    if "extra_fuel" in player1_normalcards:
                        player1_normalcards.remove("extra_fuel")
                        return getattr(intensity, "extra_fuel")()
                elif card7bol == True:
                    if "rally" in player1_normalcards:
                        player1_normalcards.remove("rally")
                        return getattr(intensity, "rally")()
                elif card8bol == True:
                    if "andrenaline_rush" in player1_normalcards:
                        player1_normalcards.remove("andrenaline_rush")
                        return getattr(intensity, "andrenaline_rush")()
                elif card9bol == True:
                    if "repair" in player1_trapcards:
                        player1_trapcards.remove("repair")
                        return getattr(intensity, "repair")()
                elif card10bol == True:
                    if "flak_armor" in player1_trapcards:
                        player1_trapcards.remove("flak_armor")
                        return getattr(intensity, "flak_armor")()
                elif card11bol == True:
                    if "far_sight" in player1_trapcards:
                        player1_trapcards.remove("far_sight")
                        return getattr(intensity, "far_sight")()
                elif card12bol == True:
                    if "aluminum_hull" in player1_trapcards:
                        player1_trapcards.remove("aluminum_hull")
                        return getattr(intensity, "aluminum_hull")()
            elif boat8bol == True:
                if card1bol == True:
                    if "fmj_upgrade" in player1_normalcards:
                        player1_normalcards.remove("fmj_upgrade")
                        return getattr(amadea, "fmj_upgrade")()
                elif card2bol == True:
                    if "rifling" in player1_normalcards:
                        player1_normalcards.remove("rifling")
                        return getattr(amadea, "rifling")()
                elif card3bol == True:
                    if "advanced_rifling" in player1_normalcards:
                        player1_normalcards.remove("advanced_rifling")
                        return getattr(amadea, "advanced_rifling")()
                elif card4bol == True:
                    if "reinforced_hull"in player1_normalcards:
                        player1_normalcards.remove("reinforced_hull")
                        return getattr(amadea, "reinforced_hull")()
                elif card6bol == True:
                    if "extra_fuel" in player1_normalcards:
                        player1_normalcards.remove("extra_fuel")
                        return getattr(amadea, "extra_fuel")()
                elif card7bol == True:
                    if "rally" in player1_normalcards:
                        player1_normalcards.remove("rally")
                        return getattr(amadea, "rally")()
                elif card8bol == True:
                    if "andrenaline_rush" in player1_normalcards:
                        player1_normalcards.remove("andrenaline_rush")
                        return getattr(amadea, "andrenaline_rush")()
                elif card9bol == True:
                    if "repair" in player1_trapcards:
                        player1_trapcards.remove("repair")
                        return getattr(amadea, "repair")()
                elif card10bol == True:
                    if "flak_armor"in player1_trapcards:
                        player1_trapcards.remove("flak_armor")
                        return getattr(amadea, "flak_armor")()
                elif card11bol == True:
                    if "far_sight" in player1_trapcards:
                        player1_trapcards.remove("far_sight")
                        return getattr(amadea, "far_sight")()
                elif card12bol == True:
                    if  "aluminum_hull" in player1_trapcards:
                        player1_trapcards.remove( "aluminum_hull")
                        return getattr(amadea, "aluminum_hull")()
        elif player1 == False:
            if boat1bol == True:
                if card1bol == True:
                    if  "fmj_upgrade"in player2_normalcards:
                        player2_normalcards.remove("fmj_upgrade")
                        return getattr(fungo_saltire, "fmj_upgrade")()
                elif card2bol == True:
                    if "rifling" in player2_normalcards:
                        player2_normalcards.remove("rifling")
                        return getattr(fungo_saltire, "rifling")()
                elif card3bol == True:
                    if  "advanced_rifling" in player2_normalcards:
                        player2_normalcards.remove( "advanced_rifling")
                        return getattr(fungo_saltire, "advanced_rifling")()
                elif card4bol == True:
                    if "reinforced_hull" in player2_normalcards:
                        player2_normalcards.remove("reinforced_hull")
                        return getattr(fungo_saltire, "reinforced_hull")()
                elif card6bol == True:
                    if "extra_fuel" in player2_normalcards:
                        player2_normalcards.remove("extra_fuel")
                        return getattr(fungo_saltire, "extra_fuel")()
                elif card7bol == True:
                    if  "rally" in player2_normalcards:
                        player2_normalcards.remove( "rally")
                        return getattr(fungo_saltire, "rally")()
                elif card8bol == True:
                    if "andrenaline_rush" in player2_normalcards:
                        player2_normalcards.remove("andrenaline_rush")
                        return getattr(fungo_saltire, "andrenaline_rush")()
                elif card9bol == True:
                    if "repair" in player2_trapcards:
                        player2_trapcards.remove("repair")
                        return getattr(fungo_saltire, "repair")()
                elif card10bol == True:
                    if "flak_armor" in player2_trapcards:
                        player2_trapcards.remove("flak_armor")
                        return getattr(fungo_saltire, "flak_armor")()
                elif card11bol == True:
                    if "far_sight" in player2_trapcards:
                        player2_trapcards.remove("far_sight")
                        return getattr(fungo_saltire, "far_sight")()
                elif card12bol == True:
                    if "aluminum_hull" in player2_trapcards:
                        player2_trapcards.remove("aluminum_hull")
                    return getattr(fungo_saltire, "aluminum_hull")()
            elif boat2bol == True:
                if card1bol == True:
                    if  "fmj_upgrade" in player2_normalcards:
                        player2_normalcards.remove( "fmj_upgrade")
                    return getattr(silver_whisper, "fmj_upgrade")()
                elif card2bol == True:
                    if "rifling" in player2_normalcards:
                        player2_normalcards.remove("rifling")
                        return getattr(silver_whisper, "rifling")()
                elif card3bol == True:
                    if "advanced_rifling" in player2_normalcards:
                        player2_normalcards.remove("advanced_rifling")
                        return getattr(silver_whisper, "advanced_rifling")()
                elif card4bol == True:
                    if "reinforced_hull" in player2_normalcards:
                        player2_normalcards.remove("reinforced_hull")
                        return getattr(silver_whisper, "reinforced_hull")()

                elif card6bol == True:
                    if "extra_fuel" in player2_normalcards:
                        player2_normalcards.remove("extra_fuel")
                        return getattr(silver_whisper, "extra_fuel")()
                elif card7bol == True:
                    if  "rally" in player2_normalcards:
                        player2_normalcards.remove( "rally")
                        return getattr(silver_whisper, "rally")()
                elif card8bol == True:
                    if "andrenaline_rush" in player2_normalcards:
                        player2_normalcards.remove("andrenaline_rush")
                        return getattr(silver_whisper, "andrenaline_rush")()
                elif card9bol == True:
                    if "repair" in player2_trapcards:
                        player2_trapcards.remove( "repair")
                        return getattr(silver_whisper, "repair")()
                elif card10bol == True:
                    if "flak_armor" in player2_trapcards:
                        player2_trapcards.remove("flak_armor")
                        return getattr(silver_whisper, "flak_armor")()
                elif card11bol == True:
                    if  "far_sight" in player2_trapcards:
                        player2_trapcards.remove( "far_sight")
                        return getattr(silver_whisper, "far_sight")()
                elif card12bol == True:
                    if "aluminum_hull" in player2_trapcards:
                        player2_trapcards.remove("aluminum_hull")
                        return getattr(silver_whisper, "aluminum_hull")()
            elif boat3bol == True:
                if card1bol == True:
                    if "fmj_upgrade" in player2_normalcards:
                        player2_normalcards.remove("fmj_upgrade")
                        return getattr(sea_spirit, "fmj_upgrade")()
                elif card2bol == True:
                    if "rifling" in player2_normalcards:
                        player2_normalcards.remove("rifling")
                        return getattr(sea_spirit, "rifling")()
                elif card3bol == True:
                    if "advanced_rifling" in player2_normalcards:
                        player2_normalcards.remove("advanced_rifling")
                        return getattr(sea_spirit, "advanced_rifling")()
                elif card4bol == True:
                    if  "reinforced_hull" in player2_normalcards:
                        player2_normalcards.remove( "reinforced_hull")
                        return getattr(sea_spirit, "reinforced_hull")()

                elif card6bol == True:
                    if "extra_fuel" in player2_normalcards:
                        player2_normalcards.remove("extra_fuel")
                        return getattr(sea_spirit, "extra_fuel")()
                elif card7bol == True:
                    if "rally" in player2_normalcards:
                        player2_normalcards.remove("rally")
                        return getattr(sea_spirit, "rally")()
                elif card8bol == True:
                    if  "andrenaline_rush" in player2_normalcards:
                        player2_normalcards.remove( "andrenaline_rush")
                        return getattr(sea_spirit, "andrenaline_rush")()
                elif card9bol == True:
                    if "repair" in player2_trapcards:
                        player2_trapcards.remove("repair")
                        return getattr(sea_spirit, "repair")()
                elif card10bol == True:
                    if "flak_armor" in player2_trapcards:
                        player2_trapcards.remove("flak_armor")
                        return getattr(sea_spirit, "flak_armor")()
                elif card11bol == True:
                    if "far_sight" in player2_trapcards:
                        player2_trapcards.remove("far_sight")
                        return getattr(sea_spirit, "far_sight")()
                elif card12bol == True:
                    if "aluminum_hull" in player2_trapcards:
                        player2_trapcards.remove("aluminum_hull")
                        return getattr(sea_spirit, "aluminum_hull")()
            elif boat4bol == True:
                if card1bol == True:
                    if "fmj_upgrade" in player2_normalcards:
                        player2_normalcards.remove("fmj_upgrade")
                        return getattr(merapi, "fmj_upgrade")()
                elif card2bol == True:
                    if "rifling" in player2_normalcards:
                        player2_normalcards.remove("rifling")
                        return getattr(merapi, "rifling")()
                elif card3bol == True:
                    if "advanced_rifling" in player2_normalcards:
                        player2_normalcards.remove("advanced_rifling")
                        return getattr(merapi, "advanced_rifling")()
                elif card4bol == True:
                    if "reinforced_hull" in player2_normalcards:
                        player2_normalcards.remove( "reinforced_hull")
                        return getattr(merapi, "reinforced_hull")()

                elif card6bol == True:
                    if "extra_fuel"  in player2_normalcards:
                        player2_normalcards.remove("extra_fuel")
                        return getattr(merapi, "extra_fuel")()
                elif card7bol == True:
                    if "rally" in player2_normalcards:
                        player2_normalcards.remove("rally")
                        return getattr(merapi, "rally")()
                elif card8bol == True:
                    if "andrenaline_rush" in player2_normalcards:
                        player2_normalcards.remove("andrenaline_rush")
                        return getattr(merapi, "andrenaline_rush")()
                elif card9bol == True:
                    if "repair" in player2_trapcards:
                        player2_trapcards.remove("repair")
                        return getattr(merapi, "repair")()
                elif card10bol == True:
                    if "flak_armor" in player2_trapcards:
                        player2_trapcards.remove("flak_armor")
                        return getattr(merapi, "flak_armor")()
                elif card11bol == True:
                    if "far_sight" in player2_trapcards:
                        player2_trapcards.remove("far_sight")
                        return getattr(merapi, "far_sight")()
                elif card12bol == True:
                    if "aluminum_hull" in player2_trapcards:
                        player2_trapcards.remove("aluminum_hull")
                        return getattr(merapi, "aluminum_hull")()
            elif boat5bol == True:
                if card1bol == True:
                    if  "fmj_upgrade" in player2_normalcards:
                        player2_normalcards.remove( "fmj_upgrade")
                        return getattr(santa_bettina, "fmj_upgrade")()
                elif card2bol == True:
                    if  "rifling" in player2_normalcards:
                        player2_normalcards.remove( "rifling")
                        return getattr(santa_bettina, "rifling")()
                elif card3bol == True:
                    if "advanced_rifling" in player2_normalcards:
                        player2_normalcards.remove("advanced_rifling")
                        return getattr(santa_bettina, "advanced_rifling")()
                elif card4bol == True:
                    if "reinforced_hull" in player2_normalcards:
                        player2_normalcards.remove("reinforced_hull")
                        return getattr(santa_bettina, "reinforced_hull")()

                elif card6bol == True:
                    if "extra_fuel" in player2_normalcards:
                        player2_normalcards.remove("extra_fuel")
                        return getattr(santa_bettina, "extra_fuel")()
                elif card7bol == True:
                    if  "rally" in player2_normalcards:
                        player2_normalcards.remove( "rally")
                        return getattr(santa_bettina, "rally")()
                elif card8bol == True:
                    if "rally" in player2_normalcards:
                        player2_normalcards.remove("andrenaline_rush")
                        return getattr(santa_bettina, "andrenaline_rush")()
                elif card9bol == True:
                    if  "repair" in player2_trapcards:
                        player2_trapcards.remove( "repair")
                        return getattr(santa_bettina, "repair")()
                elif card10bol == True:
                    if  "flak_armor" in player2_trapcards:
                        player2_trapcards.remove("flak_armor")
                        return getattr(santa_bettina, "flak_armor")()
                elif card11bol == True:
                    if  "far_sight" in player2_trapcards:
                        player2_trapcards.remove("far_sight")
                        return getattr(santa_bettina, "far_sight")()
                elif card12bol == True:
                    if "aluminum_hull" in player2_trapcards:
                        player2_trapcards.remove("aluminum_hull")
                        return getattr(santa_bettina, "aluminum_hull")()
            elif boat6bol == True:
                if card1bol == True:
                    if  "fmj_upgrade" in player2_normalcards:
                        player2_normalcards.remove( "fmj_upgrade")
                        return getattr(windsurf, "fmj_upgrade")()
                elif card2bol == True:
                    if "rifling"in player2_normalcards:
                        player2_normalcards.remove("rifling")
                        return getattr(windsurf, "rifling")()
                elif card3bol == True:
                    if  "advanced_rifling"in player2_normalcards:
                        player2_normalcards.remove( "advanced_rifling")
                        return getattr(windsurf, "advanced_rifling")()
                elif card4bol == True:
                    if "reinforced_hull"in player2_normalcards:
                        player2_normalcards.remove("reinforced_hull")
                        return getattr(windsurf, "reinforced_hull")()
                elif card6bol == True:
                    if "extra_fuel" in player2_normalcards:
                        player2_normalcards.remove("extra_fuel")
                        return getattr(windsurf, "extra_fuel")()
                elif card7bol == True:
                    if  "rally" in player2_normalcards:
                        player2_normalcards.remove( "rally")
                        return getattr(windsurf, "rally")()
                elif card8bol == True:
                    if "andrenaline_rush" in player2_normalcards:
                        player2_normalcards.remove("andrenaline_rush")
                        return getattr(windsurf, "andrenaline_rush")()
                elif card9bol == True:
                    if "repair" in player2_trapcards:
                        player2_trapcards.remove("repair")
                        return getattr(windsurf, "repair")()
                elif card10bol == True:
                    if  "flak_armor" in player2_trapcards:
                        player2_trapcards.remove( "flak_armor")
                        return getattr(windsurf, "flak_armor")()
                elif card11bol == True:
                    if "far_sight" in player2_trapcards:
                        player2_trapcards.remove("far_sight")
                        return getattr(windsurf, "far_sight")()
                elif card12bol == True:
                    if "aluminum_hull" in player2_trapcards:
                        player2_trapcards.remove("aluminum_hull")
                        return getattr(windsurf, "aluminum_hull")()
            elif boat7bol == True:
                if card1bol == True:
                    if "fmj_upgrade" in player2_normalcards:
                        player2_normalcards.remove("fmj_upgrade")
                        return getattr(intensity, "fmj_upgrade")()
                elif card2bol == True:
                    if "rifling"in player2_normalcards:
                        player2_normalcards.remove("rifling")
                        return getattr(intensity, "rifling")()
                elif card3bol == True:
                    if "advanced_rifling" in player2_normalcards:
                        player2_normalcards.remove("advanced_rifling")
                        return getattr(intensity, "advanced_rifling")()
                elif card4bol == True:
                    if "reinforced_hull" in player2_normalcards:
                        player2_normalcards.remove("reinforced_hull")
                        return getattr(intensity, "reinforced_hull")()

                elif card6bol == True:
                    if  "extra_fuel" in player2_normalcards:
                        player2_normalcards.remove( "extra_fuel")
                        return getattr(intensity, "extra_fuel")()
                elif card7bol == True:
                    if  "rally"in player2_normalcards:
                        player2_normalcards.remove( "rally")
                        return getattr(intensity, "rally")()
                elif card8bol == True:
                    if "andrenaline_rush"in player2_normalcards:
                        player2_normalcards.remove("andrenaline_rush")
                        return getattr(intensity, "andrenaline_rush")()
                elif card9bol == True:
                    if  "repair" in player2_trapcards:
                        player2_trapcards.remove( "repair")
                        return getattr(intensity, "repair")()
                elif card10bol == True:
                    if  "flak_armor" in player2_trapcards:
                        player2_trapcards.remove( "flak_armor")
                        return getattr(intensity, "flak_armor")()
                elif card11bol == True:
                    if "far_sight" in player2_trapcards:
                        player2_trapcards.remove("far_sight")
                        return getattr(intensity, "far_sight")()
                elif card12bol == True:
                    if "aluminum_hull" in player2_trapcards:
                        player2_trapcards.remove("aluminum_hull")
                        return getattr(intensity, "aluminum_hull")()
            elif boat8bol == True:
                if card1bol == True:
                    if "fmj_upgrade" in player2_normalcards:
                        player2_normalcards.remove("fmj_upgrade")
                        return getattr(amadea, "fmj_upgrade")()
                elif card2bol == True:
                    if "rifling" in player2_normalcards:
                        player2_normalcards.remove("rifling")
                        return getattr(amadea, "rifling")()
                elif card3bol == True:
                    if "advanced_rifling" in player2_normalcards:
                        player2_normalcards.remove("advanced_rifling")
                        return getattr(amadea, "advanced_rifling")()
                elif card4bol == True:
                    if "reinforced_hull" in player2_normalcards:
                        player2_normalcards.remove("reinforced_hull")
                        return getattr(amadea, "reinforced_hull")()
                elif card6bol == True:
                    if "extra_fuel" in player2_normalcards:
                        player2_normalcards.remove("extra_fuel")
                        return getattr(amadea, "extra_fuel")()
                elif card7bol == True:
                    if "rally" in player2_normalcards:
                        player2_normalcards.remove("rally")
                        return getattr(amadea, "rally")()
                elif card8bol == True:
                    if "andrenaline_rush" in player2_normalcards:
                        player2_normalcards.remove("andrenaline_rush")
                        return getattr(amadea, "andrenaline_rush")()
                elif card9bol == True:
                    if "repair" in player2_trapcards:
                        player2_trapcards.remove("repair")
                        return getattr(amadea, "repair")()
                elif card10bol == True:
                    if "flak_armor"in player2_trapcards:
                        player2_trapcards.remove("flak_armor")
                        return getattr(amadea, "flak_armor")()
                elif card11bol == True:
                    if  "far_sight" in player2_trapcards:
                        player2_trapcards.remove( "far_sight")
                        return getattr(amadea, "far_sight")()
                elif card12bol == True:
                    if "aluminum_hull" in player2_trapcards:
                        player2_trapcards.remove("aluminum_hull")
                        return getattr(amadea, "aluminum_hull")()




    the_main_loop = True
    while the_main_loop == True:
        random_normal_deck = random.randint(1, 9)
        special_normal_deck = random.randint(1, 5)
        for events in pygame.event.get():
            screen_image.blit(menu_image, (0, 0))
            if santa_bettina.health <= 0 and boat1dead == 1:
                effect19.play()
                player1winner.score += 1
                boat1dead -= 1
            if windsurf.health <= 0 and boat2dead == 1:
                effect19.play()
                player1winner.score += 1
                boat2dead -= 1
            if intensity.health <= 0 and boat3dead == 1:
                effect19.play()
                player1winner.score += 1
                boat3dead -= 1
            if amadea.health <= 0 and boat4dead == 1:
                effect19.play()
                player1winner.score += 1
                boat4dead -= 1
            if fungo_saltire.health <= 0 and boat5dead == 1:
                effect19.play()
                player2winner.score += 1
                boat5dead -= 1
            if silver_whisper.health <= 0 and boat6dead == 1:
                effect19.play()
                player2winner.score += 1
                boat6dead -= 1
            if sea_spirit.health <= 0 and boat7dead == 1:
                effect19.play()
                player2winner.score += 1
                boat7dead -= 1
            if merapi.health <= 0 and boat8dead == 1:
                effect19.play()
                player2winner.score += 1
                boat8dead -= 1
            if player1winner.score >= 4:
                menu_image300 = pygame.image.load('player1winner.png')
                screen.blit(menu_image300, (display_width1 * 0.50, display_height1 * 0.58))
                cur.execute("Insert into battleport_highscores VALUES (%s, %s, %s, %s)",
                            (3, player1winner.Name, 1, 0))
                cur.execute("Insert into battleport_highscores VALUES (%s, %s, %s, %s)",
                            (4, player2winner.Name, 0, 1))
                the_player1winner()



            if player2winner.score >= 4:
                menu_image500 = pygame.image.load('player2winner.png')
                screen.blit(menu_image500, (display_width1 * 0.69, display_height1 * 0.58))
                cur.execute("Insert into battleport_highscores VALUES (%s, %s, %s, %s)",
                            (3, player1winner.Name, 0, 1))
                cur.execute("Insert into battleport_highscores VALUES (%s, %s, %s, %s)",
                            (4, player2winner.Name, 1, 0))

                the_player2winner()


            if player1 == True:
                santa_bettina.maxsteps.stepreset()
                windsurf.maxsteps.stepreset()
                intensity.maxsteps.stepreset()
                amadea.maxsteps.stepreset()
                if events.type == pygame.KEYDOWN:
                    if events.key == pygame.K_r and fungo_saltire.health > 0 :
                        boat1bol = True
                        boat2bol = False
                        boat3bol = False
                        boat4bol = False
                        boat5bol = False
                        boat6bol = False
                        boat7bol = False
                        boat8bol = False

                        fungosaltirefont_font = my_font.render("Fungo saltire", 1, blue)
                        fungosaltireHP_font = my_font.render("HP: " + str(fungo_saltire.health), 1, red)
                        fungosaltireSteps_font = my_font.render("Steps : " + str(fungo_saltire.maxsteps.steps), 1, red)
                        fungosaltireMaxSteps_font = my_font.render("Max steps: " + str(fungo_saltire.maxsteps.Maxsteps), 1,
                                                                   red)
                        fungosaltireDamage_font = my_font.render("Damage: " + str(fungo_saltire.damage), 1, red)
                        fungosaltireOffensiveX_font = my_font.render(
                            "Off range X: " + str(fungo_saltire.offensive_range.rangeX), 1, red)
                        fungosaltireOffensiveY_font = my_font.render(
                            "Off range Y: " + str(fungo_saltire.offensive_range.rangeY), 1, red)
                        fungosaltireDefensive_font = my_font.render(
                            "Def range Y: " + str(fungo_saltire.defensive_range.therangeY), 1, red)

                        screen.blit(fungosaltirefont_font, (display_width1 * 0.75, display_height1 * 0.635))
                        screen.blit(fungosaltireHP_font, (display_width1 * 0.70, display_height1 * 0.694))
                        screen.blit(fungosaltireSteps_font, (display_width1 * 0.70, display_height1 * 0.737))
                        screen.blit(fungosaltireMaxSteps_font, (display_width1 * 0.70, display_height1 * 0.78))
                        screen.blit(fungosaltireDamage_font, (display_width1 * 0.70, display_height1 * 0.825))
                        screen.blit(fungosaltireOffensiveX_font, (display_width1 * 0.70, display_height1 * 0.87))
                        screen.blit(fungosaltireOffensiveY_font, (display_width1 * 0.70, display_height1 * 0.91))
                        screen.blit(fungosaltireDefensive_font, (display_width1 * 0.70, display_height1 * 0.95))

                    elif events.key == pygame.K_t and silver_whisper.health > 0:
                        boat2bol = True
                        boat1bol = False
                        boat3bol = False
                        boat4bol = False
                        boat5bol = False
                        boat6bol = False
                        boat7bol = False
                        boat8bol = False

                        silverwhisperfont_font = my_font.render("Silver whisper", 1, blue)
                        silverwhisperHP_font = my_font.render("HP: " + str(silver_whisper.health), 1, red)
                        silverwhisperSteps_font = my_font.render("Steps: " + str(silver_whisper.maxsteps.steps), 1,
                                                                 red)
                        silverwhisperMaxSteps_font = my_font.render("Max steps: " + str(silver_whisper.maxsteps.Maxsteps),
                                                                    1, red)
                        silverwhisperDamage_font = my_font.render("Damage: " + str(silver_whisper.damage), 1, red)
                        silverwhisperOffensiveX_font = my_font.render(
                            "Off range X: " + str(silver_whisper.offensive_range.rangeX), 1, red)
                        silverwhisperOffensiveY_font = my_font.render(
                            "Off range Y: " + str(silver_whisper.offensive_range.rangeY), 1, red)
                        silverwhisperDefensive_font = my_font.render(
                            "Def range Y: " + str(silver_whisper.defensive_range.therangeY), 1, red)

                        screen.blit(silverwhisperfont_font, (display_width1 * 0.75, display_height1 * 0.634))
                        screen.blit(silverwhisperHP_font, (display_width1 * 0.70, display_height1 * 0.695))
                        screen.blit(silverwhisperSteps_font, (display_width1 * 0.70, display_height1 * 0.737))
                        screen.blit(silverwhisperMaxSteps_font, (display_width1 * 0.70, display_height1 * 0.78))
                        screen.blit(silverwhisperDamage_font, (display_width1 * 0.70, display_height1 * 0.825))
                        screen.blit(silverwhisperOffensiveX_font, (display_width1 * 0.70, display_height1 * 0.87))
                        screen.blit(silverwhisperOffensiveY_font, (display_width1 * 0.70, display_height1 * 0.91))
                        screen.blit(silverwhisperDefensive_font, (display_width1 * 0.70, display_height1 * 0.95))

                    elif events.key == pygame.K_y and sea_spirit.health > 0:
                        boat3bol = True
                        boat2bol = False
                        boat1bol = False
                        boat4bol = False
                        boat5bol = False
                        boat6bol = False
                        boat7bol = False
                        boat8bol = False

                        seaspiritfont_font = my_font.render("Sea spirit", 1, blue)
                        seaspiritHP_font = my_font.render("HP: " + str(sea_spirit.health), 1, red)
                        seaspiritSteps_font = my_font.render("Steps: " + str(sea_spirit.maxsteps.steps), 1, red)
                        seaspiritMaxSteps_font = my_font.render("Max Steps: " + str(sea_spirit.maxsteps.Maxsteps), 1, red)
                        seaspiritDamage_font = my_font.render("Damage: " + str(sea_spirit.damage), 1, red)
                        seaspiritOffensiveX_font = my_font.render("Off range X: " + str(sea_spirit.offensive_range.rangeX),
                                                                  1, red)
                        seaspiritffensiveY_font = my_font.render("Off range Y: " + str(sea_spirit.offensive_range.rangeY),
                                                                 1, red)
                        seaspiritDefensive_font = my_font.render(
                            "Def range Y: " + str(sea_spirit.defensive_range.therangeY), 1, red)

                        screen.blit(seaspiritfont_font, (display_width1 * 0.79, display_height1 * 0.635))
                        screen.blit(seaspiritHP_font, (display_width1 * 0.70, display_height1 * 0.695))
                        screen.blit(seaspiritSteps_font, (display_width1 * 0.70, display_height1 * 0.737))
                        screen.blit(seaspiritMaxSteps_font, (display_width1 * 0.70, display_height1 * 0.78))
                        screen.blit(seaspiritDamage_font, (display_width1 * 0.70, display_height1 * 0.825))
                        screen.blit(seaspiritOffensiveX_font, (display_width1 * 0.70, display_height1 * 0.87))
                        screen.blit(seaspiritffensiveY_font, (display_width1 * 0.70, display_height1 * 0.91))
                        screen.blit(seaspiritDefensive_font, (display_width1 * 0.70, display_height1 * 0.95))

                    elif events.key == pygame.K_u and merapi.health > 0:
                        boat4bol = True
                        boat3bol = False
                        boat2bol = False
                        boat1bol = False
                        boat5bol = False
                        boat6bol = False
                        boat7bol = False
                        boat8bol = False

                        merapifont_font = my_font.render("Merapi", 1, blue)
                        merapiHP_font = my_font.render("HP: " + str(merapi.health), 1, red)
                        merapiSteps_font = my_font.render("Steps: " + str(merapi.maxsteps.steps), 1, red)
                        merapiMaxSteps_font = my_font.render("Max Steps: " + str(merapi.maxsteps.Maxsteps), 1, red)
                        merapiDamage_font = my_font.render("Damage: " + str(merapi.damage), 1, red)
                        merapiOffensiveX_font = my_font.render("Off range X: " + str(merapi.offensive_range.rangeX), 1, red)
                        merapiOffensiveY_font = my_font.render("Off range Y: " + str(merapi.offensive_range.rangeY), 1, red)
                        merapiDefensive_font = my_font.render("Def range Y: " + str(merapi.defensive_range.therangeY), 1,
                                                              red)

                        screen.blit(merapifont_font, (display_width1 * 0.79, display_height1 * 0.64))
                        screen.blit(merapiHP_font, (display_width1 * 0.70, display_height1 * 0.69))
                        screen.blit(merapiSteps_font, (display_width1 * 0.70, display_height1 * 0.737))
                        screen.blit(merapiMaxSteps_font, (display_width1 * 0.70, display_height1 * 0.78))
                        screen.blit(merapiDamage_font, (display_width1 * 0.70, display_height1 * 0.825))
                        screen.blit(merapiOffensiveX_font, (display_width1 * 0.70, display_height1 * 0.87))
                        screen.blit(merapiOffensiveY_font, (display_width1 * 0.70, display_height1 * 0.91))
                        screen.blit(merapiDefensive_font, (display_width1 * 0.70, display_height1 * 0.95))




                    elif events.key == pygame.K_w and boat1bol == True and fungo_saltire.maxsteps.stepadd() and aboat1.leady > 106:
                        aboat1.leady -= 35.5
                        fungo_saltire.maxsteps.steps += 1
                    elif events.key == pygame.K_s and boat1bol == True and fungo_saltire.maxsteps.stepadd() and aboat1.leady < 700:
                        aboat1.leady += 35.5
                        fungo_saltire.maxsteps.steps += 1
                    elif events.key == pygame.K_a and boat1bol == True and fungo_saltire.maxsteps.stepadd() and aboat1.leadx > 112:
                        aboat1.leadx -= 33
                        fungo_saltire.maxsteps.steps += 1
                    elif events.key == pygame.K_d and boat1bol == True and fungo_saltire.maxsteps.stepadd() and aboat1.leadx < 738:
                        aboat1.leadx += 33
                        fungo_saltire.maxsteps.steps += 1
                    elif events.key == pygame.K_w and boat2bol == True and silver_whisper.maxsteps.stepadd() and aboat2.leady > 106:
                         aboat2.leady -= 35.5
                         silver_whisper.maxsteps.steps += 1
                    elif events.key == pygame.K_s and boat2bol == True  and silver_whisper.maxsteps.stepadd() and aboat2.leady < 700:
                        aboat2.leady += 35.5
                        silver_whisper.maxsteps.steps += 1
                    elif events.key == pygame.K_a and boat2bol == True and  silver_whisper.maxsteps.stepadd()  and aboat2.leadx > 112:
                        aboat2.leadx -= 33
                        silver_whisper.maxsteps.steps += 1
                    elif events.key == pygame.K_d and boat2bol == True and  silver_whisper.maxsteps.stepadd() and aboat2.leadx < 738:
                        aboat2.leadx += 33
                        silver_whisper.maxsteps.steps += 1
                    elif events.key == pygame.K_w and boat3bol == True and sea_spirit.maxsteps.stepadd() and aboat3.leady > 106:
                        aboat3.leady -= 35.5
                        sea_spirit.maxsteps.steps += 1
                    elif events.key == pygame.K_s and boat3bol == True and sea_spirit.maxsteps.stepadd()  and aboat3.leady < 650:
                        aboat3.leady += 35.5
                        sea_spirit.maxsteps.steps += 1
                    elif events.key == pygame.K_a and boat3bol == True and sea_spirit.maxsteps.stepadd()  and aboat3.leadx > 112:
                        aboat3.leadx -= 33
                        sea_spirit.maxsteps.steps += 1
                    elif events.key == pygame.K_d and boat3bol == True and sea_spirit.maxsteps.stepadd() and aboat3.leadx < 738:
                        aboat3.leadx += 33
                        sea_spirit.maxsteps.steps += 1
                    elif events.key == pygame.K_w and boat4bol == True and merapi.maxsteps.stepadd()  and aboat4.leady > 106:
                        aboat4.leady -= 35.5
                        merapi.maxsteps.steps += 1
                    elif events.key == pygame.K_s and boat4bol == True and merapi.maxsteps.stepadd()  and aboat4.leady < 635:
                        aboat4.leady += 35.5
                        merapi.maxsteps.steps += 1
                    elif events.key == pygame.K_a and boat4bol == True and merapi.maxsteps.stepadd()  and aboat4.leadx > 112:
                        aboat4.leadx -= 33
                        merapi.maxsteps.steps += 1
                    elif events.key == pygame.K_d and boat4bol == True and merapi.maxsteps.stepadd() and aboat4.leadx < 738:
                        aboat4.leadx += 33
                        merapi.maxsteps.steps += 1
                    if aboat1.leady < 100:
                        specialboat1 = True
                        if sb1 == 1:
                            effect17.play()
                            sb1 = 0
                    if  aboat2.leady < 100:
                        specialboat2 = True
                        if sb2 == 1:
                            effect17.play()
                            sb2 = 0
                    if aboat3.leady < 106:
                        specialboat3 = True
                        if sb3 == 1:
                            effect17.play()
                            sb3 = 0
                    if aboat4.leady < 106:
                        specialboat4 = True
                        if sb4 == 1:
                            effect17.play()
                            sb4 = 0



                    if events.key == pygame.K_1:
                        if len(player1_normalcards) > 0:
                            card_show(player1_normalcards [0])
                            effect3.play()
                        else:
                            menu_image29 = pygame.image.load('empty_card.png')
                            screen.blit(menu_image29, (display_width1 * 0.769, display_height1 * 0.4276))

                    elif events.key == pygame.K_2:
                        if len(player1_normalcards) > 1:
                            card_show(player1_normalcards [1])
                            effect4.play()
                        else:
                            menu_image29 = pygame.image.load('empty_card.png')
                            screen.blit(menu_image29, (display_width1 * 0.769, display_height1 * 0.4276))
                    elif events.key == pygame.K_3:
                        if len(player1_normalcards) > 2:
                            card_show(player1_normalcards [2])
                            effect5.play()
                        else:
                            menu_image29 = pygame.image.load('empty_card.png')
                            screen.blit(menu_image29, (display_width1 * 0.769, display_height1 * 0.4276))
                    elif events.key == pygame.K_4:
                        if len(player1_normalcards) > 3:
                            card_show(player1_normalcards [3])
                            effect6.play()
                        else:
                            menu_image29 = pygame.image.load('empty_card.png')
                            screen.blit(menu_image29, (display_width1 * 0.769, display_height1 * 0.4276))
                    elif events.key == pygame.K_5:
                        if len(player1_normalcards) > 4:
                            card_show(player1_normalcards [4])
                            effect7.play()
                        else:
                            menu_image29 = pygame.image.load('empty_card.png')
                            screen.blit(menu_image29, (display_width1 * 0.769, display_height1 * 0.4276))
                    elif events.key == pygame.K_6:
                        if len(player1_normalcards) > 5:
                            card_show(player1_normalcards [5])
                            effect8.play()
                        else:
                            menu_image29 = pygame.image.load('empty_card.png')
                            screen.blit(menu_image29, (display_width1 * 0.769, display_height1 * 0.4276))
                    elif events.key == pygame.K_7:
                        if len(player1_trapcards) > 0:
                            card_show(player1_trapcards [0])
                            effect13.play()
                        else:
                            menu_image29 = pygame.image.load('empty_card.png')
                            screen.blit(menu_image29, (display_width1 * 0.769, display_height1 * 0.4276))
                    elif events.key == pygame.K_8:
                        if len(player1_trapcards) > 1:
                            card_show(player1_trapcards [1])
                            effect14.play()
                        else:
                            menu_image29 = pygame.image.load('empty_card.png')
                            screen.blit(menu_image29, (display_width1 * 0.769, display_height1 * 0.4276))
                    elif events.key == pygame.K_9:
                        if len(player1_trapcards) > 2:
                            card_show(player1_trapcards [2])
                            effect15.play()
                        else:
                            menu_image29 = pygame.image.load('empty_card.png')
                            screen.blit(menu_image29, (display_width1 * 0.769, display_height1 * 0.4276))
                    elif events.key == pygame.K_0:
                        if len(player1_trapcards) > 3:
                            card_show(player1_trapcards [3])
                            effect16.play()
                        else:
                            menu_image29 = pygame.image.load('empty_card.png')
                            screen.blit(menu_image29, (display_width1 * 0.769, display_height1 * 0.4276))

                        menu_image29 = pygame.image.load('empty_card.png')
                        screen.blit(menu_image29, (display_width1 * 0.769, display_height1 * 0.4276))
                    elif events.key == pygame.K_p:
                        activate_card()


                    elif events.key == pygame.K_v:
                        boat5_trigger = True
                    elif events.key == pygame.K_b:
                        boat6_trigger = True
                    elif events.key == pygame.K_n:
                        boat7_trigger = True
                    elif events.key == pygame.K_m:
                        boat8_trigger = True





                    #boat 2 on 2 squares boat 1 on boat 5 PERFECT
                    if boat1bol == True and boat5_trigger == True and fungo_saltire.offensive_rangebol == True:
                           if abs (aboat1.leadx + (fungo_saltire.offensive_range.rangeX * 2) - aboat5.leadx) <= 70:
                                if abs(aboat1.leady - aboat5.leady) < 0.20:
                                    if events.key == pygame.K_SPACE:
                                        santa_bettina.health -= fungo_saltire.damage
                                        screen.fill(red)
                                        boat5_trigger = False
                           if abs (aboat1.leady  + (fungo_saltire.offensive_range.rangeY * 1) - aboat5.leady) <= 100:
                               if abs(aboat1.leadx - aboat5.leadx) < 2:
                                   if events.key == pygame.K_SPACE:
                                       santa_bettina.health -= fungo_saltire.damage
                                       screen.fill(red)
                                       boat5_trigger = False
                    #boat 2squares on 3 squares, boat 1 on boat 6 PERFECT
                    if boat1bol == True and boat6_trigger == True and fungo_saltire.offensive_rangebol == True:
                           if abs (aboat1.leadx + (fungo_saltire.offensive_range.rangeX * 2) - aboat6.leadx) <= 70:
                                if abs(aboat1.leady - aboat6.leady) < 50:
                                    if events.key == pygame.K_SPACE:
                                        windsurf.health -= fungo_saltire.damage
                                        screen.fill(red)
                                        boat6_trigger = False
                           if abs (aboat1.leady  + (fungo_saltire.offensive_range.rangeY * 1) - aboat6.leady) <= 125:
                               if abs(aboat1.leadx - aboat6.leadx) < 2:
                                   if events.key == pygame.K_SPACE:
                                       windsurf.health -= fungo_saltire.damage
                                       screen.fill(red)
                                       boat6_trigger = False
                    #boat 1 on boat 7 2 squares on 3 squares perfect
                    if boat1bol == True and boat7_trigger == True and fungo_saltire.offensive_rangebol == True:
                           if abs (aboat1.leadx + (fungo_saltire.offensive_range.rangeX * 2) - aboat7.leadx) <= 70:
                                if abs(aboat1.leady - aboat7.leady) < 50:
                                    if events.key == pygame.K_SPACE:
                                        intensity.health -= fungo_saltire.damage
                                        screen.fill(red)
                                        boat7_trigger = False
                           if abs (aboat1.leady  + (fungo_saltire.offensive_range.rangeY * 1) - aboat7.leady) <= 125:
                               if abs(aboat1.leadx - aboat7.leadx) < 2:
                                   if events.key == pygame.K_SPACE:
                                       intensity.health -= fungo_saltire.damage
                                       screen.fill(red)
                                       boat7_trigger = False
                    #boat 1 on boat 8 2 squares on 4 squares PERFECT
                    if boat1bol == True and boat8_trigger == True and fungo_saltire.offensive_rangebol == True:
                           if abs (aboat1.leadx + (fungo_saltire.offensive_range.rangeX * 2) - aboat8.leadx) <= 70:
                                if abs(aboat1.leady - aboat8.leady) < 75:
                                    if events.key == pygame.K_SPACE:
                                        amadea.health -= fungo_saltire.damage
                                        screen.fill(red)
                                        boat8_trigger = False
                           if abs (aboat1.leady  + (fungo_saltire.offensive_range.rangeY * 1) - aboat8.leady) <= 150:
                               if abs(aboat1.leadx - aboat8.leadx) < 2:
                                   if events.key == pygame.K_SPACE:
                                       amadea.health -= fungo_saltire.damage
                                       screen.fill(red)
                                       boat8_trigger = False








                screen.blit(menu_image30, (display_width1 * 0.70, display_height1 * 0.01))



            elif player1 == False:
                fungo_saltire.maxsteps.stepreset()
                silver_whisper.maxsteps.stepreset()
                sea_spirit.maxsteps.stepreset()
                merapi.maxsteps.stepreset()
                if events.type == pygame.KEYDOWN:
                    if events.key == pygame.K_v and santa_bettina.health > 0:
                        boat5bol = True
                        boat4bol = False
                        boat3bol = False
                        boat2bol = False
                        boat1bol = False
                        boat6bol = False
                        boat7bol = False
                        boat8bol = False

                        santabettina_font = my_font1.render("Santa Bettina", 1, blue)
                        santabettinaHP_font = my_font1.render("HP: " + str(santa_bettina.health), 1, red)
                        santabettinaSteps_font = my_font1.render("Steps: " + str(santa_bettina.maxsteps.steps), 1, red)
                        santabettinaMaxSteps_font = my_font1.render("Max Steps: " + str(santa_bettina.maxsteps.Maxsteps), 1,
                                                                    red)
                        santabettinaDamage_font = my_font1.render("Damage: " + str(santa_bettina.damage), 1, red)
                        santabettinaOffensiveX_font = my_font1.render(
                            "Off range X: " + str(santa_bettina.offensive_range.rangeX), 1, red)
                        santabettinaOffensiveY_font = my_font1.render(
                            "Off range Y: " + str(santa_bettina.offensive_range.rangeY), 1, red)
                        santabettinaDefensive_font = my_font1.render(
                            "Def range Y: " + str(santa_bettina.defensive_range.therangeY), 1, red)

                        screen.blit(santabettina_font, (display_width1 * 0.81, display_height1 * 0.205))
                        screen.blit(santabettinaHP_font, (display_width1 * 0.70, display_height1 * 0.21))
                        screen.blit(santabettinaSteps_font, (display_width1 * 0.70, display_height1 * 0.24))
                        screen.blit(santabettinaMaxSteps_font, (display_width1 * 0.70, display_height1 * 0.27))
                        screen.blit(santabettinaDamage_font, (display_width1 * 0.70, display_height1 * 0.30))
                        screen.blit(santabettinaOffensiveX_font, (display_width1 * 0.70, display_height1 * 0.33))
                        screen.blit(santabettinaOffensiveY_font, (display_width1 * 0.70, display_height1 * 0.36))
                        screen.blit(santabettinaDefensive_font, (display_width1 * 0.70, display_height1 * 0.385))



                    elif events.key == pygame.K_b and windsurf.health > 0:
                        boat6bol = True
                        boat4bol = False
                        boat3bol = False
                        boat2bol = False
                        boat1bol = False
                        boat7bol = False
                        boat8bol = False
                        boat5bol = False

                        windsurf_font = my_font1.render("Windsurf", 1, blue)
                        windsurfHP_font = my_font1.render("HP: " + str(windsurf.health), 1, red)
                        windsurfSteps_font = my_font1.render("Steps: " + str(windsurf.maxsteps.steps), 1, red)
                        windsurfMaxSteps_font = my_font1.render("Max Steps: " + str(windsurf.maxsteps.Maxsteps), 1, red)
                        windsurfDamage_font = my_font1.render("Damage: " + str(windsurf.damage), 1, red)
                        windsurfOffensiveX_font = my_font1.render("Off range X: " + str(windsurf.offensive_range.rangeX), 1,
                                                                  red)
                        windsurfOffensiveY_font = my_font1.render("Off range Y: " + str(windsurf.offensive_range.rangeY), 1,
                                                                  red)
                        windsurfDefensive_font = my_font1.render("Def range Y: " + str(windsurf.defensive_range.therangeY),
                                                                 1, red)

                        screen.blit(windsurf_font, (display_width1 * 0.81, display_height1 * 0.205))
                        screen.blit(windsurfHP_font, (display_width1 * 0.70, display_height1 * 0.21))
                        screen.blit(windsurfSteps_font, (display_width1 * 0.70, display_height1 * 0.24))
                        screen.blit(windsurfMaxSteps_font, (display_width1 * 0.70, display_height1 * 0.27))
                        screen.blit(windsurfDamage_font, (display_width1 * 0.70, display_height1 * 0.30))
                        screen.blit(windsurfOffensiveX_font, (display_width1 * 0.70, display_height1 * 0.33))
                        screen.blit(windsurfOffensiveY_font, (display_width1 * 0.70, display_height1 * 0.36))
                        screen.blit(windsurfDefensive_font, (display_width1 * 0.70, display_height1 * 0.385))


                    elif events.key == pygame.K_n and intensity.health > 0:
                        boat7bol = True
                        boat6bol = False
                        boat4bol = False
                        boat3bol = False
                        boat2bol = False
                        boat1bol = False
                        boat8bol = False
                        boat5bol = False

                        intensity_font = my_font1.render("Intensity", 1, blue)
                        intensityHP_font = my_font1.render("HP: " + str(intensity.health), 1, red)
                        intensitySteps_font = my_font1.render("Steps: " + str(intensity.maxsteps.steps), 1, red)
                        intensityMaxSteps_font = my_font1.render("Max Steps: " + str(intensity.maxsteps.Maxsteps), 1, red)
                        intensityDamage_font = my_font1.render("Damage: " + str(intensity.damage), 1, red)
                        intensityOffensiveX_font = my_font1.render("Off range X: " + str(intensity.offensive_range.rangeX),
                                                                   1,
                                                                   red)
                        intensityOffensiveY_font = my_font1.render("Off range Y: " + str(intensity.offensive_range.rangeY),
                                                                   1,
                                                                   red)
                        intensityDefensive_font = my_font1.render(
                            "Def range Y: " + str(intensity.defensive_range.therangeY),
                            1, red)

                        screen.blit(intensity_font, (display_width1 * 0.81, display_height1 * 0.205))
                        screen.blit(intensityHP_font, (display_width1 * 0.70, display_height1 * 0.21))
                        screen.blit(intensitySteps_font, (display_width1 * 0.70, display_height1 * 0.24))
                        screen.blit(intensityMaxSteps_font, (display_width1 * 0.70, display_height1 * 0.27))
                        screen.blit(intensityDamage_font, (display_width1 * 0.70, display_height1 * 0.30))
                        screen.blit(intensityOffensiveX_font, (display_width1 * 0.70, display_height1 * 0.33))
                        screen.blit(intensityOffensiveY_font, (display_width1 * 0.70, display_height1 * 0.36))
                        screen.blit(intensityDefensive_font, (display_width1 * 0.70, display_height1 * 0.385))



                    elif events.key == pygame.K_m and amadea.health > 0:
                        boat8bol = True
                        boat7bol = False
                        boat6bol = False
                        boat4bol = False
                        boat3bol = False
                        boat2bol = False
                        boat1bol = False
                        boat5bol = False

                        amadea_font = my_font1.render("Amadea", 1, blue)
                        amadeaHP_font = my_font1.render("HP: " + str(amadea.health), 1, red)
                        amadeaSteps_font = my_font1.render("Steps: " + str(amadea.maxsteps.steps), 1, red)
                        amadeaMaxSteps_font = my_font1.render("Max Steps: " + str(amadea.maxsteps.Maxsteps), 1, red)
                        amadeaDamage_font = my_font1.render("Damage: " + str(amadea.damage), 1, red)
                        amadeaOffensiveX_font = my_font1.render("Off range X: " + str(amadea.offensive_range.rangeX), 1,
                                                                red)
                        amadeaOffensiveY_font = my_font1.render("Off range Y: " + str(amadea.offensive_range.rangeY), 1,
                                                                red)
                        amadeaDefensive_font = my_font1.render("Def range Y: " + str(amadea.defensive_range.therangeY), 1,
                                                               red)

                        screen.blit(amadea_font, (display_width1 * 0.81, display_height1 * 0.205))
                        screen.blit(amadeaHP_font, (display_width1 * 0.70, display_height1 * 0.21))
                        screen.blit(amadeaSteps_font, (display_width1 * 0.70, display_height1 * 0.24))
                        screen.blit(amadeaMaxSteps_font, (display_width1 * 0.70, display_height1 * 0.27))
                        screen.blit(amadeaDamage_font, (display_width1 * 0.70, display_height1 * 0.30))
                        screen.blit(amadeaOffensiveX_font, (display_width1 * 0.70, display_height1 * 0.33))
                        screen.blit(amadeaOffensiveY_font, (display_width1 * 0.70, display_height1 * 0.36))
                        screen.blit(amadeaDefensive_font, (display_width1 * 0.70, display_height1 * 0.385))



                    elif events.key == pygame.K_UP and boat5bol == True and santa_bettina.maxsteps.stepadd() and aboat5.leady > 106:
                        aboat5.leady -= 35.5
                        santa_bettina.maxsteps.steps += 1
                    elif events.key == pygame.K_DOWN and boat5bol == True and santa_bettina.maxsteps.stepadd() and aboat5.leady < 700:
                        aboat5.leady += 35.5
                        santa_bettina.maxsteps.steps += 1
                    elif events.key == pygame.K_LEFT and boat5bol == True and santa_bettina.maxsteps.stepadd() and aboat5.leadx > 120:
                        aboat5.leadx -= 33
                        santa_bettina.maxsteps.steps += 1
                    elif events.key == pygame.K_RIGHT and boat5bol == True and santa_bettina.maxsteps.stepadd() and aboat5.leadx < 738:
                        aboat5.leadx += 33
                        santa_bettina.maxsteps.steps += 1
                    elif events.key == pygame.K_UP and boat6bol == True and windsurf.maxsteps.stepadd() and aboat6.leady > 106:
                        aboat6.leady -= 35.5
                        windsurf.maxsteps.steps += 1
                    elif events.key == pygame.K_DOWN and boat6bol == True and windsurf.maxsteps.stepadd() and aboat6.leady < 660:
                        aboat6.leady += 35.5
                        windsurf.maxsteps.steps += 1
                    elif events.key == pygame.K_LEFT and boat6bol == True and windsurf.maxsteps.stepadd() and aboat6.leadx > 112:
                        aboat6.leadx -= 33
                        windsurf.maxsteps.steps += 1
                    elif events.key == pygame.K_RIGHT and boat6bol == True and windsurf.maxsteps.stepadd()  and aboat6.leadx < 738:
                        aboat6.leadx += 33
                        windsurf.maxsteps.steps += 1
                    elif events.key == pygame.K_UP and boat7bol == True and intensity.maxsteps.stepadd() and aboat7.leady > 106:
                        aboat7.leady -= 35.5
                        intensity.maxsteps.steps += 1
                    elif events.key == pygame.K_DOWN and boat7bol == True and intensity.maxsteps.stepadd() and aboat7.leady < 650:
                        aboat7.leady += 35.5
                        intensity.maxsteps.steps += 1
                    elif events.key == pygame.K_LEFT and boat7bol == True and intensity.maxsteps.stepadd()  and aboat7.leadx > 112:
                        aboat7.leadx -= 33
                        intensity.maxsteps.steps += 1
                    elif events.key == pygame.K_RIGHT and boat7bol == True and intensity.maxsteps.stepadd() and aboat7.leadx < 738:
                        aboat7.leadx += 33
                        intensity.maxsteps.steps += 1
                    elif events.key == pygame.K_UP and boat8bol == True  and amadea.maxsteps.stepadd()  and aboat8.leady > 106:
                        aboat8.leady -= 35.5
                        amadea.maxsteps.steps += 1
                    elif events.key == pygame.K_DOWN and boat8bol == True and amadea.maxsteps.stepadd()  and aboat8.leady < 635:
                        aboat8.leady += 35.5
                        amadea.maxsteps.steps += 1
                    elif events.key == pygame.K_LEFT and boat8bol == True and amadea.maxsteps.stepadd() and aboat8.leadx > 112:
                        aboat8.leadx -= 33
                        amadea.maxsteps.steps += 1
                    elif events.key == pygame.K_RIGHT and boat8bol == True and amadea.maxsteps.stepadd()  and aboat8.leadx < 738:
                        aboat8.leadx += 33
                        amadea.maxsteps.steps += 1
                    if aboat5.leady > 690:
                        specialboat5 = True
                        if sb5 == 1:
                            effect17.play()
                            sb5 = 0
                    if aboat6.leady > 650:
                        specialboat6 = True
                        if sb6 == 1:
                            effect17.play()
                            sb6 = 0
                    if aboat7.leady > 640:
                        specialboat7 = True
                        if sb7 == 1:
                            effect17.play()
                            sb7 = 0
                    if aboat8.leady > 625:
                        specialboat8 = True
                        if sb8 == 1:
                            effect17.play()
                            sb8 = 0



                    if events.key == pygame.K_1:
                        if len(player2_normalcards) > 0:
                            card_show(player2_normalcards [0])
                            effect3.play()
                        else:
                            menu_image29 = pygame.image.load('empty_card.png')
                            screen.blit(menu_image29, (display_width1 * 0.769, display_height1 * 0.4276))
                    elif events.key == pygame.K_2:
                        if len(player2_normalcards) > 1:
                            card_show(player2_normalcards [1])
                            effect4.play()
                        else:
                            menu_image29 = pygame.image.load('empty_card.png')
                            screen.blit(menu_image29, (display_width1 * 0.769, display_height1 * 0.4276))
                    elif events.key == pygame.K_3:
                        if len(player2_normalcards) > 2:
                            card_show(player2_normalcards [2])
                            effect5.play()
                        else:
                            menu_image29 = pygame.image.load('empty_card.png')
                            screen.blit(menu_image29, (display_width1 * 0.769, display_height1 * 0.4276))
                    elif events.key == pygame.K_4:
                        if len(player2_normalcards) > 3:
                            card_show(player2_normalcards [3])
                            effect6.play()
                        else:
                            menu_image29 = pygame.image.load('empty_card.png')
                            screen.blit(menu_image29, (display_width1 * 0.769, display_height1 * 0.4276))
                    elif events.key == pygame.K_5:
                        if len(player2_normalcards) > 4:
                            card_show(player2_normalcards [4])
                            effect7.play()
                        else:
                            menu_image29 = pygame.image.load('empty_card.png')
                            screen.blit(menu_image29, (display_width1 * 0.769, display_height1 * 0.4276))
                    elif events.key == pygame.K_6:
                        if len(player2_normalcards) > 5:
                            card_show(player2_normalcards [5])
                            effect8.play()
                        else:
                            menu_image29 = pygame.image.load('empty_card.png')
                            screen.blit(menu_image29, (display_width1 * 0.769, display_height1 * 0.4276))
                    elif events.key == pygame.K_7:
                        if len(player2_trapcards) > 0:
                            card_show(player2_trapcards [0])
                            effect13.play()
                        else:
                            menu_image29 = pygame.image.load('empty_card.png')
                            screen.blit(menu_image29, (display_width1 * 0.769, display_height1 * 0.4276))
                    elif events.key == pygame.K_8:
                        if len(player2_trapcards) > 1:
                            card_show(player2_trapcards [1])
                            effect14.play()
                        else:
                            menu_image29 = pygame.image.load('empty_card.png')
                            screen.blit(menu_image29, (display_width1 * 0.769, display_height1 * 0.4276))
                    elif events.key == pygame.K_9:
                        if len(player2_trapcards) > 2:
                            card_show(player2_trapcards [2])
                            effect15.play()
                        else:
                            menu_image29 = pygame.image.load('empty_card.png')
                            screen.blit(menu_image29, (display_width1 * 0.769, display_height1 * 0.4276))
                    elif events.key == pygame.K_0:
                        if len(player2_trapcards) > 3:
                            card_show(player2_trapcards [3])
                            effect16.play()
                        else:
                            menu_image29 = pygame.image.load('empty_card.png')
                            screen.blit(menu_image29, (display_width1 * 0.769, display_height1 * 0.4276))
                        menu_image29 = pygame.image.load('empty_card.png')
                        screen.blit(menu_image29, (display_width1 * 0.769, display_height1 * 0.4276))

                    elif events.key == pygame.K_p:
                            activate_card()

                    elif events.key == pygame.K_r:
                        boat1_trigger = True
                    elif events.key == pygame.K_t:
                        boat2_trigger = True
                    elif events.key == pygame.K_y:
                        boat3_trigger = True
                    elif events.key == pygame.K_u:
                        boat4_trigger = True





                        # boat 2 on 2 squares boat 1 on boat 5 PERFECT
                    if boat5bol == True and boat1_trigger == True and santa_bettina.offensive_rangebol == True:
                        if abs(aboat5.leadx + (santa_bettina.offensive_range.rangeX * 2) - aboat5.leadx) <= 70:
                            if abs(aboat5.leady - aboat1.leady) < 0.20:
                                if events.key == pygame.K_SPACE:
                                    fungo_saltire.health -= santa_bettina.damage
                                    screen.fill(red)
                                    boat1_trigger = False
                        if abs(aboat5.leady + (santa_bettina.offensive_range.rangeY * 1) - aboat1.leady) <= 100:
                            if abs(aboat5.leadx - aboat1.leadx) < 2:
                                if events.key == pygame.K_SPACE:
                                    fungo_saltire.health -= santa_bettina.damage
                                    screen.fill(red)
                                    boat1_trigger = False
                                    # boat 2squares on 3 squares, boat 1 on boat 6 PERFECT
                    if boat5bol == True and boat2_trigger == True and santa_bettina.offensive_rangebol == True:
                        if abs(aboat5.leadx + (santa_bettina.offensive_range.rangeX * 2) - aboat2.leadx) <= 70:
                            if abs(aboat5.leady - aboat2.leady) < 50:
                                if events.key == pygame.K_SPACE:
                                    silver_whisper.health -= santa_bettina.damage
                                    screen.fill(red)
                                    boat6_trigger = False
                        if abs(aboat5.leady + (santa_bettina.offensive_range.rangeY * 1) - aboat2.leady) <= 125:
                            if abs(aboat5.leadx - aboat2.leadx) < 2:
                                if events.key == pygame.K_SPACE:
                                    silver_whisper.health -= santa_bettina.damage
                                    screen.fill(red)
                                    boat2_trigger = False
                                    # boat 1 on boat 7 2 squares on 3 squares perfect
                    if boat5bol == True and boat3_trigger == True and santa_bettina.offensive_rangebol == True:
                        if abs(aboat5.leadx + (santa_bettina.offensive_range.rangeX * 2) - aboat3.leadx) <= 70:
                            if abs(aboat5.leady - aboat3.leady) < 50:
                                if events.key == pygame.K_SPACE:
                                    sea_spirit.health -= santa_bettina.damage
                                    screen.fill(red)
                                    boat7_trigger = False
                        if abs(aboat5.leady + (santa_bettina.offensive_range.rangeY * 1) - aboat3.leady) <= 125:
                            if abs(aboat5.leadx - aboat3.leadx) < 2:
                                if events.key == pygame.K_SPACE:
                                    sea_spirit.health -= santa_bettina.damage
                                    screen.fill(red)
                                    boat3_trigger = False
                                    # boat 1 on boat 8 2 squares on 4 squares PERFECT
                    if boat5bol == True and boat4_trigger == True and santa_bettina.offensive_rangebol == True:
                        if abs(aboat5.leadx + (santa_bettina.offensive_range.rangeX * 2) - aboat4.leadx) <= 70:
                            if abs(aboat5.leady - aboat4.leady) < 75:
                                if events.key == pygame.K_SPACE:
                                    merapi.health -=  santa_bettina.damage
                                    screen.fill(red)
                                    boat4_trigger = False
                        if abs(aboat5.leady + (santa_bettina.offensive_range.rangeY * 1) - aboat4.leady) <= 150:
                            if abs(aboat5.leadx - aboat4.leadx) < 2:
                                if events.key == pygame.K_SPACE:
                                    merapi.health -= santa_bettina.damage
                                    screen.fill(red)
                                    boat4_trigger = False

                screen.blit(menu_image31, (display_width1 * 0.70, display_height1 * 0.01))


            elif events.type == pygame.MOUSEBUTTONDOWN:
                print(MouseX, MouseY)
                print ("Mouse Button up")

            elif events.type == pygame.MOUSEBUTTONUP:
                print(MouseX, MouseY)
                print ("Mouse Button down")

            elif events.type == pygame.MOUSEMOTION:
                print ("mouse at " + " " + str(MouseX) +  " " + str(MouseY))


            screen.blit(aboat11, (aboat1.leadx, aboat1.leady))
            screen.blit(aboat12, (aboat2.leadx, aboat2.leady))
            screen.blit(aboat13, (aboat3.leadx, aboat3.leady))
            screen1.blit(aboat14, (aboat4.leadx, aboat4.leady))
            screen.blit(aboat15, (aboat5.leadx, aboat5.leady))
            screen.blit(aboat16, (aboat6.leadx, aboat6.leady))
            screen.blit(aboat17, (aboat7.leadx, aboat7.leady))

            screen.blit(aboat18, (aboat8.leadx, aboat8.leady))
            screen.blit(menu_image32, (display_width1 * 0.69, display_height1 * 0.58))
            screen.blit(menu_image33, (display_width1 * 0.69, display_height1 * 0.15))

            print(player1winner.score)
            print(player2winner.score)
            the_map_click(MouseX, MouseY)
            (MouseX, MouseY) = pygame.mouse.get_pos()


        pygame.display.update()


def the_startfunction():
    global the_player_1
    global the_player_2

    ''''Connection to database to store the name'''
    connection = psycopg2.connect(host= "localhost", database="postgres", user= "postgres", password="WallSpeaker5" ) #to login
    connection.autocommit = True #thanks to this it will automaticly add the rows
    cur = connection.cursor() #defines a cursor to work with


    ''''Everything with 6 added'''

    '''FPS clock'''
    fps = clock(60)

    ''''Canvas'''
    pygame.display.set_caption("Menu")
    screen6 = pygame.display.set_mode((display_width , display_height))
    pygame.display.update()

    ''''The image canvas/window'''
    the_image6 = "start.jpg"
    screen_image6 = pygame.display.set_mode((display_width , display_height))
    menu_image6 =  pygame.image.load(the_image6)
    screen_image6.blit(menu_image6,(0,0))

    ''''Black to remove letter reapearing'''
    menu_image5 = pygame.image.load("black1.png")
    menu_image5 = pygame.transform.scale(menu_image5, (display_width // 2, display_height // 3))
    screen6.blit(menu_image5, (display_width * 0.10, display_height * 0.30))

    menu_image6 = pygame.image.load("black1.png")
    menu_image6 = pygame.transform.scale(menu_image5, (display_width // 100, display_height // 100))

    ''''User enter name'''
    textinput = pygame_textinput.TextInput()


    ''''Font'''
    pygame.display.set_caption("Font") #creates the canves for the fonts
    my_font = pygame.font.Font(None,50) # stores the fond module in my_font
    my_font1 = pygame.font.Font(None,35) # stores the fond module in my_font
    start_font = my_font.render("Start",1,white)
    theplayer1message_font = my_font1.render("Player 1",1,white)
    theplayer2message_font = my_font1.render("Player 2", 1, white)

    player1message2_font = my_font1.render("Enter your firstname below", 1, white)
    player1message3_font = my_font1.render("__________", 1, white)
    # back6_font = my_font.render("Back", 1, red)


    ''''The mouse'''
    (MouseX, MouseY) = pygame.mouse.get_pos()





    ''''The loop to keep the menu open'''
    def player2loop():
        global the_player_1
        global the_player_2
        screen6.fill(black)
        screen6.blit(theplayer2message_font, (270, 100))
        screen6.blit(start_font, (275, 10))
        screen6.blit(player1message2_font, (160, 130))
        screen6.blit(player1message3_font, (250, 185))
        # screen6.blit(back6_font, (270, 400))


        player2 = True
        while player2 == True:
            event = pygame.event.get()
            for events in event:
                if events.type == pygame.QUIT:
                    pygame.quit(); sys.exit()
                if pygame.key.get_pressed()[pygame.K_RETURN] == True:
                    the_player_2 = textinput.get_text() #STORES NAME
                    the_gamefunction()


                elif events.type == pygame.MOUSEBUTTONDOWN:
                    print(MouseX, MouseY)
                    print ("Mouse Button up")
                elif events.type == pygame.MOUSEBUTTONUP:
                    print(MouseX, MouseY) #test to see if is stored



                elif events.type == pygame.MOUSEMOTION:
                    print ("mouse at " + " " + str(MouseX) +  " " + str(MouseY))

                (MouseX, MouseY) = pygame.mouse.get_pos()


            textinput.update(event)
            screen_image6.blit(textinput.get_surface(), (224, 185))
            pygame.display.update()
            screen6.blit(menu_image5, (display_width * 0.35, display_height * 0.35))



    def player1loop():
        global the_player_1
        global the_player_2

        (MouseX, MouseY) = pygame.mouse.get_pos()
        ''''Fonts'''
        screen6.blit(theplayer1message_font, (270, 100))
        screen6.blit(start_font, (275, 10))
        screen6.blit(player1message2_font, (160, 130))
        screen6.blit(player1message3_font, (250, 185))
        # screen6.blit(back6_font, (270, 400))


        player1 = True
        while player1 == True: #The loop to keep the menu open, if the user clicks on the exit screen, the menu will stop.
            event = pygame.event.get()
            for events in event:
                if events.type == pygame.QUIT: #if the arrow is pressed, they game quits
                    pygame.quit(); sys.exit()
                if pygame.key.get_pressed()[pygame.K_RETURN] == True: #when user presses enter, the input text will print
                    # print(textinput.get_text()) #backup print
                    the_player_1 = textinput.get_text() #STORES NAME
                    player2loop()


                elif events.type == pygame.MOUSEBUTTONDOWN:
                    print(MouseX, MouseY)
                    print ("Mouse Button up")
                elif events.type == pygame.MOUSEBUTTONUP:
                    print(MouseX, MouseY) #test to see if is stored



                elif events.type == pygame.MOUSEMOTION:
                    print ("mouse at " + " " + str(MouseX) +  " " + str(MouseY))

                (MouseX, MouseY) = pygame.mouse.get_pos()


            textinput.update(event)
            screen_image6.blit(textinput.get_surface(), (224, 185))
            pygame.display.update()
            screen6.blit(menu_image5, (display_width * 0.35, display_height * 0.35))
            screen6.blit(menu_image5, (display_width * 0.30, display_height * 0.50)) #black to hide player title

    player1loop()


def the_playersfunction():
    ''''Everyhing with 2 added '''

    ''''FPS Clock'''
    fps1 = clock(60)

    ''''Canvas'''
    pygame.display.set_caption("Players")
    screen2 = pygame.display.set_mode((display_width, display_height))
    pygame.display.update()

    ''''Background image'''
    the_image2 = "players.jpg"
    screen_image2 = pygame.display.set_mode((display_width, display_height))
    menu_image2 = pygame.image.load(the_image2)
    screen_image2.blit(menu_image2, (0, 0))

    ''''The images (human and AI)'''
    menu_image3 = pygame.image.load("human.jpg")
    menu_image3 = pygame.transform.scale(menu_image3, (display_width // 6, display_height // 4))
    menu_image4 = pygame.image.load("AI.jpg")
    menu_image4 = pygame.transform.scale(menu_image4, (display_width // 5, display_height // 4))
    menu_image5 = pygame.image.load("black.jpeg")
    menu_image5 = pygame.transform.scale(menu_image5, (display_width // 3, display_height // 6))

    ''''Fonts'''
    pygame.display.set_caption("Font")
    my_font = pygame.font.Font(None, 50)
    players_font = my_font.render("Players", 1, white)
    two_players_font = my_font.render("2 players", 1, white)
    ai_font = my_font.render("AI", 1, white)
    back2_myfont = my_font.render("Back", 1, red)
    playerpick_font = my_font.render("2 players", 1, white)
    aipick_font = my_font.render("AI", 1, white)

    # imports the letters
    screen2.blit(players_font, (260, 10))
    screen2.blit(two_players_font, (180, 100))
    screen2.blit(ai_font, (390, 100))
    screen2.blit(back2_myfont, (270, 410))

    ''''Title positions'''
    players_title = title_position(180, 340, 100, 270)
    ai_title = title_position(340, 470, 100, 270)
    players_back_title = title_position(270, 360, 405, 450)

    def the_players_click(posx, posy):
        playerclick = False
        AIclick = False
        if posx > players_title.beginX and posx < players_title.endX and posy > players_title.beginY and posy < players_title.endY:
            the_players_title = figure(screen_image2, red, black, 175, 90, 160, 185, 1)

            screen2.blit(menu_image5, (display_width * 0.35, display_height * 0.65))
            screen2.blit(playerpick_font, (260, 350))
            print("players")
            if events.type == pygame.MOUSEBUTTONDOWN and events.button == 1:
                effect1.play()
                the_startfunction()

                playerlick = True
                AIclick = False
                if AIclick == False:
                    screen2.blit(menu_image5, (display_width * 0.35, display_height * 0.65))
                    screen2.blit(playerpick_font, (260, 350))

        elif posx > ai_title.beginX and posx < ai_title.endX and posy > ai_title.beginY and posy < ai_title.endY:
            the_ai_title = figure(screen_image2, red, black, 330, 90, 140, 185, 1)


            screen2.blit(menu_image5, (display_width * 0.35, display_height * 0.65))
            screen2.blit(aipick_font, (300, 350))
            print("AI")
            if events.type == pygame.MOUSEBUTTONDOWN and events.button == 1:
                effect1.play()
                AIclick = True
                playerlick = False
                if playerclick == False:
                    screen2.blit(menu_image5, (display_width * 0.35, display_height * 0.65))
                    screen2.blit(aipick_font, (300, 350))


        elif posx > players_back_title.beginX and posx < players_back_title.endX and posy > players_back_title.beginY and posy < players_back_title.endY:
            the_back1_title = figure(screen_image2, red, black, 260, 400, 100, 50, 1)
            print("Back")
            if events.type == pygame.MOUSEBUTTONDOWN and events.button == 1:
                effect1.play()
                the_menufunction()

    ''''Mouse'''
    (MouseX, MouseY) = pygame.mouse.get_pos()

    players = True
    while players == True:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit();
                sys.exit()

            elif events.type == pygame.MOUSEBUTTONDOWN:
                print(MouseX, MouseY)
                print("Mouse Button up")
            elif events.type == pygame.MOUSEBUTTONUP:
                print(MouseX, MouseY)
                print("Mouse Button down")

            elif events.type == pygame.MOUSEMOTION:
                print("mouse at " + " " + str(MouseX) + " " + str(MouseY))

            screen2.blit(menu_image3, (display_width * 0.30, display_height * 0.30))
            screen2.blit(menu_image4, (display_width * 0.53, display_height * 0.30))
            the_players_click(MouseX, MouseY)
            (MouseX, MouseY) = pygame.mouse.get_pos()

        pygame.display.update()

def Rule_Page_8():
    import pygame
    pygame.init()

    white = (255, 255, 255)
    grey = (100, 100, 100)
    buttonshade = (160, 160, 160)
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 150, 255)

    screen_width = 640
    screen_height = 480

    gameScreen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Rulepage 8')

    def text_objects(text, font):
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()

    def message_display(text):
        TextSurf, TextRect = text_objects(text)
        gameScreen.blit(TextSurf, TextRect)

    def button(message, x, y, width, height, fc, sc):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x + width > mouse[0] > x and y + height > mouse[1] > y:  # checks if the mouse is over the button
            pygame.draw.rect(gameScreen, sc, (x, y, width, height))
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                the_menufunction()
                # gameScreen.fill(black)
                print("you clicked next")   #TODO dit moet de user terugsturen naar het hoofdmenu waar hij/zij een nieuw spel kan starten bijv
        else:
            pygame.draw.rect(gameScreen, fc, (x, y, width, height))

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

        gameScreen.fill(grey)

        myfont = pygame.font.SysFont("ariel", 30)
        button("Back to Menu", 465, 400, 150, 30, white, buttonshade)

        smallText = pygame.font.SysFont('None', 30)
        TextSurf, TextRect = text_objects("Back to Menu", smallText)
        TextRect.center = (535, 415)
        gameScreen.blit(TextSurf, TextRect)

        # below are text rectangles
        label = myfont.render("Controls", 1, white)
        gameScreen.blit(label, (180, 5))
        rule1 = myfont.render("- Changing stances", 1, white)
        gameScreen.blit(rule1, (30, 75))
        rule2 = myfont.render(" Defensive : G", 1, white)
        gameScreen.blit(rule2, (30, 100))
        rule3 = myfont.render("- Offensive : H", 1, white)
        gameScreen.blit(rule3, (30, 150))
        rule4 = myfont.render("- To activate a card, first press the card then the boat and then P", 1, white)
        gameScreen.blit(rule4, (30, 200))



        page_number = myfont.render("Page 8", 1, white)
        gameScreen.blit(page_number, (30, 400))

        pygame.display.update()

    pygame.quit()
    quit()

def Rule_Page_7():
    import pygame

    pygame.init()

    # below are the definitions of the colours white, black, red, green,etc you can use them by name
    white = (255, 255, 255)
    grey = (100, 100, 100)
    buttonshade = (160, 160, 160)
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 150, 255)



    screen_width = 640
    screen_height = 480

    gameScreen = pygame.display.set_mode((screen_width, screen_height))  # resolution of the screen set to x, x pixels you can use 1920,1080 for full screen if you have a 1080p screen
    pygame.display.set_caption('Rulepage 7')  # this is the name of the window. feel free to change it and see what happens (with change i mean everything in between ' ')

    def text_objects(text, font):
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()

    def message_display(text):
        TextSurf, TextRect = text_objects(text)
        gameScreen.blit(TextSurf, TextRect)

    def button(message, x, y, width, height, fc, sc):  # use this as parameters for a button fc = first colour sc= second colour (because i changes colour when you hoverover it
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x + width > mouse[0] > x and y + height > mouse[1] > y:  # checks if the mouse is over the button
            pygame.draw.rect(gameScreen, sc, (x, y, width, height))
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                gameScreen.fill(black)
                Rule_Page_8()   #TODO dit moet de user terugsturen naar het hoofdmenu waar hij/zij een nieuw spel kan starten bijv
        else:
            pygame.draw.rect(gameScreen, fc, (x, y, width, height))

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

        gameScreen.fill(grey)

        myfont = pygame.font.SysFont("ariel", 30)
        button("Next", 500, 400, 70, 30, white, buttonshade)

        smallText = pygame.font.SysFont('None', 30)
        TextSurf, TextRect = text_objects("Next", smallText)
        TextRect.center = (535, 415)
        gameScreen.blit(TextSurf, TextRect)

        # below are text rectangles
        label = myfont.render("Controls", 1, white)
        gameScreen.blit(label, (180, 5))
        rule1 = myfont.render("- Player 1 movement : WASD", 1, white)
        gameScreen.blit(rule1, (30, 75))
        rule2 = myfont.render(" Boat selection R, T, Y and U", 1, white)
        gameScreen.blit(rule2, (30, 100))
        rule3 = myfont.render("- Player 2 movement : Arrow keys", 1, white)
        gameScreen.blit(rule3, (30, 150))
        rule4 = myfont.render("-Boat selection V, B, N and M", 1, white)
        gameScreen.blit(rule4, (30, 175))
        rule4 = myfont.render("-Normal card selection : 1 - 6", 1, white)
        gameScreen.blit(rule4, (30, 225))
        rule4 = myfont.render("-Special card selection 7 - 0", 1, white)
        gameScreen.blit(rule4, (30, 275))
        rule4 = myfont.render("-Attack:Choose friendly OR enemy boat and then press space", 1, white)
        gameScreen.blit(rule4, (30, 325))


        page_number = myfont.render("Page 7", 1, white)
        gameScreen.blit(page_number, (30, 400))

        pygame.display.update()

    pygame.quit()
    quit()

def Rule_Page_6():
    import pygame

    pygame.init()

    # below are the definitions of the colours white, black, red, green,etc you can use them by name
    white = (255, 255, 255)
    grey = (100, 100, 100)
    buttonshade = (160, 160, 160)
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 150, 255)


    screen_width = 640
    screen_height = 480

    gameScreen = pygame.display.set_mode((screen_width,screen_height))  # resolution of the screen set to x, x pixels you can use 1920,1080 for full screen if you have a 1080p screen
    pygame.display.set_caption('Rulepage 6')  # this is the name of the window. feel free to change it and see what happens (with change i mean everything in between ' ')

    def text_objects(text, font):
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()

    def message_display(text):
        TextSurf, TextRect = text_objects(text)
        gameScreen.blit(TextSurf, TextRect)

    def button(message, x, y, width, height, fc, sc):  # use this as parameters for a button fc = first colour sc= second colour (because i changes colour when you hoverover it
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x + width > mouse[0] > x and y + height > mouse[1] > y:  # checks if the mouse is over the button
            pygame.draw.rect(gameScreen, sc, (x, y, width, height))
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                gameScreen.fill(black)
                Rule_Page_7()
        else:
            pygame.draw.rect(gameScreen, fc, (x, y, width, height))

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

        gameScreen.fill(grey)

        myfont = pygame.font.SysFont("ariel", 30)
        button("Next", 500, 400, 70, 30, white, buttonshade)

        smallText = pygame.font.SysFont('None', 30)
        TextSurf, TextRect = text_objects("Next", smallText)
        TextRect.center = (535, 415)
        gameScreen.blit(TextSurf, TextRect)

        # below are text rectangles
        label = myfont.render("Card description - Utility", 1, white)
        gameScreen.blit(label, (180, 5))
        rule1 = myfont.render("- Backup : draw 1 cards", 1, white)
        gameScreen.blit(rule1, (30, 100))
        rule2 = myfont.render("- Extra fuel : 1 ship gets +2 moves", 1, white)
        gameScreen.blit(rule2, (30, 150))
        rule3 = myfont.render("- Adrenaline rush : double a ship's total moves", 1, white)
        gameScreen.blit(rule3, (30, 200))
        rule4 = myfont.render("- Rally : double a ships total moves", 1, white)
        gameScreen.blit(rule4, (30, 250))

        page_number = myfont.render("Page 6", 1, white)
        gameScreen.blit(page_number, (30, 400))

        pygame.display.update()

    pygame.quit()
    quit()

def Rule_Page_5():
    import pygame

    pygame.init()

    # below are the definitions of the colours white, black, red, green,etc you can use them by name
    white = (255, 255, 255)
    grey = (100, 100, 100)
    buttonshade = (160, 160, 160)
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 150, 255)

    screen_width = 640
    screen_height = 480

    gameScreen = pygame.display.set_mode((screen_width,screen_height))  # resolution of the screen set to x, x pixels you can use 1920,1080 for full screen if you have a 1080p screen
    pygame.display.set_caption('Rulepage 5')  # this is the name of the window. feel free to change it and see what happens (with change i mean everything in between ' ')

    def text_objects(text, font):
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()

    def message_display(text):
        TextSurf, TextRect = text_objects(text)
        gameScreen.blit(TextSurf, TextRect)

    def button(message, x, y, width, height, fc, sc):  # use this as parameters for a button fc = first colour sc= second colour (because i changes colour when you hoverover it
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x + width > mouse[0] > x and y + height > mouse[1] > y:  # checks if the mouse is over the button
            pygame.draw.rect(gameScreen, sc, (x, y, width, height))
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                Rule_Page_6()
                print("you clicked next")
        else:
            pygame.draw.rect(gameScreen, fc, (x, y, width, height))

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

        gameScreen.fill(grey)

        myfont = pygame.font.SysFont("ariel", 30)
        button("Next", 500, 400, 70, 30, white, buttonshade)  # This button changes from white to grey when you hover over it

        smallText = pygame.font.SysFont('None', 30)
        TextSurf, TextRect = text_objects("Next", smallText)
        TextRect.center = (535, 415)
        gameScreen.blit(TextSurf, TextRect)

        # below are text rectangles
        label = myfont.render("Card description - Defensive", 1, white)
        gameScreen.blit(label, (180, 5))
        rule1 = myfont.render("- Reinforced hull : your ship has +1 health", 1, white)
        gameScreen.blit(rule1, (30, 100))
        rule2 = myfont.render("- Sonar : disable a mine (TRAPCARD)", 1, white)
        gameScreen.blit(rule2, (30, 150))
        rule3 = myfont.render("Special: When the player reaches the other side,", 1, white)
        gameScreen.blit(rule3, (30, 200))
        rule100 = myfont.render("He is allowed to grab from the special(spc) deck", 1, white)
        gameScreen.blit(rule100, (30, 220))
        # rule4 = myfont.render("Special: When the player reaches the other side, he is allowed to grab from the special (spc) deck", 1, white)

        page_number = myfont.render("Page 5", 1, white)
        gameScreen.blit(page_number, (30, 400))

        pygame.display.update()

    pygame.quit()
    quit()

def Rule_Page_4():
    import pygame

    pygame.init()

    # below are the definitions of the colours white, black, red, green,etc you can use them by name
    white = (255, 255, 255)
    grey = (100, 100, 100)
    buttonshade = (160, 160, 160)
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 150, 255)

    screen_width = 640
    screen_height = 480

    gameScreen = pygame.display.set_mode((screen_width, screen_height))  # resolution of the screen set to x, x pixels you can use 1920,1080 for full screen if you have a 1080p screen
    pygame.display.set_caption('Rulepage 4')  # this is the name of the window. feel free to change it and see what happens (with change i mean everything in between ' ')

    def text_objects(text, font):
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()

    def message_display(text):
        TextSurf, TextRect = text_objects(text)
        gameScreen.blit(TextSurf, TextRect)

    def button(message, x, y, width, height, fc,sc):  # use this as parameters for a button fc = first colour sc= second colour (because i changes colour when you hoverover it
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x + width > mouse[0] > x and y + height > mouse[1] > y:  # checks if the mouse is over the button
            pygame.draw.rect(gameScreen, sc, (x, y, width, height))
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                Rule_Page_5()
                print("you clicked next")
        else:
            pygame.draw.rect(gameScreen, fc, (x, y, width, height))

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

        gameScreen.fill(grey)

        myfont = pygame.font.SysFont("ariel", 30)
        button("Next", 500, 400, 70, 30, white, buttonshade)  # This button changes from white to grey when you hover over it

        smallText = pygame.font.SysFont('None', 30)
        TextSurf, TextRect = text_objects("Next", smallText)
        TextRect.center = (535, 415)
        gameScreen.blit(TextSurf, TextRect)

        # below are text rectangles
        label = myfont.render("Card description - Offensive", 1, white)
        gameScreen.blit(label, (180, 5))
        rule1 = myfont.render("- FMJ card : your next attack does +1 dmg", 1, white)
        gameScreen.blit(rule1, (30, 100))
        rule2 = myfont.render("- Rifling card : your next attack has +1 range", 1, white)
        gameScreen.blit(rule2, (30, 150))
        rule3 = myfont.render("- Rifling + card : your next attack has +2 range", 1, white)
        gameScreen.blit(rule3, (30, 200))
        # rule4 = myfont.render("- Naval mine : activate a mine (TRAPCARD)", 1, white)
        # gameScreen.blit(rule4, (30, 250))
        rule5 = myfont.render("- EMP upgrade : next attack on your ship has no effect", 1, white)

        page_number = myfont.render("Page 4", 1, white)
        gameScreen.blit(page_number, (30, 400))

        pygame.display.update()

    pygame.quit()
    quit()

def Rule_Page_3():
    import pygame

    pygame.init()

    # below are the definitions of the colours white, black, red, green,etc you can use them by name
    white = (255, 255, 255)
    grey = (100, 100, 100)
    buttonshade = (160, 160, 160)
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 150, 255)

    screen_width = 640
    screen_height = 480

    gameScreen = pygame.display.set_mode((screen_width, screen_height))  # resolution of the screen set to x, x pixels you can use 1920,1080 for full screen if you have a 1080p screen
    pygame.display.set_caption('Rulepage 3')  # this is the name of the window. feel free to change it and see what happens (with change i mean everything in between ' ')

    def text_objects(text, font):
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()

    def message_display(text):
        TextSurf, TextRect = text_objects(text)
        gameScreen.blit(TextSurf, TextRect)

    def button(message, x, y, width, height, fc, sc):  # use this as parameters for a button fc = first colour sc= second colour (because i changes colour when you hoverover it
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x + width > mouse[0] > x and y + height > mouse[1] > y:  # checks if the mouse is over the button
            pygame.draw.rect(gameScreen, sc, (x, y, width, height))
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                Rule_Page_4()
                print("you clicked next")
        else:
            pygame.draw.rect(gameScreen, fc, (x, y, width, height))

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

        gameScreen.fill(grey)

        myfont = pygame.font.SysFont("ariel", 30)
        button("Next", 500, 400, 70, 30, white, buttonshade)  # This button changes from white to grey when you hover over it

        smallText = pygame.font.SysFont('None', 30)
        TextSurf, TextRect = text_objects("Next", smallText)
        TextRect.center = (535, 415)
        gameScreen.blit(TextSurf, TextRect)

        # below are text rectangles
        label = myfont.render("INTRODUCTION", 1, white)
        gameScreen.blit(label, (180, 5))
        rule1 = myfont.render("- Players may attack 2 times during their turn", 1, white)
        gameScreen.blit(rule1, (30, 100))
        rule2 = myfont.render("  each ship may attack only once ", 1, white)
        gameScreen.blit(rule2, (30, 125))
        rule3 = myfont.render("  you can only attack the enemy if he is inside your range", 1, white)
        gameScreen.blit(rule3, (30, 150))
        rule4 = myfont.render("- Each ship has a base health according to its size ", 1, white)
        gameScreen.blit(rule4, (30, 200))
        rule5 = myfont.render(" a ship that is 4 blocks tall has 4 hp, etc ", 1, white)
        gameScreen.blit(rule5, (30, 225))
        rule6 = myfont.render("- Upon destruction, ships remain on the battlefield ", 1, white)
        gameScreen.blit(rule6, (30, 275))


        page_number = myfont.render("Page 3", 1, white)
        gameScreen.blit(page_number, (30, 400))

        pygame.display.update()

    pygame.quit()
    quit()

def Rule_Page_2():
    import pygame

    pygame.init()

    # below are the definitions of the colours white, black, red, green,etc you can use them by name
    white = (255, 255, 255)
    grey = (100, 100, 100)
    buttonshade = (160, 160, 160)
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 150, 255)

    screen_width = 640
    screen_height = 480

    gameScreen = pygame.display.set_mode((screen_width, screen_height))  # resolution of the screen set to x, x pixels you can use 1920,1080 for full screen if you have a 1080p screen
    pygame.display.set_caption('Rulepage 2')  # this is the name of the window. feel free to change it and see what happens (with change i mean everything in between ' ')

    def text_objects(text, font):
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()

    def message_display(text):
        TextSurf, TextRect = text_objects(text)
        gameScreen.blit(TextSurf, TextRect)

    def button(message, x, y, width, height, fc, sc):  # use this as parameters for a button fc = first colour sc= second colour (because i changes colour when you hoverover it
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x + width > mouse[0] > x and y + height > mouse[1] > y:  # checks if the mouse is over the button
            pygame.draw.rect(gameScreen, sc, (x, y, width, height))
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                Rule_Page_3()
                print("you clicked next")
        else:
            pygame.draw.rect(gameScreen, fc, (x, y, width, height))

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

        gameScreen.fill(grey)

        myfont = pygame.font.SysFont("ariel", 30)
        button("Next", 500, 400, 70, 30, white, buttonshade)  # This button changes from white to grey when you hover over it

        smallText = pygame.font.SysFont('None', 30)
        TextSurf, TextRect = text_objects("Next", smallText)
        TextRect.center = (535, 415)
        gameScreen.blit(TextSurf, TextRect)

        # below are text rectangles
        label = myfont.render("INTRODUCTION", 1, white)
        gameScreen.blit(label, (180, 5))
        rule1 = myfont.render("- Ships may change stances between defensive and offensive", 1, white)
        gameScreen.blit(rule1, (30, 100))
        rule2 = myfont.render("- Offensive ships: ", 1, white)
        gameScreen.blit(rule2, (30, 150))
        rule3 = myfont.render("  allowed to move, shorter attack range", 1, white)
        gameScreen.blit(rule3, (30, 175))
        rule4 = myfont.render("- Defensive ships ", 1, white)
        gameScreen.blit(rule4, (30, 225))
        rule5 = myfont.render(" unable to move, longer attack ranges ", 1, white)
        gameScreen.blit(rule5, (30, 250))


        page_number = myfont.render("Page 2", 1, white)
        gameScreen.blit(page_number, (30, 400))

        pygame.display.update()

    pygame.quit()
    quit()

def Rule_Page1():
    import pygame

    pygame.init()

    # below are the definitions of the colours white, black, red, green,etc you can use them by name
    white = (255, 255, 255)
    grey = (100, 100, 100)
    buttonshade = (160,160,160)
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 150, 255)


    screen_width = 640
    screen_height = 480

    gameScreen = pygame.display.set_mode((screen_width, screen_height))  # resolution of the screen set to x, x pixels you can use 1920,1080 for full screen if you have a 1080p screen
    pygame.display.set_caption('Rulepage 1')                              # this is the name of the window. feel free to change it and see what happens (with change i mean everything in between ' ')


    def text_objects(text, font):
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()


    def message_display(text):
        TextSurf, TextRect = text_objects(text)
        gameScreen.blit(TextSurf, TextRect)


    def button(message, x, y, width, height, fc,sc):  # use this as parameters for a button fc = first colour sc= second colour (because i changes colour when you hoverover it
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x + width > mouse[0] > x and y + height > mouse[1] > y:  # checks if the mouse is over the button
            pygame.draw.rect(gameScreen, sc, (x, y, width, height))
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                Rule_Page_2()
                pygame.display.update()
        else:
            pygame.draw.rect(gameScreen, fc, (x, y, width, height))


    gameExit = False



    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

        gameScreen.fill(grey)


        myfont = pygame.font.SysFont("ariel", 30)
        button("Next",500, 400, 70, 30, white, buttonshade)                        #This button changes from white to grey when you hover over it



        smallText = pygame.font.SysFont('None', 30)
        TextSurf, TextRect = text_objects("Next", smallText)
        TextRect.center = (535,415)
        gameScreen.blit(TextSurf, TextRect)

        # below are text rectangles
        label = myfont.render("INTRODUCTION", 1, white)
        gameScreen.blit(label, (180, 5))
        # rule1 = myfont.render("- Each player starts with 2 cards", 1, white)
        # gameScreen.blit(rule1, (30, 100))
        rule2 = myfont.render("- At the start of the game, players start with their ships ", 1, white)
        gameScreen.blit(rule2, (30, 150))
        rule3 = myfont.render("  rears touching the players start line", 1, white)
        gameScreen.blit(rule3, (30, 175))
        rule4 = myfont.render("- The amount of moves you are allowed to move depends ", 1, white)
        gameScreen.blit(rule4, (30, 225))
        rule5 = myfont.render(" on the size of your ship ", 1, white)
        gameScreen.blit(rule5, (30, 250))
        rule6 = myfont.render(" Ship size 2 = 3 steps ", 1, white)
        gameScreen.blit(rule6, (30, 275))
        rule7 = myfont.render(" Ship size 3 = 2 steps ", 1, white)
        gameScreen.blit(rule7, (30, 300))
        rule8 = myfont.render(" Ship size 4 = 1 step ", 1, white)
        gameScreen.blit(rule8, (30, 325))

        page_number = myfont.render("Page 1", 1, white)
        gameScreen.blit(page_number, (30, 400))


        pygame.display.update()


    pygame.quit()
    quit()

def the_highscoresfunction():
    "Everything with 4 added"

    ''''Database'''
    connection = psycopg2.connect(host="localhost", database="postgres", user="postgres",
                                  password="WallSpeaker5")  # to login
    connection.autocommit = True  # thanks to this it will automaticly add the rows
    cur = connection.cursor()  # defines a cursor to work with

    cur.execute("SELECT * FROM battleport_highscores where rank = '1' ")
    rows = cur.fetchall()
    cur.execute("SELECT * FROM battleport_highscores where rank = '2' ")
    rows1 = cur.fetchall()
    cur.execute("SELECT * FROM battleport_highscores where rank = '3' ")
    rows2 = cur.fetchall()
    cur.execute("SELECT * FROM battleport_highscores where rank = '4' ")
    rows3 = cur.fetchall()
    cur.execute("SELECT * FROM battleport_highscores where rank = '5' ")
    rows4 = cur.fetchall()
    cur.execute("SELECT * FROM battleport_highscores where rank = '6' ")
    rows5 = cur.fetchall()
    cur.execute("SELECT * FROM battleport_highscores where rank = '7' ")
    rows6 = cur.fetchall()
    cur.execute("SELECT * FROM battleport_highscores where rank = '8' ")
    rows7 = cur.fetchall()
    cur.execute("SELECT * FROM battleport_highscores where rank = '9' ")
    rows8 = cur.fetchall()
    cur.execute("SELECT * FROM battleport_highscores where rank = '10' ")
    rows9 = cur.fetchall()

    ''''FPS Clock'''
    fps1 = clock(60)

    pygame.display.set_caption("HighScores")
    screen4 = pygame.display.set_mode((display_width, display_height))
    pygame.display.update()

    ''''Background image'''
    the_image2 = "highscores.jpg"
    screen_image2 = pygame.display.set_mode((display_width, display_height))  # Window for the canvas
    menu_image2 = pygame.image.load(the_image2)  # the image (the image that will apear on the canvas
    screen_image2.blit(menu_image2, (0, 0))

    ''''Fonts'''
    pygame.display.set_caption("Font")
    my_font = pygame.font.Font(None, 50)
    my_font1 = pygame.font.Font(None, 90)
    highscores_font = my_font.render("HIGH SCORES", 1, blue)
    rank_font = my_font.render("RANK", 1, yellow)
    wins_font = my_font.render("WINS", 1, yellow)
    losses_font = my_font.render("LOSSES", 1, yellow)
    name_myfont = my_font.render("NAME", 1, yellow)
    back4_myfont = my_font.render("Back", 1, red)

    ''''Database font testing'''
    rank1_myfont1 = my_font1.render(str(rows), 1, white)
    rank1_myfont2 = my_font1.render(str(rows1), 1, white)
    rank1_myfont3 = my_font1.render(str(rows2), 1, white)
    rank1_myfont4 = my_font1.render(str(rows3), 1, white)
    rank1_myfont5 = my_font1.render(str(rows4), 1, white)


    # imports the letters
    screen4.blit(highscores_font, (210, 10))
    screen4.blit(rank_font, (10, 50))
    screen4.blit(wins_font, (350, 50))
    screen4.blit(name_myfont, (170, 50))
    screen4.blit(back4_myfont, (270, 410))
    screen4.blit(losses_font, (450, 50))


    ''''Database font testing'''
    screen4.blit(rank1_myfont1, (10, 90))
    screen4.blit(rank1_myfont2 ,(10,140))
    screen4.blit(rank1_myfont3, (10, 200))
    screen4.blit(rank1_myfont4, (10, 260))
    screen4.blit(rank1_myfont5, (10, 320))

    ''''Mouse'''
    (MouseX, MouseY) = pygame.mouse.get_pos()

    ''''Title'''
    highscores_back_title = title_position(260, 365, 400, 450)

    def the_highscores_click(posx, posy):
        if posx > highscores_back_title.beginX and posx < highscores_back_title.endX and posy > highscores_back_title.beginY and posy < highscores_back_title.endY:
            the_players_title = figure(screen_image2, red, black, 265, 400, 95, 50, 1)
            print("players")
            if events.type == pygame.MOUSEBUTTONDOWN and events.button == 1:
                effect1.play()
                the_menufunction()

    highscores = True
    while highscores == True:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit(); sys.exit()


            elif events.type == pygame.MOUSEBUTTONDOWN:
                print(MouseX, MouseY)
                print("Mouse Button up")
            elif events.type == pygame.MOUSEBUTTONUP:
                print(MouseX, MouseY)
                print("Mouse Button down")


            elif events.type == pygame.MOUSEMOTION:
                print("mouse at " + " " + str(MouseX) + " " + str(MouseY))

            the_highscores_click(MouseX, MouseY)
            (MouseX, MouseY) = pygame.mouse.get_pos()
        pygame.display.update()

def the_settingsfunction():
    global scroll
    ''''Everything with 1 added'''

    ''''fps clock'''
    fps1 = clock(60)

    ''''Canvas'''
    pygame.display.set_caption("Settings")
    screen1 = pygame.display.set_mode((display_width1, display_height1))
    pygame.display.update()

    ''''Window'''
    the_image1 = "settings.jpg"
    screen_image1 = pygame.display.set_mode((display_width, display_height))
    menu_image1 =  pygame.image.load(the_image1)
    screen_image1.blit(menu_image1,(0,0))

    ''''Black to remove letter reapearing'''
    menu_image5 = pygame.image.load("black.jpeg")
    menu_image5 = pygame.transform.scale(menu_image5, (display_width // 4, display_height // 8))

    ''''Font'''
    pygame.display.set_caption("Font")
    my_font = pygame.font.Font(None,50)
    my_fontvolume = pygame.font.Font(None,25)
    settings_font = my_font.render("Settings",1,white)
    volume_font = my_font.render("Volume",1,white)
    # resolution_font = my_font.render("resolution", 1, white)
    # resolutionsetting_font = my_font.render("(click me)", 1, white)
    volumehelp_font = my_fontvolume.render("(Press up or down key)", 1, white)
    back1_font = my_font.render("Back", 1, red)

    ''''imports the letters'''
    screen1.blit(settings_font,(240,10))
    screen1.blit(volume_font,(240,80))
    screen1.blit(volumehelp_font, (230,60))
    # screen1.blit(resolution_font, (240,220))
    # screen1.blit(resolutionsetting_font, (240,255))
    screen1.blit(back1_font, (240, 400))

    ''''Positions'''
    volume_title = title_position(230, 380, 75, 160)
    resolution1_title = title_position(235, 415, 220, 300)
    back1_title = title_position(230, 335, 390, 445)

    ''''The mouse'''
    (MouseX, MouseY) = pygame.mouse.get_pos()

    ''''In output the volume level will be stored'''

    zero = ""
    one = "|"
    two = "||"
    three = "|||"
    four = "||||"
    five = "|||||"
    six = "||||||"
    seven = "|||||||"
    eight = "||||||||"
    nine = "|||||||||"
    ten = "||||||||||"

    def volume(scroll):
        output = "test"
        if scroll > 10:
            scroll = 10
        if scroll < 0:
            scroll = 0
        if scroll == 10:
            output = ten
            pygame.mixer.music.set_volume(100)
        elif scroll == 9:
            output = nine
            pygame.mixer.music.set_volume(0.90)
        elif scroll == 8:
            output = eight
            pygame.mixer.music.set_volume(0.80)
        elif scroll == 7:
            output = seven
            pygame.mixer.music.set_volume(0.70)
        elif scroll == 6:
            output = six
            pygame.mixer.music.set_volume(0.60)
        elif scroll == 5:
            output = five
            pygame.mixer.music.set_volume(0.50)
        elif scroll == 4:
            output = four
            pygame.mixer.music.set_volume(0.40)
        elif scroll == 3:
            output = three
            pygame.mixer.music.set_volume(0.30)
        elif scroll == 2:
            output = two
            pygame.mixer.music.set_volume(0.20)
        elif scroll == 1:
            output = one
            pygame.mixer.music.set_volume(0.10)
        elif scroll == 0:
            output = zero
            pygame.mixer.music.set_volume(0)

        return output



    ''''Function returns desired page'''
    def the_menu_click1(posx,posy):


        if posx > volume_title.beginX and posx < volume_title.endX and posy > volume_title.beginY and posy < volume_title.endY:
            the_volume_title = figure(screen_image1, red, black, 230, 80, 145, 90, 1)
            print("Volume")

        elif posx > back1_title.beginX and posx < back1_title.endX and posy > back1_title.beginY and posy < back1_title.endY:
             the_back1_title = figure(screen_image1, red, black, 240, 400, 90, 35, 1)
             print("Back")
             if events.type == pygame.MOUSEBUTTONDOWN and events.button == 1:
                 the_menufunction()



    settings = True
    while settings == True:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif events.type == pygame.MOUSEBUTTONDOWN:
                print ("Mouse Button up")
            elif events.type == pygame.MOUSEBUTTONUP:
                print ("Mouse Button down")
            elif pygame.key.get_pressed()[pygame.K_DOWN] == True:
                scroll -= 1
                screen1.blit(menu_image5, (display_width * 0.35, display_height * 0.23))
            elif pygame.key.get_pressed()[pygame.K_UP] == True:
                scroll += 1
                screen1.blit(menu_image5, (display_width * 0.35, display_height * 0.23))

            elif events.type == pygame.MOUSEMOTION:
                print ("mouse at " + " " + str(MouseX) +  " " + str(MouseY))


            # effect.set_volume(effect.get_volume() + 0.1)
            sound_font = my_font.render(volume(scroll), 1, white)  # the volume level
            screen1.blit(sound_font, (240, 115))  # the volume level
            the_menu_click1(MouseX, MouseY)
            (MouseX, MouseY) = pygame.mouse.get_pos()



        pygame.display.update()


def the_menufunction():
    '''FPS clock'''
    fps = clock(60)


    ''''Canvas'''
    pygame.display.set_caption("Menu")
    screen = pygame.display.set_mode((display_width , display_height))
    pygame.display.update()

    ''''The image canvas/window'''
    the_image = "menu.jpg"
    screen_image = pygame.display.set_mode((display_width, display_height))
    menu_image =  pygame.image.load(the_image)
    screen_image.blit(menu_image,(0,0))

    ''''The font/letters canvas/window'''
    pygame.display.set_caption("Font")
    my_font = pygame.font.Font(None,50)
    menu_font = my_font.render("MENU",1,white)
    start_font = my_font.render("Start",0,white)
    player_font = my_font.render("Rules",0,white)
    highscores_font = my_font.render("High Scores",0,white)
    rules_font = my_font.render("Video", 0, white )
    settings_font = my_font.render("Settings",0,white)
    quit_font = my_font.render("Quit",0,red)

    #imports the letters
    screen.blit(menu_font,(240,10))
    screen.blit(start_font,(240,90))
    screen.blit(player_font,(240,160))
    screen.blit(highscores_font,(240,230))
    screen.blit(settings_font,(240,300))
    screen.blit(rules_font,(240,370))
    screen.blit(quit_font,(240,430))

    ''''The mouse'''
    (MouseX, MouseY) = pygame.mouse.get_pos()

    ''''Menu title coordinations'''
    start_title = title_position(240,320,90,130)
    players_title = title_position(240,370,160,200)
    highscore_title = title_position(240,440,230,270)
    settings_title = title_position(240,390,300,340)
    rules_title = title_position(240, 340, 370, 410)
    quit_title = title_position(240,320,430,470)

    ''''Function returns desired page'''
    def the_menu_click(posx,posy):
        music = True
        if posx > start_title.beginX and posx < start_title.endX and posy > start_title.beginY and posy < start_title.endY:
            the_start_title = figure(screen_image, red, black, 240, 90, 80, 30, 1)
            print("start""")
            if events.type == pygame.MOUSEBUTTONDOWN and events.button == 1:
                effect1.play()
                the_playersfunction()

        elif posx > players_title.beginX and posx < players_title.endX and posy > players_title.beginY and posy < players_title.endY:
             the_players_title = figure(screen_image, red, black, 240, 160, 100, 35, 1)
             if events.type == pygame.MOUSEBUTTONDOWN and events.button == 1:
                 effect1.play()
                 Rule_Page1()
        elif posx > highscore_title.beginX and posx < highscore_title.endX and posy > highscore_title.beginY and posy < highscore_title.endY:
            the_highscores_title = figure(screen_image, red, black, 240, 230, 200, 35, 1)
            if events.type == pygame.MOUSEBUTTONDOWN and events.button == 1:
                effect1.play()
                the_highscoresfunction()
        elif posx > settings_title.beginX and posx < settings_title.endX and posy > settings_title.beginY and posy < settings_title.endY:
            the_settings_title = figure(screen_image, red, black, 240, 300, 150, 35, 1)
            if events.type == pygame.MOUSEBUTTONDOWN and events.button == 1:
                effect1.play()
                the_settingsfunction()
        elif posx > rules_title.beginX and posx < rules_title.endX and posy > rules_title.beginY and posy < rules_title.endY:
            the_rules_title = figure(screen_image, red, black, 240, 370, 130, 30, 1)
            if events.type == pygame.MOUSEBUTTONDOWN and events.button == 1:
                the_video()


        elif posx > quit_title.beginX and posx < quit_title.endX and posy > quit_title.beginY and posy < quit_title.endY:
            the_quit_title = figure(screen_image, red, black, 240, 430, 70, 30, 1)
            if events.type == pygame.MOUSEBUTTONDOWN and events.button == 1:
                 pygame.quit();sys.exit()


    ''''The loop to keep the menu open'''
    main_menu = True
    while main_menu == True:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif events.type == pygame.MOUSEBUTTONDOWN:
                print(MouseX, MouseY)
                print ("Mouse Button up")
            elif events.type == pygame.MOUSEBUTTONUP:
                print(MouseX, MouseY)
                print ("Mouse Button down")
            elif events.type == pygame.MOUSEMOTION:
                print ("mouse at " + " " + str(MouseX) +  " " + str(MouseY))
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_SPACE:
                    the_video()

            the_menu_click(MouseX, MouseY)
            (MouseX, MouseY) = pygame.mouse.get_pos()

        pygame.display.update()



def the_video():
    FPS = 60
    pygame.display.set_caption("Font")
    my_font1 = pygame.font.Font(None, 70)

    menu111_font = my_font1.render("Press space to start the game", 1, red)
    count = 0



    pygame.init()
    clock = pygame.time.Clock()
    movie = pygame.movie.Movie('the_war.mpg')
    screen = pygame.display.set_mode(movie.get_size())
    movie_screen = pygame.Surface(movie.get_size()).convert()


    movie.set_display(movie_screen)
    movie.play()
    pygame.mixer.music.load("goldberg100.wav")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.9)

    war_sound1 = pygame.mixer.Sound("introduction100.wav")
    war_sound1.play()

    the_image2000 = "video_image.png"
    menu_image2000 = pygame.image.load(the_image2000)
    screen.blit(menu_image2000, (359, 300))

    playing = True
    while playing:
        count += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                movie.stop()
                playing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("musictheme.wav")
                    pygame.mixer.music.set_volume(volume)
                    pygame.mixer.music.play(-1)
                    war_sound1.stop()
                    the_menufunction()

        screen.blit(movie_screen, (0, 0))

        screen.blit(menu_image2000, (250, 20))
        if count % 90 == 0:
            screen.blit(menu111_font, (345, 350))

        pygame.display.update()
        clock.tick(FPS)


    pygame.quit()

the_video()