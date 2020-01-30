"""
setup

Description: Setup for platformer 
Do not run! The main game is platformer.py
"""

# imports classes and all variables
import classes
from classes import *

# pygame variables
window = pygame.display.set_mode([600,600])
surface = pygame.Surface((600, 600))
surface.fill((50, 0, 0))
surface.set_alpha(0)
clock = pygame.time.Clock()
times_new_roman = pygame.freetype.SysFont("Times New Roman", 40)

# game_variables
ticks = 0
room = 0
died = False

# player
player = classes.Player()

# blocks and text
b = classes.Block
t = classes.Text
ground = b(0, 22, 24, 20, "Normal")
exit_0 = b(22, 20, 2, 2, "Exit")
exit_1 = b(22, 2, 2, 2, "Exit")

start_0 = t((10, 10), "Use WASD or Arrow Keys to move.")


end_0 = t((150, 10), "Thanks for playing")
end_1 = t((160, 50), "You died " + str(player.deaths) + " times")
end_2 = t((60, 90), "You played for " + str(pygame.time.get_ticks()/1000) +  " seconds")

r1_0 = b(8, 22, 16, 4, "Lava", 1) 
r1_1 = b(6, 18, 4, 2)
r1_2 = b(12, 14, 4, 2, "Bouncy")
r1_3 = b(16, 8, 4, 2)
r1_4 = b(22, 6, 2, 20, "Lava")
r1_5 = b(22, 4, 2, 2)

r2_0 = b(22, 4, 2, 2)
r2_1 = b(4, 22, 20, 2, "Lava", 1)
r2_2 = b(22, 6, 2, 18, "Lava")
r2_3 = b(4, 18, 2, 2)
r2_4 = b(12, 20, 2, 2)
r2_5 = b(20, 16, 2, 2)
r2_6 = b(12, 12, 4, 2)
r2_7 = b(4, 10, 4, 2)
r2_8 = b(14, 6, 4, 2)

r3_0 = b(2, 22, 2, 2, "Bouncy", 1, 100, "x")
r3_2 = b(12, 22, 2, 2, "Bouncy", 1, 100, "x")
r3_4 = b(20, 18, 2, 2, "Bouncy")
r3_5 = b(12, 14, 6, 1, "Lava")
r3_6 = b(12, 13, 6, 1)
r3_7 = b(12, 13, 2, 1, "Bouncy", 1, 100, "x")
r3_8 = b(2, 14, 6, 1, "Lava")
r3_9 = b(2, 13, 6, 1)
r3_10 = b(2, 13, 2, 1, "Bouncy", 1, 100, "x")
r3_11 = b(0, 10, 2, 2, "Bouncy")
r3_12 = b(3, 5, 7, 1, "Lava")
r3_13 = b(3, 4, 7, 1)
r3_14 = b(13, 5, 6, 1, "Lava")
r3_15 = b(13, 4, 6, 1)
r3_16 = b(22, 6, 2, 18, "Lava")
r3_17 = b(22, 4, 2, 2)


# rooms
start = classes.Room((ground, exit_0), (start_0, ))
r1 = classes.Room((ground, r1_0, r1_1, r1_2, r1_3, r1_4, r1_5, exit_1))
r2 = classes.Room((ground, r2_0, r2_1, r2_2, r2_3, r2_4, r2_5, r2_6, r2_7,r2_8, exit_1))
r3 = classes.Room((ground, r3_0, r3_2, r3_4, r3_5, r3_6, r3_7, r3_8, r3_9, r3_10, r3_11, r3_12, r3_13, r3_14, r3_15, r3_16, r3_17, exit_1))
end = classes.Room((ground, exit_0), (end_0, end_1, end_2))

rooms = (start, r1, r2, r3, end)