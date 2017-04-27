from functions_remastered import *
import pygame_textInput_remastered
from pygame_textInput_remastered import *
import psycopg2
import sys



#TODO database login
#Database login: (host= "localhost", database="postgres", user= "postgres", password="WallSpeaker5" )






def Settings():
    image = ImageLoad("Remastered\Images\Settings\settings.jpg")
    image.blit(display)

    while gameState.current == gameState.settings:
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

        display.Update()
    GameStateLoop()

def MenuFunction():
    # fps = Clock(60)

    image = ImageLoad("Remastered\Images\Main_Menu\menu.jpg")
    image.blit(display)

    fontWelcome = Font(None, 100, "Welcome to Battleport", white, "welcome")
    fontWelcome.blit(display,10)

    fontFight = Font(None, 100, "Fight", white, "fight")
    fontFight.blit(display,160)

    fontRules = Font(None, 100, "Rules and instructions", white, "rules")
    fontRules.blit(display,310)

    fontScores = Font(None, 100, "High Scores", white, "scores")
    fontScores.blit(display,460)

    fontSettings = Font(None, 100, "Settings", white, "settings" )
    fontSettings.blit(display,610)

    fontMakingOf = Font(None, 100, "Making of", white, "making")
    fontMakingOf.blit(display,760)

    fontQuit = Font(None, 100, "Quit", red, "quit")
    fontQuit.blit(display,910)

    while gameState.current == gameState.menu:
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
            fontFight.Rect(display, black, MouseX, MouseY, events)
            fontRules.Rect(display, black, MouseX, MouseY, events)
            fontScores.Rect(display, black, MouseX, MouseY, events)
            fontSettings.Rect(display, black, MouseX, MouseY, events)
            fontMakingOf.Rect(display, black, MouseX, MouseY, events)
            fontQuit.Rect(display, black, MouseX, MouseY, events)

        display.Update()
    GameStateLoop()

def GameStateLoop():
    gameStateLoop = True
    while gameStateLoop:
        for events in pygame.event.get():
            if gameState.current == gameState.menu:
                MenuFunction()
            elif gameState.current == gameState.settings:
                Settings()
        display.Update()
        gameStateLoop = False

GameStateLoop()