def the_player1winner():
    global the_player_1

    pygame.display.set_caption("Players")
    screen2 = pygame.display.set_mode((display_width1, display_height1))
    pygame.display.update()

    ''''Background image'''
    the_image2000 = "player1winner.png"
    screen_image2000 = pygame.display.set_mode((display_width1, display_height1))
    menu_image2000 = pygame.image.load(the_image2000)
    screen_image2000.blit(menu_image2000, (0, 0))

    ''''Fonts'''
    pygame.display.set_caption("Font")
    my_font = pygame.font.Font(None, 150)
    thewinner1_font = my_font.render(str(the_player_1), 5, black)

    ''''Mouse'''
    (MouseX, MouseY) = pygame.mouse.get_pos()

    players = True
    while players == True:

        for events in pygame.event.get():
            screen2.blit(thewinner1_font, (380, 250))
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_SPACE:
                    pygame.quit();
                    sys.exit()

            elif events.type == pygame.MOUSEBUTTONDOWN:
                print(MouseX, MouseY)
                print("Mouse Button up")
            elif events.type == pygame.MOUSEBUTTONUP:
                print(MouseX, MouseY)
                print("Mouse Button down")

            elif events.type == pygame.MOUSEMOTION:
                print("mouse at " + " " + str(MouseX) + " " + str(MouseY))

            (MouseX, MouseY) = pygame.mouse.get_pos()

        pygame.display.update()