from classes_new import pygame, Game, Game_Mode

normal = Game_Mode()
eleven = Game_Mode(1, "value + 1")
game = Game(normal)
game.draw()

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
            if game.board.check_can_move():
                old_board_values = [cell.value for cell in game.board.cells]
                game.board.move_blocks(x, positive, game)

                # does not create new block if board is full or the board did not change
                if not game.board.check_full() and old_board_values != [cell.value for cell in game.board.cells]:
                    game.board.make_new_block(game.mode)

            if game.score > game.high_score:
                game.high_score = game.score
            game.draw()
            if not game.board.check_can_move():
                game.lose_game()           

    game.clock.tick(30)
