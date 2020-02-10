from classes import *

# pygame setup
window = pygame.display.set_mode([800, 1000])
clock = pygame.time.Clock()
times_new_roman = pygame.freetype.SysFont(None, 50)

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
            game.board.move(x, positive)

    game.draw(window, times_new_roman)

    pygame.display.flip()
    clock.tick(30)
# credits