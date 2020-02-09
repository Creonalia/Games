from setup import *



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

             