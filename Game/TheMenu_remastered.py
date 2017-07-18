from functions_remastered import *
import sys
from abc import ABC

#TODO database login

#Abstract class that has the abstract methods needed for the pages
class AbstractMenuPage(ABC):
    __metaclass__ = ABC.__abstractmethods__
    def PrepareImagesForBlit(self):
        raise NotImplementedError("Abstract method")
    def PrepareFontsForBlit(self):
        raise NotImplementedError("Abstract method")
    def BlitToScreen(self):
        raise NotImplementedError("Abstract method")
    def GameLoop(self):
        raise NotImplementedError("Abstract method")

#The fight page
class Fight(AbstractMenuPage):
    def __init__(self):
        self.pygameBuiltInEvents = pygame.event.get()
        self.playerOne = Player(True)  # Player instance to keep track of the score
        self.playerTwo = Player(False)
        self.timer = Clock(60)
        self.image = ImageLoad("Remastered\Images\Fight\Background\map.jpg")
        self.scoreboard = ImageLoad("Remastered\Images\Fight\Scoreboard\scoreboard.png")
        self.playerOneScore = Font("Remastered\Fonts\Scoreboard\score_board_st\Score Board St.ttf", 110,
                              str(self.playerOne.score), red, "playerOneScore")
        self.playerTwoScore = Font("Remastered\Fonts\Scoreboard\score_board_st\Score Board St.ttf", 110,
                              str(self.playerTwo.score), red, "playerTwoScore")

        self.secondScoreboard = Font("Remastered\Fonts\Scoreboard\score_board_st\Score Board St.ttf", 130,
                                str(self.timer.seconds), red, "secondScoreboard")
        self.minuteScoreboard = Font("Remastered\Fonts\Scoreboard\score_board_st\Score Board St.ttf", 130,
                                str(self.timer.minutes), red,
                                "minuteScoreboard")
        self.playerOneStatsBoard = ImageLoad("Remastered\Images\Fight\Stats\stats.png")  # boat stats, health damage etc
        self.playerTwoStatsBoard = ImageLoad("Remastered\Images\Fight\Stats\stats.png")
        self.playerOneBoatOne = Boat(3, 126, "Remastered\Images\Fight\Boats\player_1\player1Boat.png",
                                True)  # The actual boats
        self.playerOneBoatTwo = Boat(3, 311, "Remastered\Images\Fight\Boats\player_1\player1Boat.png", True)
        self.playerOneBoatThree = Boat(3, 500, "Remastered\Images\Fight\Boats\player_1\player1Boat.png", True)
        self.playerOneBoatFour = Boat(3, 683, "Remastered\Images\Fight\Boats\player_1\player1Boat.png", True)
        self.playerTwoBoatOne = Boat(1490, 123, "Remastered\Images\Fight\Boats\player_2\player2Boat.png", False)
        self.playerTwoBoatTwo = Boat(1490, 309, "Remastered\Images\Fight\Boats\player_2\player2Boat.png", False)
        self.playerTwoBoatThree = Boat(1490, 496, "Remastered\Images\Fight\Boats\player_2\player2Boat.png", False)
        self.playerTwoBoatFour = Boat(1490, 681, "Remastered\Images\Fight\Boats\player_2\player2Boat.png", False)
        self.dummyBoat = Boat(None, None, "Remastered\Images\Fight\Boats\dummy\dummy.png", None)  # Used to access methods
        self.fontHealthPlayerOne = Font(None, 100, "", white, "fontHealthPlayerOne")
        self.fontHealthPlayerTwo = Font(None, 100, "", white, "fontHealthPlayerTwo")
        self.playerOneBoats = []  # array to change the state of the objects(isActive etc)
        self.playerOneBoats.extend((self.playerOneBoatOne, self.playerOneBoatTwo, self.playerOneBoatThree, self.playerOneBoatFour))
        self.playerTwoBoats = []
        self.playerTwoBoats.extend((self.playerTwoBoatOne, self.playerTwoBoatTwo, self.playerTwoBoatThree, self.playerTwoBoatFour))
        self.playerOneAttacks = []  # When user clicks on the attack button it is put in this list
        self.playerOneFights = []  # the sprites (cannons) will be loaded in this list
        self.playerOneResult = None  # To store the sprite
        self.playerTwoAttacks = []
        self.playerTwoFights = []
        self.playerTwoResult = None

    def PrepareImagesForBlit(self):
        self.dummyBoat.NormalBlit(None, None, self.playerOneBoats)  # blits the boats to the screen
        self.dummyBoat.NormalBlit(None, None, self.playerTwoBoats)
        self.dummyBoat.Rect(display, white, self.playerTwoFights, self.playerOneBoats)  # Creates rect around the boats (for collision)
        self.dummyBoat.Rect(display, red, self.playerOneFights, self.playerTwoBoats)

        self.scoreboard.NormalBlit(self.scoreboard.screenDetect.current_w / 2 - self.scoreboard.imageLoading.get_width() / 2, 700,
                              None, None)
        self.playerOneStatsBoard.NormalBlit(0, 720, 360, 180)
        self.playerTwoStatsBoard.NormalBlit(1240, 720, 360, 180)

        self.fontHealthPlayerOne.PositionBlit(display, 2, 870)
        self.fontHealthPlayerTwo.PositionBlit(display, 1320, 870)

    def PrepareFontsForBlit(self):
        self.playerOneScore.reloadText(str(self.playerOne.score))  # Scoreboard scores get updated
        self.playerTwoScore.reloadText(str(self.playerTwo.score))
        self.playerOneScore.PositionBlit(display, 390, 925)
        self.playerTwoScore.PositionBlit(display, 1150, 925)
        self.secondScoreboard.reloadText(str(self.timer.seconds))
        self.minuteScoreboard.reloadText(str(self.timer.minutes))
        self.secondScoreboard.PositionBlit(display, 857, 877)
        self.minuteScoreboard.PositionBlit(display, 660, 877)

    def GameChecks(self):
        self.playerOne.ChangePlayerScore(self.playerTwoBoats)
        self.playerTwo.ChangePlayerScore(self.playerOneBoats)
        self.dummyBoat.SetDefeat(self.playerOneBoats)
        self.dummyBoat.SetDefeat(self.playerTwoBoats)
        self.timer.Tick()  # Updates time of the scoreboard
        self.PlayerAttacks()


    def BlitToScreen(self):
        self.PrepareImagesForBlit()
        self.PrepareFontsForBlit()

    def PlayerAttacks(self):
        #Player 1 attacks
        if len(self.playerOneAttacks) > 0: #For the attacks
            for i in range(len(self.playerOneAttacks)):
                playerOneResult = self.playerOneAttacks[i].Attack(self.playerOneBoats) #Cannon Sprite is saved in playerOneResult
                self.playerOneFights.append(playerOneResult)
            del self.playerOneAttacks[0]

        if len(self.playerOneFights) > 0 :
            for i in range(len(self.playerOneFights)):
                self.dummyBoat.GetAttacked(self.playerOneFights[i], True) #the position of the cannon sprites are updated
                self.playerOneFights[i].NormalBlit(30,30, None) #Loads the cannon sprite

        #Player 2 Attacks
        if len(self.playerTwoAttacks) > 0:  # For the attacks
            for i in range(len(self.playerTwoAttacks)):
                playerTwoResult = self.playerTwoAttacks[i].Attack(self.playerTwoBoats)
                self.playerTwoFights.append(playerTwoResult)
            del self.playerTwoAttacks[0]

        if len(self.playerTwoFights) > 0:
            for i in range(len(self.playerTwoFights)):
                self.dummyBoat.GetAttacked(self.playerTwoFights[i], False)
                self.playerTwoFights[i].NormalBlit(30,30,None)
    def GameControls(self, events):
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
            self.dummyBoat.Move(self.playerOneBoats, events, True)  # Moves boats of player one
            self.dummyBoat.Move(self.playerTwoBoats, events, False)

            if events.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

                # Player 1 keys
            elif events.key == pygame.K_w:
                pass

            elif events.key == pygame.K_s:
                pass
            elif events.key == pygame.K_a:
                pass
            elif events.key == pygame.K_d:
                pass
            elif events.key == pygame.K_1:
                self.dummyBoat.activateBoat(self.playerOneBoats, 0)  # actives one boat and resets the rest
                self.fontHealthPlayerOne.reloadText(
                    "H: " + str(self.playerOneBoatOne.health))  # to update the boat stats on the stats wall
            elif events.key == pygame.K_2:
                self.dummyBoat.activateBoat(self.playerOneBoats, 1)
                self.fontHealthPlayerOne.reloadText("H: " + str(self.playerOneBoatTwo.health))
            elif events.key == pygame.K_3:
                self.dummyBoat.activateBoat(self.playerOneBoats, 2)
                self.fontHealthPlayerOne.reloadText("H: " + str(self.playerOneBoatThree.health))
            elif events.key == pygame.K_4:
                self.dummyBoat.activateBoat(self.playerOneBoats, 3)
                self.fontHealthPlayerOne.reloadText("H: " + str(self.playerOneBoatFour.health))
            elif events.key == pygame.K_q and self.dummyBoat.IsOneBoatActive(self.playerOneBoats):
                # Attack
                self.playerOneAttacks.append(self.dummyBoat)

            # Player 2 Keys
            elif events.key == pygame.K_UP:
                pass
            elif events.key == pygame.K_LEFT:
                pass
            elif events.key == pygame.K_RIGHT:
                pass
            elif events.key == pygame.K_LEFT:
                pass
            elif events.key == pygame.K_7:
                self.dummyBoat.activateBoat(self.playerTwoBoats, 0)
                self.fontHealthPlayerTwo.reloadText("H: " + str(self.playerTwoBoatOne.health))
            elif events.key == pygame.K_8:
                self.dummyBoat.activateBoat(self.playerTwoBoats, 1)
                self.fontHealthPlayerTwo.reloadText("H: " + str(self.playerTwoBoatTwo.health))
            elif events.key == pygame.K_9:
                self.dummyBoat.activateBoat(self.playerTwoBoats, 2)
                self.fontHealthPlayerTwo.reloadText("H: " + str(self.playerTwoBoatThree.health))
            elif events.key == pygame.K_0:
                self.dummyBoat.activateBoat(self.playerTwoBoats, 3)
                self.fontHealthPlayerTwo.reloadText("H: " + str(self.playerTwoBoatFour.health))
            elif events.key == pygame.K_RCTRL and self.dummyBoat.IsOneBoatActive(self.playerTwoBoats):  # Attack
                self.playerTwoAttacks.append(self.dummyBoat)

    def GameLoop(self):
        while gameState.current == gameState.fight:  # when gamestate changes, another page is opened
            self.image.FullScreenBlit(display)
            self.BlitToScreen()
            self.GameChecks()
            for events in pygame.event.get():
                self.GameControls(events)
            display.Update()
        GameStateLoop.MainGameLoop()

#The rules page
class Rules(AbstractMenuPage):
    def __init__(self):
        self.image = ImageLoad("Remastered\Images\Menu\Rules\gameRules.jpg")
        self.fontRules = Font(None, 100, "Rules and instructions", blue, "rules")
        self.fontForward = Font(None, 80, "Foward", white, "forward")
        self.fontBack = Font(None, 80, "Back", red, "back")
    def PrepareImagesForBlit(self):
        self.image.FullScreenBlit(display)
    def PrepareFontsForBlit(self):
        self.fontRules.blit(display, 30, FontAllignmentEnum.GetTop())
        self.fontForward.blit(display, 5, FontAllignmentEnum.GetTop())
        self.fontBack.blit(display, 5, FontAllignmentEnum.GetDown())
    def BlitToScreen(self):
        self.PrepareImagesForBlit()
        self.PrepareFontsForBlit()
    def GameLoop(self):
        self.BlitToScreen()
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

#The highscores page
class HighScores(AbstractMenuPage):
    def __init__(self):
        self.image = ImageLoad("Remastered\Images\Menu\High_Scores\highscores.jpg")
        self.fontHighScore = Font(None, 100, "High Scores", blue, "highScoreTitle")
        self.fontName = Font(None, 80, "Name", white, "name")
        self.fontScore = Font(None, 80, "Score", white, "score")
        self.fontBack = Font(None, 80, "Back", red, "back")
    def PrepareImagesForBlit(self):
        self.image.FullScreenBlit(display)
    def PrepareFontsForBlit(self):
        self.fontHighScore.blit(display, 30, FontAllignmentEnum.GetTop())
        self.fontName.blit(display, 5, FontAllignmentEnum.GetTop())
        self.fontScore.blit(display, 3.5, FontAllignmentEnum.GetTop())
        self.fontBack.blit(display, 5, FontAllignmentEnum.GetDown())
    def BlitToScreen(self):
        self.PrepareImagesForBlit()
        self.PrepareFontsForBlit()
    def GameLoop(self):
        self.BlitToScreen()
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

#The settings page
class Settings(AbstractMenuPage):
    def __init__(self):
        self.image = ImageLoad("Remastered\Images\Menu\Settings\settings.jpg")
        self.fontSettings = Font(None, 100, "Settings", blue, "settingsTitle")
        self.fontVolume = Font(None, 80, "Volume", white, "volume")
        self.fontResolution = Font(None, 80, "Resolution", white, "resolution")
        self.fontBack = Font(None, 80, "Back", red, "back")
    def PrepareImagesForBlit(self):
        self.image.FullScreenBlit(display)
    def PrepareFontsForBlit(self):
        self.fontSettings.blit(display, 30, FontAllignmentEnum.GetTop())
        self.fontVolume.blit(display, 5, FontAllignmentEnum.GetTop())
        self.fontResolution.blit(display, 3.5, FontAllignmentEnum.GetTop())
        self.fontBack.blit(display, 5, FontAllignmentEnum.GetDown())
    def BlitToScreen(self):
        self.PrepareImagesForBlit()
        self.PrepareFontsForBlit()
    @staticmethod
    def ChangeVolume(musicFile):
        volume = 100
        pygame.mixer.music.set_volume(volume - 10)

    def GameLoop(self):
        self.BlitToScreen()
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

#The menu page
class Menu(AbstractMenuPage):
    def __init__(self):
        self.image = ImageLoad("Remastered\Images\Menu\Main_Menu\menu.jpg")
        self.fontWelcome = Font(None, 100, "Battleport", blue, "welcomeTitle")
        self.fontFight = Font(None, 80, "Fight", white, "fight")
        self.fontRules = Font(None, 80, "Rules and instructions", white, "rules")
        self.fontScores = Font(None, 80, "High Scores", white, "scores")
        self.fontSettings = Font(None, 80, "Settings", white, "settings")
        self.fontQuit = Font(None, 80, "Quit", red, "quit")
    def PrepareImagesForBlit(self):
        self.image.FullScreenBlit(display)
    def PrepareFontsForBlit(self):
        self.fontWelcome.blit(display, 30, FontAllignmentEnum.GetTop())
        self.fontFight.blit(display, 5, FontAllignmentEnum.GetTop())
        self.fontRules.blit(display, 3.5, FontAllignmentEnum.GetTop())
        self.fontScores.blit(display, 2.5, FontAllignmentEnum.GetTop())
        self.fontSettings.blit(display, 2, FontAllignmentEnum.GetTop())
        self.fontQuit.blit(display, 5, FontAllignmentEnum.GetDown())
    def BlitToScreen(self):
        self.PrepareImagesForBlit()
        self.PrepareFontsForBlit()
    def GameLoop(self):
        self.BlitToScreen()
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
                self.fontFight.Rect(display, red, MouseX, MouseY, events)
                self.fontRules.Rect(display, red, MouseX, MouseY, events)
                self.fontScores.Rect(display, red, MouseX, MouseY, events)
                self.fontSettings.Rect(display, red, MouseX, MouseY, events)
                self.fontQuit.Rect(display, red, MouseX, MouseY, events)

            display.Update()
        GameStateLoop.MainGameLoop()

#Page objects needed for the gameLoop
Menu = Menu()
Settings = Settings()
HighScores = HighScores()
Rules = Rules()
Fight = Fight()

#Has the main gameloop
class GameStateLoop(ABC):
    @staticmethod
    def MainGameLoop():
        gameStateLoop = True
        while gameStateLoop:
            if gameState.current == gameState.menu:
                Menu.GameLoop()
            elif gameState.current == gameState.fight:
                Fight.GameLoop()
            elif gameState.current == gameState.scores:
                HighScores.GameLoop()
            elif gameState.current == gameState.rules:
                Rules.GameLoop()
            elif gameState.current == gameState.settings:
                Settings.GameLoop()
        gameStateLoop = False

GameStateLoop = GameStateLoop()
GameStateLoop.MainGameLoop()