from classes_new import *


game = Game()

# main loop
running = True
while running:
    
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        elif event.type == pygame.KEYDOWN:
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
                game.board.move_blocks(x, positive, game)
                if not game.board.check_full():
                    game.board.make_new_block()
    
    if not game.board.check_can_move():
        game.restart()           

    game.draw()
    if game.score > game.high_score:
        game.high_score = game.score

    pygame.display.flip()
    game.clock.tick(30)
