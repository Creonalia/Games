from classes_new import *

# pygame setup
window = pygame.display.set_mode([800, 1000])
clock = pygame.time.Clock()
pygame_font = pygame.freetype.SysFont(None, 50)

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
            if game.board.check_can_move:
                game.board.move(x, positive, game)
            else:
                game.restart()

    game.draw(window, pygame_font)
    if game.score > game.

    pygame.display.flip()
    clock.tick(30)
# creditsa