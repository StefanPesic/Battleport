import pygame
import psycopg2

''''Functions remastered'''
pygame.init()

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
        (self.mouseX, self.mouseY) = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()
    def FigureAppear(self, image, colour, colour1, colourChange, x, y, width, height, tickness):
        if x + width > (self.mouseX, self.mouseY)[0] > x and y + height > (self.mouseX, self.mouseY)[1] > y:
            pygame.draw.rect(image, colour (x,y,width,height), tickness)
        else:
            pygame.draw.rect(image.colour1, (x,y,width, height), tickness)

class Title_position:
    def __init__(self, beginX, endX, beginY, endY):
        self.beginX = beginX
        self.endX = endX
        self.beginY = beginY
        self.endY = endY

menu_title = Title_position(4,70,5,63)
endturn_title = Title_position(4,70,360,450)
nordeck_title = Title_position(4,70,540,600)
spcdeck_title = Title_position(4,70,645,700)
playerhead_title = Title_position(855,1020,0,35)
normalcard1_title = Title_position(775,935,65,180)

class Display:
    def __init__(self, captiontitle, width, height):
        self.caption = pygame.display.set_caption(captiontitle)
        self.screen = pygame.display.set_mode((width, height))
        self.fullScreen =  pygame.display.set_mode((width, height), pygame.FULLSCREEN)
    def displayChange(self, click):
        pass
    def Update(self):
        return pygame.display.update()

class ImageLoad:
    def __init__(self, imageFile):
        self.imageFile = imageFile
        self.imageLoading = pygame.image.load(self.imageFile)
        pygame.transform.scale(self.imageLoading, (1600,900))
    def blit(self, screenBox):
        return screenBox.screen.blit(self.imageLoading, (500, 0))

class Font:
    def __init__(self, styleFont, sizeFont, text, colour):
        self.fontSet = pygame.font.Font(styleFont, sizeFont)
        self.fontRender = self.fontSet.render(str(text), 5, colour.showColour()) #TODO edit
    def blit(self, screenBox, posX, posY):
        return screenBox.screen.blit(self.fontRender,(posX, posY))

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

effectSilencer = Music(100, "silencer.wav", -1)
effectCannon = Music(100, "cannon.wav", -1)
musicPlay = Music(100, "musictheme.wav", -1)

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

class Player(ImageLoad):
    def __init__(self, turn, playerGrab):
        self.name = ""
        self.isTurn = turn
        self.isPlayerGrab = playerGrab
        self.score = 0
    def playerWinner(self):
        for events in pygame.event.get():
            pass
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_SPACE:
                    pass #TODO need to go to the menu

class Boat: #TODO make 9 instances of boat
    def __init__(self):
        self.isActiveBoat = False
