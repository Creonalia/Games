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
    if player.x > 600:
        player.x = ground.x 
        player.y = ground.y - player.height
        room = (room + 1) % len(rooms)
        
    elif player.x < 0:
        player.x = 0
        
    if player.y < 0:
        player.y = 0
        player.jumps = 0


    #block collision
    for block in rooms[room].blocks:
        if pygame.Rect.colliderect(player, block):

            # check for special blocks
            if block.kind == "Lava":
                
                # death animation
                for i in range(0, 255, 15):
                    surface.set_alpha(i)
                    window.blit(surface, (0, 0))
                    pygame.display.flip()
                    clock.tick(30)
                    
                player.deaths += 1                
                player.x = ground.x
                player.y = ground.y - player.height
                continue
                
            elif block.kind == "Bouncy" and player.y < block.y:
                player.bounces = 10
            

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
           
        

    # draw room and player
    window.fill((255,255,255))  
    pygame.draw.rect(window, (0,0,0), player)
    rooms[room].draw(window, times_new_roman, ticks)


    # finish drawing
    pygame.display.flip()
    clock.tick(30)
    ticks = (ticks + 1) % 30
   