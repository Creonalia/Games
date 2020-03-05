"""
platformer

Description: Main game
"""
from setup import *

# gameplay loop
running = True
while running:

    # check for quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # moves the player
    player.move()

    # edge of room collision
    if player.x > 600 - player.width:
        player.x = 600 - player.width

    elif player.x < 0:
        player.x = 0

    if player.y < 0:
        player.y = 0
        player.jumps = 0
        player.bounces = 0

    # block collision
    for block in rooms[room].blocks:
        if pygame.Rect.colliderect(player, block):

            # check for special blocks
            if block.kind == "Lava":
                player.died = True
                break

            elif block.kind == "Bouncy" and player.y < block.y:
                player.bounces = 10

            elif block.kind == "Exit":
                player.reset_position(ground)
                room += 1
                if room >= len(rooms):
                    running = False
                break

            # move player with moving block
            if block.movement_distance and player.y > block.y:
                if block.axis == "x":
                    player.x += block.speed
                else:
                    player.y += block.speed

            # checks player location and moves player out of block
            if player.y > block.y:
                player.top = block.bottom
                player.jumps = 0
                player.bounces = 0

            elif player.y < block.y:
                player.bottom = block.top
                player.jumps = player.default_jumps

            elif player.x > block.x:
                player.left = block.right

            elif player.x < block.x:
                player.right = block.left

    # prevents errors when the game has ended but the loop has not finished
    if not running:
        break

    # draw room and player
    window.fill((255, 255, 255))
    pygame.draw.rect(window, (0, 0, 0), player)
    rooms[room].animate(window, times_new_roman, ticks % 30)

    # update end statistics
    if rooms[room] is end:
        end.text[1].message = "You died " + str(player.deaths) + " times"
        end.text[2].message = "You played for " + \
            str(pygame.time.get_ticks() // 1000) + " seconds"

    # death animation
    if player.died:
        for i in range(0, 255, 15):
            death_surface.set_alpha(i)
            window.blit(death_surface, (0, 0))
            pygame.display.flip()
            clock.tick(30)

        player.deaths += 1
        player.reset_position(ground)
        player.died = False

    # finish drawing
    pygame.display.flip()
    clock.tick(30)
    ticks += 1
