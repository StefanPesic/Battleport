from functions_remastered import *
import pygame_textInput_remastered
from pygame_textInput_remastered import *
import psycopg2
import sys

#TODO database login
#Database login: (host= "localhost", database="postgres", user= "postgres", password="WallSpeaker5" )

def menuFunction():
    fps = Clock(60)

    display = Display("1108x819", 1600,900)
    display.Update()

    image = ImageLoad("menu.jpg")
    image.blit(display)

    font = Font(None, 90, "Menutest", white)
    font.blit(display,350,10)


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
                    pygame.quit();
                    sys.exit()

            # the_menu_click(MouseX, MouseY)
            (MouseX, MouseY) = pygame.mouse.get_pos()

        pygame.display.update()


menuFunction()

