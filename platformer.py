# import libraries
import pygame
import pygame.freetype
pygame.init()

# setup 
w = pygame.display.set_mode([600,600])
c = pygame.time.Clock()
f = pygame.freetype.SysFont("Times New Roman", 40)

pspeed = 5
jspeed = 20
jumps = 15
djumps = jumps
jdelay = 0
bluej = 0
bjspeed = 30
gravity = 10
deaths = 0


player = pygame.Rect(0, 500, 50, 50)
ground = pygame.Rect(0, 550, 600, 500)

room = 4
r1_0 = pygame.Rect(200, ground.y - 1, 400, ground.height + 1) 
r1_1 = pygame.Rect(150,450, 100, 50)
r1_2 = pygame.Rect(300, 350, 100, 50)
r1_3 = pygame.Rect(400, 200, 100, 50)
r1_4 = pygame.Rect(550, 150, 50, 500)
r1_5 = pygame.Rect(550, 100, 50, 50)

r2_0 = pygame.Rect(550, 100, 50, 50)
r2_1 = pygame.Rect(100, 549, 500, 50)
r2_2 = pygame.Rect(550, 150, 50, 450)
r2_3 = pygame.Rect(100, 450, 50, 50)
r2_4 = pygame.Rect(350, 500, 50, 50)
r2_5 = pygame.Rect(500, 400, 50, 50)
r2_6 = pygame.Rect(300, 300, 100, 50)
r2_7 = pygame.Rect(100, 250, 100, 50)
r2_8 = pygame.Rect(350, 150, 100, 50)

r3_0 = pygame.Rect(100, 549, 50, 51)
r3_2 = pygame.Rect(350, 549, 50, 51)
r3_4 = pygame.Rect(500, 450, 50, 50)
r3_5 = pygame.Rect(300, 350, 150, 25)
r3_6 = pygame.Rect(300, 325, 150, 25)
r3_7 = pygame.Rect(350, r3_6.y -1, 50, r3_6.height + 1)
r3_8 = pygame.Rect(50, r3_5.y, 150, r3_5. height)
r3_9 = pygame.Rect(50, 325, 150, 25)
r3_10 = pygame.Rect(100, r3_9.y -1, 50, r3_9.height + 1)
r3_11 = pygame.Rect(0, 200, 30, 50)
r3_12 = pygame.Rect(100, 120, 150,5)
r3_13 = pygame.Rect(100, 95, 150, 25)
r3_14 = pygame.Rect(350, 120, 150, 5)
r3_15 = pygame.Rect(350, 95, 150, 25)
r3_16 = pygame.Rect(550, 150, 50, 450)
r3_17 = pygame.Rect(550, 100, 50, 50)

r0 = ()
r1 = [r1_0, r1_1, r1_2, r1_3, r1_4, r1_5]
r2  = [r2_0, r2_1, r2_2, r2_3, r2_4, r2_5, r2_6, r2_7,r2_8]
r3 = [r3_0, r3_2, r3_4, r3_5, r3_6, r3_7, r3_8, r3_9, r3_10, r3_11, r3_12, r3_13, r3_14, r3_15, r3_16, r3_17]
r4 = []
redb = [r1_0, r1_4, r2_1, r2_2, r3_5, r3_8, r3_12, r3_14, r3_16]
blueb = [r1_2, r3_0, r3_2, r3_4, r3_7, r3_10, r3_11]
rooms = (r0, r1, r2, r3, r4)


gcolor = (100,100,100)
red = (200, 50, 50)
blue = (50, 50, 200)

#gameplay loop
running = True
while running:
    # check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # move player
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_w] or keys[pygame.K_UP]) and jumps:
        player.y -= jspeed
        jumps -= 1
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player.x -= pspeed
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        player.y += pspeed
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player.x += pspeed
    player.y += gravity
    if bluej:
        player.y -= bjspeed
        bluej -= 1
        jumps = 0

    # edge collision
    if player.x > 600:
        player.x = ground.x
        player.y = ground.y - player.height
        room += 1
        if room >= 5:
            room = 0
    elif player.x < 0:
        player.x = 0
    if player.y < 0:
        player.y = 0
        jumps = 0
    # collision with ground         
    if pygame.Rect.colliderect(player, ground):
        player.y = ground.y - player.height
        jdelay += 1
        if jdelay == 10:
            jumps = djumps
            jdelay = 0

    #block collision
    for block in rooms[room]:
        if pygame.Rect.colliderect(player, block):

            # check for special blocks
            if block in redb:
                w.fill((0,0,0))
                pygame.display.flip()
                pygame.time.wait(300)
                deaths += 1                
                player.x = ground.x
                player.y = ground.y - player.height
                continue
            elif block in blueb and player.y < block.y:
                bluej = 10
            

            # collision with block
            if player.y > block.y:
                player.y = block.y + block.height
                jumps = 0
                bluej = 0
            elif player.y < block.y:
                player.y = block.y - player.height
                jumps = djumps
            elif player.x > block.x:
                player.x = block.x + block.width
            elif player.x < block.x:
                player.x = block.x - player.width


    
    # draw
    w.fill((255,255,255))  
    pygame.draw.rect(w, gcolor, ground)
    pygame.draw.rect(w, (0,0,0), player)

    #draw room 
    for block in rooms[room]:
        if block in redb:
            color = red  
        elif block in blueb:
            color = blue
        else:
            color = gcolor
        pygame.draw.rect(w, color, block)
    
    if room == 0:
        f.render_to(w, (1000, 10), "Use WASD or Arrow Keys to move")
    elif room == 4:
        f.render_to(w, (150, 10), "Thanks for playing")
        f.render_to(w, (160, 50), "You died " + str(deaths) + " times")
        

    # finish drawing
    pygame.display.flip()
    c.tick(30)
