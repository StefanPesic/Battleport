import pygame
import psycopg2
import sys
import numpy


pygame.init()

#based on the gamestate a certain page will be loaded
class GameState:
    def __init__(self):
        self.menu = "menu"
        self.fight = "fight"
        self.rules = "rules"
        self.scores = "scores"
        self.settings = "settings"
        self.current = self.menu #TODO change this to make the game work
gameState = GameState()



#For displaying colours
class Colour:
    def __init__(self, colourOne, colourTwo, colourThree):
        self.colourOne = colourOne
        self.colourTwo = colourTwo
        self.colourThree = colourThree
    def showColour(self):
        tuple = (self.colourOne, self.colourTwo, self.colourThree)
        return tuple

white = Colour(255,255,255)
black = Colour(0,0,0)
red = Colour(255,0,0)
yellow = Colour(255,255,0)
blue = Colour(0,0,255)

#For playing music
class Music:
    def __init__(self, volume, audioFile, typePlay):
        self.audiofile = pygame.mixer.music.load(audioFile)
        self.typePlay = typePlay
        self.audioLocation = audioFile
        self.volume = volume
        pygame.mixer.music.set_volume(volume)

    def playSound(self):
        return pygame.mixer.music.play(self.typePlay)
    def ChangeVolume(self, mouseEvent):
        leftMouse = 1
        volumeChangeLevel = 0.1     
        if mouseEvent.button == leftMouse:
            self.volume += volumeChangeLevel
        else:
            self.volume -= volumeChangeLevel
        pygame.mixer.music.set_volume(self.volume)

menuTheme = Music(1.0, "Remastered\Sound\Menu\menu_theme.wav", 0)
menuTheme.playSound()


#Used for the count clock of the scoreboard
class Clock:
    def __init__(self, fps):
        self.fps = fps
        self.seconds = 0
        self.minutes = 0
        self.changingNumber = 0
    def StartClock(self):
        clock = pygame.time.Clock()
        clock.tick(self.fps)
    def Tick(self):
        self.seconds = round(int(self.changingNumber), 0)
        if self.changingNumber > 60:
            self.minutes += 1
            self.changingNumber = 0
        else:
            self.changingNumber += 0.01
#The mouse (Hardware device)
class Mouse:
    def __init__(self):
        self.mouseX = None
        self.mouseY = None
        self.click = pygame.mouse.get_pressed()
    def mouseMotion(self):
        (self.mouseX, self.mouseY) = pygame.mouse.get_pos()

#For the screen resolutions
class ScreenResolutionEnum:
    def __init__(self):
        resolutionOne = [1920, 1680]
        resolutionTwo = [1366, 768]
        resolutionThree = [1280, 1024]
        resolutionFour = [1280, 800]
        resolutionFive = [1024, 768]
        self.resolutions = []
        self.resolutions.append(resolutionOne)
        self.resolutions.append(resolutionTwo)
        self.resolutions.append(resolutionThree)
        self.resolutions.append(resolutionFour)
        self.resolutions.append(resolutionFive)
    def GiveResolution(self):
        index = -1
        if index >= len(self.resolutions) - 1:
            index = -1
        else:
            index += 1
            return self.resolutions[index]

ScreenResolutionEnum = ScreenResolutionEnum()

#Main Display screen
class Display:
    def __init__(self, captiontitle):
        self.screenDetect = pygame.display.Info()
        self.caption = pygame.display.set_caption(captiontitle)
        self.fullScreen =  pygame.display.set_mode((self.screenDetect.current_w, self.screenDetect.current_h), pygame.FULLSCREEN)
    def Update(self):
        pygame.display.update()
    def ChangeResolution(self):
        #TODO 
        currentResultion = ScreenResolutionEnum.GiveResolution()
        self.fullScreen = pygame.display.set_mode((1300, 600), pygame.FULLSCREEN)

display = Display("Fullscreen")

#To set position options
class FontAllignmentEnum:
    Top, Down = range(0,2)
    @staticmethod
    def GetTop():
        return FontAllignmentEnum.Top
    @staticmethod
    def GetDown():
        return FontAllignmentEnum.Down


#For the images
class ImageLoad(Display):
    def __init__(self, imageFile):
        Display.__init__(self,"Image")
        self.imageFile = imageFile
        self.imageLoading = pygame.image.load(self.imageFile).convert_alpha()
        self.fullImage = pygame.transform.scale(self.imageLoading,(self.screenDetect.current_w, self.screenDetect.current_h))
        self.posX = None
        self.posY = None
    def FullScreenBlit(self, screenBox):
        return screenBox.fullScreen.blit(self.fullImage, (0, 0)) #Fills entire screen
    def NormalBlit(self, posX, posY, width, height): #for specific images (sprites)
        self.posX = posX
        self.posY = posY
        if width == None and height == None: #It is optional to give width and height
            return self.fullScreen.blit(self.imageLoading, (self.posX,self.posY))
        else:
            scaledImageSize = pygame.transform.scale(self.imageLoading, (width, height)) #changes size of image
            return self.fullScreen.blit(scaledImageSize, (posX,posY, 1600, 900))
    def setPositions(self, posX, posY): #Sets new position for the image
        self.posX = posX
        self.posY = posY



#TODO scale font
#For the fonts
class Font:
    def __init__(self, styleFont, sizeFont, text, colour, name):
        self.fontSet = pygame.font.Font(styleFont, sizeFont)
        self.fontRender = self.fontSet.render(str(text), 5, colour.showColour())
        self.positionX = None
        self.positionY = None
        self.name = name
        self.colour = colour
    def blit(self, screenBox, posY, screenPosition): #Mainly used for menu fonts (it centres)
        if screenPosition is FontAllignmentEnum.Top:
            blit = screenBox.fullScreen.blit(self.fontRender, (
            (screenBox.screenDetect.current_w / 2) - (self.fontRender.get_width() / 2),
            screenBox.screenDetect.current_h / posY))
        elif screenPosition is FontAllignmentEnum.Down:
            blit = screenBox.fullScreen.blit(self.fontRender, (
            (screenBox.screenDetect.current_w / 2) - (self.fontRender.get_width() / 2),screenBox.screenDetect.current_h / 2 + screenBox.screenDetect.current_h / posY))
        self.positionX = blit[0]
        self.positionY = blit[1]

    def PositionBlit(self, screenBox, posX, posY): #For specific fotns
        self.positionY = posX
        self.positionY = posY
        return screenBox.fullScreen.blit(self.fontRender, (posX, posY))
    def Rect(self, screenBox, colour, mouseX, mouseY, events): #Makes the font clickable
        rect = pygame.draw.rect(screenBox.fullScreen, colour.showColour(), (self.positionX, self.positionY, self.fontRender.get_width(), self.fontRender.get_height()), 1)
        if rect.collidepoint(mouseX, mouseY) and events.type == pygame.MOUSEBUTTONDOWN:
            self.changeGameState(events)
    def reloadText(self, text): #To have the font update in the pygame loop (example: to update scores)
        self.fontRender = self.fontSet.render(str(text), 5, self.colour.showColour())
    def changeGameState(self, mouseEvent): #The gamestate of the game changes, and depending on the state, a page will be loaded
        if self.name == "fight":
            gameState.current = gameState.fight
        elif self.name == "rules":
            gameState.current = gameState.rules
        elif self.name == "scores":
            gameState.current = gameState.scores
        elif self.name == "settings":
            gameState.current = gameState.settings
        elif self.name == "quit":
            pygame.quit()
            sys.exit()
        else:
            self.ButtonFunctionality(mouseEvent)

    def ButtonFunctionality(self, mouseEvent): #For the buttons of each page
        if gameState.current == gameState.fight:
            pass
        elif gameState.current == gameState.rules:
            if self.name == "back":
                gameState.current = gameState.menu
        elif gameState.current == gameState.scores:
            if self.name == "back":
                gameState.current = gameState.menu
        elif gameState.current == gameState.settings:
            if self.name == "volume":
                menuTheme.ChangeVolume(mouseEvent)
            elif self.name == "resolution":
                display.ChangeResolution()
                pass
            elif self.name == "back":
                gameState.current = gameState.menu
            else:
                pass

#For the highscores
class DataBase:
    def __init__(self, host, database, user, password):
        self.connection = psycopg2.connect(host= host, database= database, user= user, password= password)
        self.connection.autocommit = True
        self.cur = self.connection.cursor()

#Used to keep track of player score, also the name that the user types in
class Player:
    def __init__(self, turn):
        self.isTurn = turn
        self.score = 0
        self.defeatedBoats = []
    def ChangePlayerScore(self, boatsList): #Changes player's score based on if a boat is defeated
        for boat in boatsList:
            if boat.defeated == True:
                    boatsList.remove(boat)
                    self.score += 1
                    self.CheckPlayerScore()
    def CheckPlayerScore(self): #If the players score is 4, it will go to the main menu
        if(self.score >= 4):
            gameState.current = gameState.menu

#For the boat
class Boat(ImageLoad):
    def __init__(self, posX, posY, imageFile, isPlayerOne):
        ImageLoad.__init__(self, imageFile= imageFile )
        self.isActiveBoat = False
        self.defeated = False
        self.positionX = posX
        self.positionY = posY
        self.health = 100
        self.isPlayerOne = isPlayerOne #To seperate player 1 and player 2 boats
        self.YMoveDistance = 2.070 #The distance the player walks in Y
        self.XMoveDistance = 3 #The distance the player walks in X
    def NormalBlit(self, width, height, boatlist):
        if width == None and height == None: #Width and height are optional
            for boat in boatlist:
                boat.fullScreen.blit(boat.imageLoading, (boat.positionX, boat.positionY))
        else:
            newSize = pygame.transform.scale(self.imageLoading, (width, height))
            return self.fullScreen.blit(newSize, (self.positionX, self.positionY))
    def activateBoat(self, boatsList, index): #activates one boat, resets others, used to have only one boat move
        for boat in boatsList:
            if boat == boatsList[index]:
                boat.isActiveBoat = True
            else:
                boat.isActiveBoat = False
    def IsOneBoatActive(self, boatList):
        for boat in boatList:
            if boat.isActiveBoat == True:
                return True
    def Move(self, boatsList, events, isPlayerOne): #To move the boats
            if isPlayerOne == True:
                for boat in boatsList:
                    if boat.defeated != True:
                        if boat.isActiveBoat == True:
                            if self.IsOutOfBoundary(boatsList) != True:
                                if events.key == pygame.K_w:
                                    boat.positionY -= self.imageLoading.get_height() / self.YMoveDistance
                                elif events.key == pygame.K_s:
                                    boat.positionY += self.imageLoading.get_height() / self.YMoveDistance
                                elif events.key == pygame.K_a:
                                    boat.positionX -= self.imageLoading.get_width() / self.XMoveDistance
                                elif events.key == pygame.K_d:
                                    boat.positionX +=  self.imageLoading.get_width() / self.XMoveDistance
            else:
                for boat in boatsList:
                    if boat.defeated != True:
                        if boat.isActiveBoat == True:
                            if self.IsOutOfBoundary(boatsList) != True:
                                if events.key == pygame.K_UP:
                                    boat.positionY -= self.imageLoading.get_height() / self.YMoveDistance
                                elif events.key == pygame.K_DOWN:
                                    boat.positionY += self.imageLoading.get_height() / self.YMoveDistance
                                elif events.key == pygame.K_LEFT:
                                    boat.positionX -= self.imageLoading.get_width() / self.XMoveDistance
                                elif events.key == pygame.K_RIGHT:
                                    boat.positionX += self.imageLoading.get_width() / self.XMoveDistance

    def Attack(self, boatsList): #When the user clicks the attack button a cannon sprite is returned
        for boat in boatsList:
            if boat.isActiveBoat == True: #looks for the boat that is activated
                cannon = Boat(boat.positionX, boat.positionY + 18, "Remastered\Images\Fight\Attack\Cannon\cannon.png",
                              None)
                return cannon

    def GetAttacked(self, cannon, isPlayerOne): #Changes position of the cannon sprite
        if isPlayerOne is True and cannon is not None:
            cannon.positionX += 5
        elif isPlayerOne is False and cannon is not None:
            cannon.positionX -= 5
    def Rect(self, screenBox, colour, cannonList, boatList): #for collision detection
        for boat in boatList: #Draws the rects for the boats in the list
            boatRect = pygame.draw.rect(screenBox.fullScreen, colour.showColour(), (boat.positionX, boat.positionY, boat.imageLoading.get_width(),
                                                                                    boat.imageLoading.get_height()), 1)
            if len(cannonList) > 0:
                for cannon in cannonList:
                    cannonDrawRect = pygame.draw.rect(screenBox.fullScreen, colour.showColour(), (cannon.positionX, cannon.positionY, cannon.imageLoading.get_width() / 9 , cannon.imageLoading.get_height() / 14), 1)
                    if(boatRect.colliderect(cannonDrawRect)):
                        boat.health -= 1
                        cannonList.remove(cannon)
    def SetDefeat(self, boatList): #Checks if a boat is defeated
        for boat in boatList:
            if boat.health <= 0:
                boat.defeated = True
        return True
    def IsOutOfBoundary(self, boatList): # Checks if a boat is outside of an boundary #TODO change it
        for boat in boatList:
            if boat.positionX + boat.imageLoading.get_width() > display.screenDetect.current_w:
                boat.positionX -= (self.XMoveDistance + 100)
            elif boat.positionX < display.screenDetect.current_w - display.screenDetect.current_w:
                boat.positionX += (self.XMoveDistance + 100)
            elif boat.positionY + boat.imageLoading.get_height() > display.screenDetect.current_h:
                boat.positionY -= (self.YMoveDistance + 100)
            elif boat.positionY + boat.imageLoading.get_height() < display.screenDetect.current_h - display.screenDetect.current_h:
                boat.positionY += (self.YMoveDistance + 150)