import pygame
import sys
import random

''''Initalizes pygame'''
pygame.init()

''''Colours'''
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
yellow = (255,255,0)
blue = (0,0,255)

''''Clock fps'''
def clock(fps):
    clock = pygame.time.Clock()
    clock.tick(fps)

''''The mouse'''
(MouseX, MouseY) = pygame.mouse.get_pos()

''''menu coordinations positions'''
class title_position: #640 * 480 resolution class
    def __init__(self, BeginX, EndX, BeginY, EndY):
        self.beginX = BeginX
        self.endX = EndX
        self.beginY = BeginY
        self.endY = EndY

''''The coordinations of the title'''
menu_title = title_position(4,70,5,63)
endturn_title = title_position(4,70,360,450)
nordeck_title = title_position(4,70,540,600)
spcdeck_title = title_position(4,70,645,700)
playerhead_title = title_position(855,1020,0,35)
normalcard1_title = title_position(775,935,65,180)


''''Figure making'''
def figure(image, colour, colour1, x,y,width, height, tickness):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
         pygame.draw.rect(image, colour, (x,y,width,height), tickness)

    else:
         pygame.draw.rect(image, colour1, (x, y, width, height), tickness)


''''Display'''
display_width = 640
display_height = 480
screen1 = pygame.display.set_mode((display_width, display_height))

''''DISPLAY REAL ONE'''''
display_width1 = 1108
display_height1 = 819


def display_resolution(resolutionclick):
        display_width = 640
        display_height = 480
        info = pygame.display.Info()
        if resolutionclick == 0:
            return pygame.display.set_mode((display_width, display_height))
        elif resolutionclick == 1:
            return pygame.display.set_mode((800,600), pygame.FULLSCREEN)
        elif resolutionclick == 2:
            return pygame.display.set_mode((display_width, display_height), pygame.FULLSCREEN)
        elif resolutionclick == 3:
            pygame.display.set_mode((display_width, display_height), pygame.FULLSCREEN)

''''Resolution'''
resolutionclicker = 3


''''--------------------------------------------------------------------------------------------------------------'''
''''MUSIC'''
"Volume"
volume = 100
pygame.mixer.music.load("musictheme.wav")
pygame.mixer.music.set_volume(volume)
pygame.mixer.music.play(-1)



def music(location, type,):
    pygame.mixer.music.load(location)
    pygame.mixer.music.play(type)


''''the audio effect'''
effect = pygame.mixer.Sound('silencer.wav')
effect1 = pygame.mixer.Sound('cannon.wav')

''''Players'''
effect1000 = pygame.mixer.Sound('Not_available.wav')

''''Volume fix'''
scroll = 10

