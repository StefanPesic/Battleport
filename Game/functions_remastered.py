import pygame
import psycopg2

''''Functions remastered'''

pygame.init()

class Colour:
    def __init__(self, colourOne, colourTwo, colourThree):
        self.colourOne = colourOne
        self.colourTwo = colourTwo
        self.colourThree = colourThree

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
    def __init__(self, width, height):
        self.screen = pygame.display.set_mode((width, height))
        self.fullScreen =  pygame.display.set_mode((width, height), pygame.FULLSCREEN)
    def displayChange(self, click):
        if click == 0:
            return self.screen
        elif click == 1:
            return pygame.display.set_mode((800,600), pygame.FULLSCREEN)
        elif click == 2:
            return self.fullScreen

display640x480 = Display(640,480)
display1108x819 = Display(1108,819)

class Music:
    def __init__(self, audioFile, volume, typePlay):
        self.audiofile = pygame.mixer.music.load(audioFile)
        self.volume = pygame.mixer.music.set_volume(volume)
        self.typePlay = pygame.mixer.music.play(typePlay)
    def playSound(self):
        return pygame.mixer.Sound(self.audiofile)
    def scroll(self, scroll):
        scroll = 10
        pass

musicPlay = Music(100, "musictheme.wav", -1)
effectSilencer = Music(100, "silencer.wav", -1)
effectCannon = Music(100, "cannon.wav", -1)
effectNotAvailable = Music(100, "not_available.wav", -1)

class DataBase:
    def __init__(self, host, database, user, password):
        self.connection = psycopg2.connect(host= host, database= database, user= user, password= password)



