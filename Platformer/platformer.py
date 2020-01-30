"""
platformer

Description: Main game
"""
# imports setup and all variables
import setup
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


    #block collision
    for block in rooms[room].blocks:
        if pygame.Rect.colliderect(player, block):

            # check for special blocks
            if block.kind == "Lava":
                died = True
                break
                
            elif block.kind == "Bouncy" and player.y < block.y:
                player.bounces = 10
                
            elif block.kind == "Exit":
                player.x = ground.x 
                player.y = ground.y - player.height
                room += 1
                if room >= len(rooms):
                    running = False
                break
            # move player with moving block
            if block.movement_distance:
                if block.axis == "x":
                    player.x += block.speed
                else:
                    player.y += block.speed   

            # checks player location and moves player out of block 
            if player.y > block.y:
                player.y = block.y + block.height
                player.jumps = 0
                player.bounces = 0
                
            elif player.y < block.y:
                player.y = block.y - player.height
                player.jumps = player.default_jumps
                
            elif player.x > block.x:
                player.x = block.x + block.width
                
            elif player.x < block.x:
                player.x = block.x - player.width
                
    # prevents errors when the game has ended but the loop has not finished
    if running == False:
        break

    # draw room and player
    window.fill((255,255,255))  
    pygame.draw.rect(window, (0,0,0), player)
    rooms[room].animate(window, times_new_roman, ticks)
    
    # update end statistics
    end_1 = t((160, 50), "You died " + str(player.deaths) + " times")
    end_2 = t((60, 90), "You played for " + str(pygame.time.get_ticks()/1000) +  " seconds") 
    end = classes.Room((ground, exit_0), (end_0, end_1, end_2))

    rooms = (start, r1, r2, r3, end)
    
    # death animation
    if died:
        
        for i in range(0, 255, 15):
            surface.set_alpha(i)
            window.blit(surface, (0, 0))
            pygame.display.flip()
            clock.tick(30)
            
        player.deaths += 1                
        player.x = ground.x
        player.y = ground.y - player.height
        died = False
    
    # finish drawing
    pygame.display.flip()
    clock.tick(30)
    ticks += 1