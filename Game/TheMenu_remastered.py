from functions_remastered import *
import pygame_textInput_remastered
from pygame_textInput_remastered import *
import psycopg2
import sys

#TODO database login
#Database login: (host= "localhost", database="postgres", user= "postgres", password="WallSpeaker5" )

def menuFunction():
    fps = Clock(60)

    display = Display("Fullscreen")

    image = ImageLoad("menu.jpg")
    image.blit(display)

    font = Font(None, 100, "Welcome to Battleport", white)
    font.blit(display,10)

    font = Font(None, 100, "Fight", white)
    font.blit(display,160)

    font = Font(None, 100, "Rules and instructions", white)
    font.blit(display,310)

    font = Font(None, 100, "High Scores", white)
    font.blit(display,460)

    font = Font(None, 100, "Settings", white)
    font.blit(display,610)

    font = Font(None, 100, "Making of", white)
    font.blit(display,760)

    font = Font(None, 100, "Quit", red)
    font.blit(display,910)

    font.Rect(display,white)


    mainMenu = True
    while mainMenu == True:
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

        display.Update()


menuFunction()

