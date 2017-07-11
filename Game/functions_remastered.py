import pygame
import psycopg2
import sys

''''Functions remastered'''

pygame.init()

#based on the gamestate a certain page will be loaded
class GameState:
    def __init__(self):
        self.menu = "menu"
        self.fight = "fight"
        self.rules = "rules"
        self.scores = "scores"
        self.settings = "settings"
        self.makingOf = "makingOf"
        self.current = self.menu
gameState = GameState()

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

class Mouse:
    def __init__(self):
        self.mouseX = None
        self.mouseY = None
        self.click = pygame.mouse.get_pressed()
    def mouseMotion(self):
        (self.mouseX, self.mouseY) = pygame.mouse.get_pos()

#Main Display
class Display:
    def __init__(self, captiontitle):
        self.screenDetect = pygame.display.Info()
        self.caption = pygame.display.set_caption(captiontitle)
        self.fullScreen =  pygame.display.set_mode((self.screenDetect.current_w, self.screenDetect.current_h), pygame.FULLSCREEN)
    def Update(self):
        return pygame.display.update()
display = Display("Fullscreen")

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
            newSize = pygame.transform.scale(self.imageLoading, (width, height)) #changes size of image
            return self.fullScreen.blit(newSize, (posX, posY))
    def setPositions(self, posX, posY): #Sets new position for the image
        self.posX = posX
        self.posY = posY

class Font:
    def __init__(self, styleFont, sizeFont, text, colour, name):
        self.fontSet = pygame.font.Font(styleFont, sizeFont)
        self.fontRender = self.fontSet.render(str(text), 5, colour.showColour())
        self.positionX = None
        self.positionY = None
        self.name = name
        self.colour = colour
    def blit(self, screenBox, posY): #Mainly used for menu fonts (it centres)
        blit = screenBox.fullScreen.blit(self.fontRender,((screenBox.screenDetect.current_w / 2) - (self.fontRender.get_width() / 2),  posY))
        self.positionX = blit[0]
        self.positionY = posY
        return blit
    def PositionBlit(self, screenBox, posX, posY): #For specific fotns
        self.positionY = posX
        self.positionY = posY
        return screenBox.fullScreen.blit(self.fontRender, (posX, posY))
    def Rect(self, screenBox, colour, mouseX, mouseY, events): #Makes the font clickable
        rect = pygame.draw.rect(screenBox.fullScreen, colour.showColour(), (self.positionX, self.positionY, self.fontRender.get_width(), self.fontRender.get_height()), 1)
        if rect.collidepoint(mouseX, mouseY) and events.type == pygame.MOUSEBUTTONDOWN:
            self.changeGameState()
    def reloadText(self, text): #To have the font update in the pygame loop (example: to update scores)
        self.fontRender = self.fontSet.render(str(text), 5, self.colour.showColour())
    def changeGameState(self): #The gamestate of the game changes, and depending on the state, a page will be loaded
        if self.name == "fight":
            gameState.current = gameState.fight
        elif self.name == "rules":
            gameState.current = gameState.rules
        elif self.name == "scores":
            gameState.current = gameState.scores
        elif self.name == "settings":
            gameState.current = gameState.settings
        elif self.name == "making":
            gameState.current = gameState.makingOf
        elif self.name == "quit":
            pygame.quit()
            sys.exit()
        else:
            self.ButtonFunctionality()

    def ButtonFunctionality(self): #For the buttons of each page
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
                pass
            elif self.name == "resolution":
                pass
            elif self.name == "back":
                gameState.current = gameState.menu
            else:
                pass
        elif gameState.current == gameState.makingOf:
            if self.name == "back":
                gameState.current = gameState.menu

class Music:
    def __init__(self, volume, audioFile, typePlay):
        self.audiofile = pygame.mixer.music.load(audioFile)
        self.volume = pygame.mixer.music.set_volume(volume)
        self.typePlay = typePlay
        self.audioLocation = audioFile
    def playSound(self):
        return pygame.mixer.music.play(self.typePlay)
    def playList(self, musicList, index):
        return musicList[index].PlaySound()
    def scroll(self, scroll):
        scroll = 10
        pass

menuTheme = Music(10, "Remastered\Sound\Menu\menu_theme.wav", 0)
menuTheme.playSound()


#For the highscores
class DataBase:
    def __init__(self, host, database, user, password):
        self.connection = psycopg2.connect(host= host, database= database, user= user, password= password)
        self.connection.autocommit = True
        self.cur = self.connection.cursor()

#Used to keep track of player score, also the name that the user types in
class Player:
    def __init__(self, turn):
        self.name = ""
        self.isTurn = turn
        self.score = 0
        self.defeatedBoats = []
    def ChangePlayerScore(self, boatsList):
        for boat in boatsList:
            if boat.defeated == True:
                    boatsList.remove(boat)
                    self.score += 1
                    self.CheckPlayerScore()
    def CheckPlayerScore(self):
        if(self.score >= 4):
            gameState.current = gameState.menu

#For the boats of the gamed
class Boat(ImageLoad):
    def __init__(self, posX, posY, imageFile, isPlayerOne):
        ImageLoad.__init__(self, imageFile= imageFile )
        self.isActiveBoat = False
        self.defeated = False
        self.positionX = posX
        self.positionY = posY
        self.health = 100
        self.isPlayerOne = isPlayerOne #To seperate player 1 and player 2 boats


    def NormalBlit(self, width, height, boatlist):
        if width == None and height == None: #Width and height are optional
            for i in boatlist:
                i.fullScreen.blit(i.imageLoading, (i.positionX, i.positionY))
        else:
            newSize = pygame.transform.scale(self.imageLoading, (width, height))
            return self.fullScreen.blit(newSize, (self.positionX, self.positionY))

    def activateBoat(self, boatsList, index): #activates one boat, resets others, used to have only one boat move
        for boat in boatsList:
            if boat == boatsList[index]:
                boat.isActiveBoat = True
            else:
                boat.isActiveBoat = False
    def Move(self, boatsList, events, isPlayerOne):
            if isPlayerOne == True:
                for boat in boatsList:
                    if boat.defeated != True:
                        if boat.isActiveBoat == True:
                            if events.key == pygame.K_w:
                                boat.positionY -= self.imageLoading.get_height() / 2
                            elif events.key == pygame.K_s:
                                boat.positionY += self.imageLoading.get_height() /2
                            elif events.key == pygame.K_a:
                                boat.positionX -= self.imageLoading.get_width() / 3
                            elif events.key == pygame.K_d:
                                boat.positionX +=  self.imageLoading.get_width() / 3
            else:
                for boat in boatsList:
                    if boat.defeated != True:
                        if boat.isActiveBoat == True:
                            if events.key == pygame.K_UP:
                                boat.positionY -= self.imageLoading.get_height() / 2
                            elif events.key == pygame.K_DOWN:
                                boat.positionY += self.imageLoading.get_height() /2
                            elif events.key == pygame.K_LEFT:
                                boat.positionX -= self.imageLoading.get_width() / 3
                            elif events.key == pygame.K_RIGHT:
                                boat.positionX += self.imageLoading.get_width() / 3

    def Attack(self, boatsList): #When the user clicks the attack button a cannon sprite is returned
        for boat in boatsList:
            if boat.isActiveBoat == True: #looks for the boat that is activated
                cannon = Boat(boat.positionX, boat.positionY, "Remastered\Images\Fight\Attack\Cannon\cannon.png",
                              None)
                return cannon
    def GetAttacked(self, cannon, isPlayerOne): #Changes position of the cannon sprite
        if isPlayerOne == True:
            cannon.positionX += 5
        else:
            cannon.positionX -= 5
    def Rect(self, screenBox, colour, cannonList, boatList): #for collision detection
        for boat in boatList: #Draws the rects for the boats in the list
            boatRect = pygame.draw.rect(screenBox.fullScreen, colour.showColour(), (boat.positionX, boat.positionY, boat.imageLoading.get_width(),
                                                                                    boat.imageLoading.get_height()), 1)
            if len(cannonList) > 0:
                for cannon in cannonList:
                    cannonDrawRect = pygame.draw.rect(screenBox.fullScreen, colour.showColour(), (cannon.positionX, cannon.positionY, cannon.imageLoading.get_width() / 5 , cannon.imageLoading.get_height() / 7.5), 1)
                    if(boatRect.colliderect(cannonDrawRect)):

                        boat.health -= 1000
                        cannonList.remove(cannon)
    def SetDefeat(self, boatList):
        for boat in boatList:
            if boat.health <= 0:
                boat.defeated = True
        return True
