from functions_remastered import *
import pygame_textInput_remastered
from pygame_textInput_remastered import *
import psycopg2
import sys



#TODO database login
#Database login: (host= "localhost", database="postgres", user= "postgres", password="WallSpeaker5" )

def Fight():
    image = ImageLoad("Remastered\Images\Fight\Background\map.jpg")

    playerOneBoatOne = Boat(3,126, "Remastered\Images\Fight\Boats\player_1\player1Boat.png", True)
    playerOneBoatTwo = Boat(3, 311, "Remastered\Images\Fight\Boats\player_1\player1Boat.png", True)
    playerOneBoatThree = Boat(3, 500, "Remastered\Images\Fight\Boats\player_1\player1Boat.png", True)
    playerOneBoatFour = Boat(3, 683, "Remastered\Images\Fight\Boats\player_1\player1Boat.png", True)

    playerTwoBoatOne = Boat(1490,123, "Remastered\Images\Fight\Boats\player_2\player2Boat.png", False)
    playerTwoBoatTwo = Boat(1490, 309, "Remastered\Images\Fight\Boats\player_2\player2Boat.png", False)
    playerTwoBoatThree = Boat(1490, 496, "Remastered\Images\Fight\Boats\player_2\player2Boat.png", False)
    playerTwoBoatFour = Boat(1490, 681, "Remastered\Images\Fight\Boats\player_2\player2Boat.png", False)

    dummyBoat = Boat(None,None, "Remastered\Images\Fight\Boats\dummy\dummy.png", False)




    playerOneBoats = [] #array to change the state of the objects
    playerOneBoats.extend((playerOneBoatOne, playerOneBoatTwo, playerOneBoatThree, playerOneBoatFour))
    playerTwoBoats = []
    playerTwoBoats.extend((playerTwoBoatOne, playerTwoBoatTwo, playerTwoBoatThree, playerTwoBoatFour))

    playerOne = Player(True)
    playerTwo = Player(False)

    while gameState.current == gameState.fight:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif events.type == pygame.MOUSEBUTTONDOWN:
                pass

            elif events.type == pygame.MOUSEBUTTONUP:
                 pass

            elif events.type == pygame.MOUSEMOTION:
                pass

            elif events.type == pygame.KEYDOWN:
                dummyBoat.Move(playerOneBoats, events, True)  # Moves boats of player one
                dummyBoat.Move(playerTwoBoats, events, False)

                if events.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                    #Player 1 keys
                elif events.key == pygame.K_w:
                    pass

                elif events.key == pygame.K_s:
                    pass
                elif events.key == pygame.K_a:
                    pass
                elif events.key == pygame.K_d:
                    pass
                elif events.key == pygame.K_1:
                    dummyBoat.activateBoat(playerOneBoats,0)
                elif events.key == pygame.K_2:
                    dummyBoat.activateBoat(playerOneBoats, 1)
                elif events.key == pygame.K_3:
                    dummyBoat.activateBoat(playerOneBoats, 2)
                elif events.key == pygame.K_4:
                    dummyBoat.activateBoat(playerOneBoats, 3)
                elif events.key == pygame.K_SPACE:
                    pass

                #Player 2 Keys

                elif  events.key ==  pygame.K_UP:
                    pass
                elif events.key == pygame.K_LEFT:
                    pass
                elif events.key == pygame.K_RIGHT:
                    pass
                elif events.key == pygame.K_LEFT:
                    pass
                elif events.key == pygame.K_7:
                    dummyBoat.activateBoat(playerTwoBoats, 0)
                elif events.key == pygame.K_8:
                    dummyBoat.activateBoat(playerTwoBoats, 1)
                elif events.key == pygame.K_9:
                    dummyBoat.activateBoat(playerTwoBoats, 2)
                elif events.key == pygame.K_0:
                    dummyBoat.activateBoat(playerTwoBoats, 3)


        display.Update()
        image.FullScreenBlit(display)
        playerOneBoatOne.NormalBlit()
        playerOneBoatTwo.NormalBlit()
        playerOneBoatThree.NormalBlit()
        playerOneBoatFour.NormalBlit()

        playerTwoBoatOne.NormalBlit()
        playerTwoBoatTwo.NormalBlit()
        playerTwoBoatThree.NormalBlit()
        playerTwoBoatFour.NormalBlit()







    GameStateLoop()



def MakingOf():
    image = ImageLoad("Remastered\Images\Menu\Making_Of\makingOf.jpg")
    image.FullScreenBlit(display)

    fontMakingOf = Font(None, 100, "Making of", blue, "makingOf")
    fontMakingOf.blit(display,10)

    fontBack = Font(None, 100, "Back", red, "back")
    fontBack.blit(display,910)

    while gameState.current == gameState.makingOf:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif events.type == pygame.MOUSEBUTTONDOWN:
                pass

            elif events.type == pygame.MOUSEBUTTONUP:
                 pass

            elif events.type == pygame.MOUSEMOTION:
                pass
            elif events.type == pygame.KEYDOWN:
                if events.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            (MouseX, MouseY) = pygame.mouse.get_pos()
            fontBack.Rect(display, black, MouseX, MouseY, events)
        display.Update()
    GameStateLoop()



def Rules():
    image = ImageLoad("Remastered\Images\Menu\Rules\gameRules.jpg")
    image.FullScreenBlit(display)

    fontRules = Font(None, 100, "Rules and instructions", blue, "rules")
    fontRules.blit(display,10)

    fontForward = Font(None, 100, "Foward", white, "forward")
    fontForward.blit(display,310)

    fontBack = Font(None, 100, "Back", red, "back")
    fontBack.blit(display,910)

    while gameState.current == gameState.rules:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif events.type == pygame.MOUSEBUTTONDOWN:
                pass

            elif events.type == pygame.MOUSEBUTTONUP:
                 pass

            elif events.type == pygame.MOUSEMOTION:
                pass
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            (MouseX, MouseY) = pygame.mouse.get_pos()
            fontBack.Rect(display, black, MouseX, MouseY, events)
        display.Update()
    GameStateLoop()


def HighScores():
    image = ImageLoad("Remastered\Images\Menu\High_Scores\highscores.jpg")
    image.FullScreenBlit(display)

    fontHighScore = Font(None, 100, "High Scores", blue, "highScoreTitle")
    fontHighScore.blit(display,10)

    fontName = Font(None, 100, "Name", white, "name")
    fontName.blit(display,160)

    fontScore = Font(None, 100, "Score", white, "score")
    fontScore.blit(display,310)

    fontBack = Font(None, 100, "Back", red, "back")
    fontBack.blit(display,910)



    while gameState.current == gameState.scores:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif events.type == pygame.MOUSEBUTTONDOWN:
                pass

            elif events.type == pygame.MOUSEBUTTONUP:
                 pass

            elif events.type == pygame.MOUSEMOTION:
                pass

            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            (MouseX, MouseY) = pygame.mouse.get_pos()
            fontBack.Rect(display, black, MouseX, MouseY, events)
        display.Update()
    GameStateLoop()

def Settings():
    image = ImageLoad("Remastered\Images\Menu\Settings\settings.jpg")
    image.FullScreenBlit(display)

    fontSettings = Font(None, 100, "Settings", blue, "settingsTitle")
    fontSettings.blit(display,10)

    fontVolume = Font(None, 100, "Volume", white, "volume")
    fontVolume.blit(display, 160)

    fontResolution = Font(None, 100, "Resolution", white, "resolution")
    fontResolution.blit(display, 310)

    fontBack = Font(None, 100, "Back", red, "back")
    fontBack.blit(display,910)

    while gameState.current == gameState.settings:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif events.type == pygame.MOUSEBUTTONDOWN:
                pass

            elif events.type == pygame.MOUSEBUTTONUP:
                 pass

            elif events.type == pygame.MOUSEMOTION:
                pass

            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            (MouseX, MouseY) = pygame.mouse.get_pos()
            fontVolume.Rect(display, black, MouseX, MouseY, events)
            fontResolution.Rect(display, black, MouseX, MouseY, events)
            fontBack.Rect(display, black, MouseX, MouseY, events)

        display.Update()
    GameStateLoop()


def MenuFunction():
    # fps = Clock(60)

    image = ImageLoad("Remastered\Images\Menu\Main_Menu\menu.jpg")
    image.FullScreenBlit(display)

    fontWelcome = Font(None, 100, "Welcome to Battleport", blue, "welcomeTitle")
    fontWelcome.blit(display,10)

    fontFight = Font(None, 100, "Fight", white, "fight")
    fontFight.blit(display,160)

    fontRules = Font(None, 100, "Rules and instructions", white, "rules")
    fontRules.blit(display,310)

    fontScores = Font(None, 100, "High Scores", white, "scores")
    fontScores.blit(display,460)

    fontSettings = Font(None, 100, "Settings", white, "settings" )
    fontSettings.blit(display,610)

    fontMakingOf = Font(None, 100, "Making of", white, "making")
    fontMakingOf.blit(display,760)

    fontQuit = Font(None, 100, "Quit", red, "quit")
    fontQuit.blit(display,910)

    while gameState.current == gameState.menu:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif events.type == pygame.MOUSEBUTTONDOWN:
                pass

            elif events.type == pygame.MOUSEBUTTONUP:
                 pass

            elif events.type == pygame.MOUSEMOTION:
                pass

            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            (MouseX, MouseY) = pygame.mouse.get_pos()
            fontFight.Rect(display, black, MouseX, MouseY, events)
            fontRules.Rect(display, black, MouseX, MouseY, events)
            fontScores.Rect(display, black, MouseX, MouseY, events)
            fontSettings.Rect(display, black, MouseX, MouseY, events)
            fontMakingOf.Rect(display, black, MouseX, MouseY, events)
            fontQuit.Rect(display, black, MouseX, MouseY, events)

        display.Update()
    GameStateLoop()

def GameStateLoop(): #changes the page depending on the gamestate
    gameStateLoop = True
    while gameStateLoop:
        if gameState.current == gameState.menu:
            MenuFunction()
        elif gameState.current == gameState.fight:
            Fight()
        elif gameState.current == gameState.scores:
            HighScores()
        elif gameState.current == gameState.rules:
            Rules()
        elif gameState.current == gameState.settings:
            Settings()
        elif gameState.current == gameState.makingOf:
            MakingOf()

    gameStateLoop = False

GameStateLoop()