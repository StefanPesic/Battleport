from functions_remastered import *
import psycopg2
import sys
from abc import ABC


#TODO database login
#Database login: (host= "localhost", database="postgres", user= "postgres", password="WallSpeaker5" )


class AbstractMenuPage(ABC):
    __metaclass__ = ABC.__abstractmethods__
    def BlitImages(self):
        raise NotImplementedError("Abstract method")
    def BlitFonts(self):
        raise NotImplementedError("Abstract method")
    def CallObjects(self):
        raise NotImplementedError("Abstract method")
    def GameLoop(self):
        raise NotImplementedError("Abstract method")


#In Fight the actual game is
def Fight():
    playerOne = Player(True) # Player instance to keep track of the score
    playerTwo = Player(False)

    timer = Clock(60) #used for the scoreboard to keep track of the time

    image = ImageLoad("Remastered\Images\Fight\Background\map.jpg")
    scoreboard = ImageLoad("Remastered\Images\Fight\Scoreboard\scoreboard.png")
    playerOneScore = Font("Remastered\Fonts\Scoreboard\score_board_st\Score Board St.ttf", 110, str(playerOne.score), red, "playerOneScore")
    playerTwoScore = Font("Remastered\Fonts\Scoreboard\score_board_st\Score Board St.ttf", 110, str(playerTwo.score), red, "playerTwoScore")

    secondScoreboard = Font("Remastered\Fonts\Scoreboard\score_board_st\Score Board St.ttf", 130, str(timer.seconds), red, "secondScoreboard")
    minuteScoreboard = Font("Remastered\Fonts\Scoreboard\score_board_st\Score Board St.ttf", 130, str(timer.minutes), red,
                            "minuteScoreboard")

    playerOneStatsBoard = ImageLoad("Remastered\Images\Fight\Stats\stats.png") #boat stats, health damage etc
    playerTwoStatsBoard = ImageLoad("Remastered\Images\Fight\Stats\stats.png")

    playerOneBoatOne = Boat(3,126, "Remastered\Images\Fight\Boats\player_1\player1Boat.png", True) #The actual boats
    playerOneBoatTwo = Boat(3, 311, "Remastered\Images\Fight\Boats\player_1\player1Boat.png", True)
    playerOneBoatThree = Boat(3, 500, "Remastered\Images\Fight\Boats\player_1\player1Boat.png", True)
    playerOneBoatFour = Boat(3, 683, "Remastered\Images\Fight\Boats\player_1\player1Boat.png", True)

    playerTwoBoatOne = Boat(1490,123, "Remastered\Images\Fight\Boats\player_2\player2Boat.png", False)
    playerTwoBoatTwo = Boat(1490, 309, "Remastered\Images\Fight\Boats\player_2\player2Boat.png", False)
    playerTwoBoatThree = Boat(1490, 496, "Remastered\Images\Fight\Boats\player_2\player2Boat.png", False)
    playerTwoBoatFour = Boat(1490, 681, "Remastered\Images\Fight\Boats\player_2\player2Boat.png", False)

    dummyBoat = Boat(None,None, "Remastered\Images\Fight\Boats\dummy\dummy.png", None) #Used to access methods

    fontHealthPlayerOne = Font(None, 100, "", white, "fontHealthPlayerOne")
    fontHealthPlayerTwo = Font(None, 100, "", white, "fontHealthPlayerTwo")

    playerOneBoats = [] #array to change the state of the objects(isActive etc)
    playerOneBoats.extend((playerOneBoatOne, playerOneBoatTwo, playerOneBoatThree, playerOneBoatFour))
    playerTwoBoats = []
    playerTwoBoats.extend((playerTwoBoatOne, playerTwoBoatTwo, playerTwoBoatThree, playerTwoBoatFour))

    playerOneAttacks = []  # When user clicks on the attack button it is put in this list
    playerOneFights = [] #the sprites (cannons) will be loaded in this list
    playerOneResult = None #To store the sprite

    playerTwoAttacks = []
    playerTwoFights = []
    playerTwoResult = None


    while gameState.current == gameState.fight: #when gamestate changes, another page is opened
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
                    dummyBoat.activateBoat(playerOneBoats,0) #actives one boat and resets the rest
                    fontHealthPlayerOne.reloadText("H: " + str(playerOneBoatOne.health)) #to update the boat stats on the stats wall
                elif events.key == pygame.K_2:
                    dummyBoat.activateBoat(playerOneBoats, 1)
                    fontHealthPlayerOne.reloadText("H: " + str(playerOneBoatTwo.health))
                elif events.key == pygame.K_3:
                    dummyBoat.activateBoat(playerOneBoats, 2)
                    fontHealthPlayerOne.reloadText("H: " + str(playerOneBoatThree.health))
                elif events.key == pygame.K_4:
                    dummyBoat.activateBoat(playerOneBoats, 3)
                    fontHealthPlayerOne.reloadText("H: " + str(playerOneBoatFour.health))
                elif events.key == pygame.K_q: #Attack
                    playerOneAttacks.append(dummyBoat)


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
                    fontHealthPlayerTwo.reloadText("H: " + str(playerTwoBoatOne.health))
                elif events.key == pygame.K_8:
                    dummyBoat.activateBoat(playerTwoBoats, 1)
                    fontHealthPlayerTwo.reloadText("H: " + str(playerTwoBoatTwo.health))
                elif events.key == pygame.K_9:
                    dummyBoat.activateBoat(playerTwoBoats, 2)
                    fontHealthPlayerTwo.reloadText("H: " + str(playerTwoBoatThree.health))
                elif events.key == pygame.K_0:
                    dummyBoat.activateBoat(playerTwoBoats, 3)
                    fontHealthPlayerTwo.reloadText("H: " + str(playerTwoBoatFour.health))
                elif events.key == pygame.K_RCTRL: #Attack
                    playerTwoAttacks.append(dummyBoat)

        display.Update()
        image.FullScreenBlit(display)

        #Player 1 attacks
        if len(playerOneAttacks) > 0: #For the attacks
            for i in range(len(playerOneAttacks)):
                playerOneResult = playerOneAttacks[i].Attack(playerOneBoats) #Cannon Sprite is saved in playerOneResult
                playerOneFights.append(playerOneResult)
            del playerOneAttacks[0]

        if len(playerOneFights) > 0 :
            for i in range(len(playerOneFights)):
                dummyBoat.GetAttacked(playerOneFights[i], True) #the position of the cannon sprites are updated
                playerOneFights[i].NormalBlit(70,60, None) #Loads the cannon sprite

        #Player 2 Attacks
        if len(playerTwoAttacks) > 0:  # For the attacks
            for i in range(len(playerTwoAttacks)):
                playerTwoResult = playerTwoAttacks[i].Attack(playerTwoBoats)
                playerTwoFights.append(playerTwoResult)
            del playerTwoAttacks[0]

        if len(playerTwoFights) > 0:
            for i in range(len(playerTwoFights)):
                dummyBoat.GetAttacked(playerTwoFights[i], False)
                playerTwoFights[i].NormalBlit(70,60,None)

        dummyBoat.NormalBlit(None, None, playerOneBoats) # blits the boats to the screen
        dummyBoat.NormalBlit(None, None, playerTwoBoats)

        dummyBoat.Rect(display,white, playerTwoFights, playerOneBoats) #Creates rect around the boats (for collision)
        dummyBoat.Rect(display, red, playerOneFights, playerTwoBoats)

        playerOne.ChangePlayerScore(playerTwoBoats)
        playerTwo.ChangePlayerScore(playerOneBoats)

        dummyBoat.SetDefeat(playerOneBoats)
        dummyBoat.SetDefeat(playerTwoBoats)

        playerOneScore.reloadText(str(playerOne.score)) #Scoreboard scores get updated
        playerTwoScore.reloadText(str(playerTwo.score))

        scoreboard.NormalBlit(scoreboard.screenDetect.current_w / 2 - scoreboard.imageLoading.get_width() / 2 , 860, None, None)
        playerOneScore.PositionBlit(display, 390, 925)
        playerTwoScore.PositionBlit(display, 1150, 925)

        timer.Tick() #Updates time of the scoreboard
        secondScoreboard.reloadText(str(timer.seconds))
        minuteScoreboard.reloadText(str(timer.minutes))
        secondScoreboard.PositionBlit(display, 857, 877)
        minuteScoreboard.PositionBlit(display, 660, 877)

        playerOneStatsBoard.NormalBlit(0,870, 360, 180)
        playerTwoStatsBoard.NormalBlit(1320, 870, 360, 180)

        fontHealthPlayerOne.PositionBlit(display, 2, 870)
        fontHealthPlayerTwo.PositionBlit(display, 1320, 870)
    GameStateLoop.MainGameLoop()


class MakingOf(AbstractMenuPage):
    def __init__(self):
        self.image = ImageLoad("Remastered\Images\Menu\Making_Of\makingOf.jpg")  # Background
        self.fontMakingOf = Font(None, 100, "Making of", blue, "makingOf")
        self.fontBack = Font(None, 100, "Back", red, "back")
    def BlitImages(self):
        self.image.FullScreenBlit(display)
    def BlitFonts(self):
        self.fontMakingOf.blit(display, 10)
        self.fontBack.blit(display, 910)
    def CallObjects(self):
        self.BlitImages()
        self.BlitFonts()
    def GameLoop(self):
        self.CallObjects()
        while gameState.current == gameState.makingOf:
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
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
                self.fontBack.Rect(display, black, MouseX, MouseY, events)  # Makes the font clickable
            display.Update()
        GameStateLoop.MainGameLoop()


class Rules(AbstractMenuPage):
    def __init__(self):
        self.image = ImageLoad("Remastered\Images\Menu\Rules\gameRules.jpg")
        self.fontRules = Font(None, 100, "Rules and instructions", blue, "rules")
        self.fontForward = Font(None, 100, "Foward", white, "forward")
        self.fontBack = Font(None, 100, "Back", red, "back")
    def BlitImages(self):
        self.image.FullScreenBlit(display)
    def BlitFonts(self):
        self.fontRules.blit(display, 10)
        self.fontForward.blit(display, 310)
        self.fontBack.blit(display, 910)
    def CallObjects(self):
        self.BlitImages()
        self.BlitFonts()
    def GameLoop(self):
        self.CallObjects()
        while gameState.current == gameState.rules:
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
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
                self.fontBack.Rect(display, black, MouseX, MouseY, events)
            display.Update()
        GameStateLoop.MainGameLoop()


class HighScores(AbstractMenuPage):
    def __init__(self):
        self.image = ImageLoad("Remastered\Images\Menu\High_Scores\highscores.jpg")
        self.fontHighScore = Font(None, 100, "High Scores", blue, "highScoreTitle")
        self.fontName = Font(None, 100, "Name", white, "name")
        self.fontScore = Font(None, 100, "Score", white, "score")
        self.fontBack = Font(None, 100, "Back", red, "back")
    def BlitImages(self):
        self.image.FullScreenBlit(display)
    def BlitFonts(self):
        self.fontHighScore.blit(display, 10)
        self.fontName.blit(display, 160)
        self.fontScore.blit(display, 310)
        self.fontBack.blit(display, 910)
    def CallObjects(self):
        self.BlitImages()
        self.BlitFonts()
    def GameLoop(self):
        self.CallObjects()
        while gameState.current == gameState.scores:
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
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
                self.fontBack.Rect(display, black, MouseX, MouseY, events)
            display.Update()
        GameStateLoop.MainGameLoop()


class Settings(AbstractMenuPage):
    def __init__(self):
        self.image = ImageLoad("Remastered\Images\Menu\Settings\settings.jpg")
        self.fontSettings = Font(None, 100, "Settings", blue, "settingsTitle")
        self.fontVolume = Font(None, 100, "Volume", white, "volume")
        self.fontResolution = Font(None, 100, "Resolution", white, "resolution")
        self.fontBack = Font(None, 100, "Back", red, "back")
    def BlitImages(self):
        self.image.FullScreenBlit(display)
    def BlitFonts(self):
        self.fontSettings.blit(display, 10)
        self.fontVolume.blit(display, 160)
        self.fontResolution.blit(display, 310)
        self.fontBack.blit(display, 910)
    def CallObjects(self):
        self.BlitImages()
        self.BlitFonts()
    def GameLoop(self):
        self.CallObjects()
        while gameState.current == gameState.settings:
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
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
                self.fontVolume.Rect(display, black, MouseX, MouseY, events)
                self.fontResolution.Rect(display, black, MouseX, MouseY, events)
                self.fontBack.Rect(display, black, MouseX, MouseY, events)

            display.Update()
        GameStateLoop.MainGameLoop()


class Menu(AbstractMenuPage):
    def __init__(self):
        self.image = ImageLoad("Remastered\Images\Menu\Main_Menu\menu.jpg")
        self.fontWelcome = Font(None, 100, "Welcome to Battleport", blue, "welcomeTitle")
        self.fontFight = Font(None, 100, "Fight", white, "fight")
        self.fontRules = Font(None, 100, "Rules and instructions", white, "rules")
        self.fontScores = Font(None, 100, "High Scores", white, "scores")
        self.fontSettings = Font(None, 100, "Settings", white, "settings")
        self.fontMakingOf = Font(None, 100, "Making of", white, "making")
        self.fontQuit = Font(None, 100, "Quit", red, "quit")
    def BlitImages(self):
        self.image.FullScreenBlit(display)
    def BlitFonts(self):
        self.fontWelcome.blit(display, 10)
        self.fontFight.blit(display, 160)
        self.fontRules.blit(display, 310)
        self.fontScores.blit(display, 460)
        self.fontSettings.blit(display, 610)
        self.fontSettings.blit(display, 610)
        self.fontMakingOf.blit(display, 760)
        self.fontQuit.blit(display, 910)
    def CallObjects(self):
        self.BlitImages()
        self.BlitFonts()
    def GameLoop(self):
        self.CallObjects()
        while gameState.current == gameState.menu:
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
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
                self.fontFight.Rect(display, black, MouseX, MouseY, events)
                self.fontRules.Rect(display, black, MouseX, MouseY, events)
                self.fontScores.Rect(display, black, MouseX, MouseY, events)
                self.fontSettings.Rect(display, black, MouseX, MouseY, events)
                self.fontMakingOf.Rect(display, black, MouseX, MouseY, events)
                self.fontQuit.Rect(display, black, MouseX, MouseY, events)

            display.Update()
        GameStateLoop.MainGameLoop()


Menu = Menu()
Settings = Settings()
HighScores = HighScores()
Rules = Rules()
MakingOf = MakingOf()

class GameStateLoop(ABC):
    @staticmethod
    def MainGameLoop():
        gameStateLoop = True
        while gameStateLoop:
            if gameState.current == gameState.menu:
                Menu.GameLoop()
            elif gameState.current == gameState.fight:
                Fight()
            elif gameState.current == gameState.scores:
                HighScores.GameLoop()
            elif gameState.current == gameState.rules:
                Rules.GameLoop()
            elif gameState.current == gameState.settings:
                Settings.GameLoop()
            elif gameState.current == gameState.makingOf:
                MakingOf.GameLoop()
        gameStateLoop = False

GameStateLoop = GameStateLoop()
GameStateLoop.MainGameLoop()