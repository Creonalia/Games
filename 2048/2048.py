from classes_new import pygame, Game

game = Game()

# main game loop
while game.state != "Quit":
    
    # event loop
    for event in pygame.event.get():

        # check for quit
        if event.type == pygame.QUIT:
            game.state = "Quit"
            break

        # check player movement
        elif event.type == pygame.KEYDOWN and game.state == "Playing":
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                x = False
                positive = False
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                x = True
                positive = False
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                x = False
                positive = True
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                x = True
                positive = True 
            else:
                continue
            game.move(x, positive)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if game.state == "Won":
                game.state = "Playing"
                
            elif game.state == "Menu" or game.state == "Playing":
                main_menu = game.state == "Menu"
                menu = game.main_menu if main_menu else game.game_menu
                for button in menu.buttons:
                        mouse_pos = [pygame.mouse.get_pos()[i] - menu.window_position[i] for i in range(2)]
                        if menu.buttons[button].collidepoint(mouse_pos):
                            if main_menu:
                                game.restart(Game.modes[button]) 
                            else:
                                game.state = game.buttons[button]

    game.update()
