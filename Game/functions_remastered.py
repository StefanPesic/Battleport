import pygame
import psycopg2
import sys


''''Functions remastered'''
pygame.init()

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

class SettingButtons:
    def __init__(self):
        self.volume = "volume"
        self.resolution = "resolution"

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

class Clock:
    def __init__(self, fps):
        self.fps = fps
    def StartClock(self):
        clock = pygame.time.Clock()
        clock.tick(self.fps)

class Mouse:
    def __init__(self):
        self.mouseX = None
        self.mouseY = None
        self.click = pygame.mouse.get_pressed()
    def mouseMotion(self):
        (self.mouseX, self.mouseY) = pygame.mouse.get_pos()


class Title_position:
    def __init__(self, beginX, endX, beginY, endY):
        self.beginX = beginX
        self.endX = endX
        self.beginY = beginY
        self.endY = endY

class Display:
    def __init__(self, captiontitle):
        self.screenDetect = pygame.display.Info()
        self.caption = pygame.display.set_caption(captiontitle)
        self.fullScreen =  pygame.display.set_mode((self.screenDetect.current_w, self.screenDetect.current_h), pygame.FULLSCREEN)
    def displayChange(self, click):
        pass
    def Update(self):
        return pygame.display.update()

display = Display("Fullscreen")

class ImageLoad(Display):
    def __init__(self, imageFile):
        Display.__init__(self,"Image")
        self.imageFile = imageFile
        self.imageLoading = pygame.image.load(self.imageFile).convert_alpha() #doesn't resize image
        self.fullImage = pygame.transform.scale(self.imageLoading,(self.screenDetect.current_w, self.screenDetect.current_h)) #resizes image to full screen
        self.posX = None
        self.posY = None
    def FullScreenBlit(self, screenBox):
        return screenBox.fullScreen.blit(self.fullImage, (0, 0))
    def NormalBlit(self):
        return self.fullScreen.blit(self.imageLoading, (self.posX,self.posY))
    def setPositions(self, posX, posY):
        self.posX = posX
        self.posY = posY




class Font:
    def __init__(self, styleFont, sizeFont, text, colour, name):
        self.fontSet = pygame.font.Font(styleFont, sizeFont)
        self.fontRender = self.fontSet.render(str(text), 5, colour.showColour()) #TODO edit
        self.positionX = None
        self.positionY = None
        self.name = name
    def blit(self, screenBox, posY):
        blit = screenBox.fullScreen.blit(self.fontRender,((screenBox.screenDetect.current_w / 2) - (self.fontRender.get_width() / 2),  posY))
        self.positionX = blit[0]
        self.positionY = posY
        return blit
    def Rect(self, screenBox, colour, mouseX, mouseY, events):
        rect = pygame.draw.rect(screenBox.fullScreen, colour.showColour(), (self.positionX, self.positionY, self.fontRender.get_width(), self.fontRender.get_height()), 1)
        if rect.collidepoint(mouseX, mouseY) and events.type == pygame.MOUSEBUTTONDOWN:
            self.changeGameState()
    def changeGameState(self): #The gamestate of the game changes
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
    def ButtonFunctionality(self):
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
        self.typePlay = pygame.mixer.music.play(typePlay)
    def playSound(self):
        return pygame.mixer.Sound(self.audiofile)
    def scroll(self, scroll):
        scroll = 10
        pass

# effectSilencer = Music(100, "silencer.wav", -1)
# effectCannon = Music(100, "cannon.wav", -1)
# musicPlay = Music(100, "musictheme.wav", -1)

class DataBase:
    def __init__(self, host, database, user, password):
        self.connection = psycopg2.connect(host= host, database= database, user= user, password= password)
        self.connection.autocommit = True
        self.cur = self.connection.cursor()

class Card: #TODO make 12 instances of card
    def __init__(self):
        self.isGrab = False

class specialBoatGrab: #TODO 9 instances of card, with 9 specialboat9grabs
    def __init__(self):
        self.isSpecialGrab = True

class Player:
    def __init__(self, turn):
        self.name = ""
        self.isTurn = turn
        self.score = 0




class Boat(ImageLoad):
    def __init__(self, posX, posY, imageFile, isPlayerOne):
        ImageLoad.__init__(self, imageFile= imageFile )
        self.isActiveBoat = False
        self.positionX = posX
        self.positionY = posY
        self.health = 100
        self.steps = 2
        self.isPlayerOne = isPlayerOne
    def NormalBlit(self):
        return self.fullScreen.blit(self.imageLoading, (self.positionX, self.positionY))
    def activateBoat(self, boatsList, index): #activates one boat, resets others
        for boat in boatsList:
            if boat == boatsList[index]:
                boat.isActiveBoat = True
            else:
                boat.isActiveBoat = False
    def Move(self, boatsList, events, isPlayerOne):
            if isPlayerOne == True:
                for boat in boatsList:
                    if boat.isActiveBoat == True:
                        if events.key == pygame.K_w:
                            boat.positionY -= 10
                        elif events.key == pygame.K_s:
                            boat.positionY += 10
                        elif events.key == pygame.K_a:
                            boat.positionX -= 10
                        elif events.key == pygame.K_d:
                            boat.positionX += 10
            else:
                for boat in boatsList:
                    if boat.isActiveBoat == True:
                        if events.key == pygame.K_UP:
                            boat.positionY -= 10
                        elif events.key == pygame.K_DOWN:
                            boat.positionY += 10
                        elif events.key == pygame.K_LEFT:
                            boat.positionX -= 10
                        elif events.key == pygame.K_RIGHT:
                            boat.positionX += 10
    def Attack(self, boatsList, isPlayerOne):
        cannon = Boat(None, None, "Remastered\Images\Fight\Attack\Cannon\cannon.png", None)
        pass










