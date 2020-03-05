import classes
import pygame
pygame.init()

game = classes.Game()

while game.state != "Quit":
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.state = "Quit"
        elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
            if game.state == "Not Playing" or game.state == "Lost":
                if game.state == "Lost":
                    game.reset()
                game.state = "Playing"

    game.update()
    game.draw()

    game.clock.tick(30)
