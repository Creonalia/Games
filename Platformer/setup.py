"""
setup

Description: Setup for platformer
Do not run! The main game is platformer.py
"""

from classes import *

# pygame variables
window = pygame.display.set_mode([600, 600])
death_surface = pygame.Surface((600, 600))
death_surface.fill((50, 0, 0))
death_surface.set_alpha(0)
clock = pygame.time.Clock()
times_new_roman = pygame.freetype.SysFont("Times New Roman", 40)

# game_variables
ticks = 0
room = 0

player = Player()

ground = Block(0, 22, 24, 20, "Normal")
exit_low = Block(22, 20, 2, 2, "Exit")
exit_high = Block(22, 2, 2, 2, "Exit")

# rooms
start = Room((ground, exit_low), (Text((10, 10), "Use WASD or Arrow Keys to move."), ))
r1 = Room((
    ground, Block(8, 22, 16, 4, "Lava", 1), Block(6, 18, 4, 2), Block(12, 14, 4, 2, "Bouncy"),
    Block(16, 8, 4, 2), Block(22, 6, 2, 20, "Lava"), Block(22, 4, 2, 2), exit_high
    ))
r2 = Room((
    ground, Block(22, 4, 2, 2), Block(4, 22, 20, 2, "Lava", 1),
    Block(22, 6, 2, 18, "Lava"), Block(4, 18, 2, 2), Block(12, 20, 2, 2),
    Block(20, 16, 2, 2), Block(12, 12, 4, 2), Block(4, 10, 4, 2), Block(14, 6, 4, 2), exit_high
    ))
r3 = Room((
    ground, Block(2, 22, 2, 2, "Bouncy", 1, 100, "x"), Block(12, 22, 2, 2, "Bouncy", 1, 100, "x"),
    Block(20, 18, 2, 2, "Bouncy"), Block(12, 14, 6, 1, "Lava"), Block(12, 13, 6, 1),
    Block(12, 13, 2, 1, "Bouncy", 1, 100, "x"), Block(2, 14, 6, 1, "Lava"), Block(2, 13, 6, 1),
    Block(2, 13, 2, 1, "Bouncy", 1, 100, "x"), Block(0, 10, 2, 2, "Bouncy"),
    Block(3, 5, 7, 1, "Lava"), Block(3, 4, 7, 1), Block(13, 5, 6, 1, "Lava"),
    Block(13, 4, 6, 1), Block(22, 6, 2, 18, "Lava"), Block(22, 4, 2, 2), exit_high
    ))
end = Room((ground, exit_low), [
    Text((150, 10), "Thanks for playing"),
    Text((160, 50), "You died " + str(player.deaths) + " times"),
    Text((100, 90), "You played for " + str(pygame.time.get_ticks() // 1000) + " seconds")
    ])

rooms = (start, r1, r2, r3, end)
