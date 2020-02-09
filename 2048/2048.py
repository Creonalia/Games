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
                pass
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                pass
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                pass
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                pass
    game.draw(window, times_new_roman)
    clock.tick(30)
# credits