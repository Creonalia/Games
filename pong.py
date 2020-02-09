import pygame
import pygame.freetype
import random
pygame.init()

# pygame variables
w = pygame.display.set_mode([600,600])
c = pygame.time.Clock()
f = pygame.freetype.SysFont("Wingdings", 40)

# game variables
white = (255,255,255)
pspeed = 10
xspeed = random.choice([10, -10])
yspeed = random.randint(-10, 10) 
player = pygame.Rect(10, 275, 20, 50)
player2 = pygame.Rect(580, 275, 20, 50)
ball = pygame.Rect(300, 300, 10, 10)
p1 = 0
p2 = 0

# main loop
running = True
while running:
    # check for quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
    
    # paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if player2.y > pspeed:
            player2.y -= pspeed
    if keys[pygame.K_DOWN]:
        if player2.y < 550 - pspeed:
            player2.y += pspeed
    if keys[pygame.K_w]:
        if player.y > pspeed:
            player.y -= pspeed
    if keys[pygame.K_s]:
        if player.y < 550 - pspeed:
            player.y += pspeed
    
    # ball movememt
    if (ball.y > 600 or ball.y < 0):
        yspeed *= -1
    if ball.x > 600:
        p1 += 1  
        ball = pygame.Rect(300, 300, 10, 10)
        yspeed = random.randint(-10, 10)
        xspeed = random.choice([10, -10])
    elif ball.x < 0:
        p2 += 1
        ball = pygame.Rect(300, 300, 10, 10)
        yspeed = random.randint(-10, 10)
        xspeed = random.choice([10, -10])

    if pygame.Rect.colliderect(player, ball) or pygame.Rect.colliderect(player2, ball):
        xspeed*= -1

    ball.x += xspeed
    ball.y += yspeed
    
    # draw
    w.fill((0, 0, 0))
    pygame.draw.rect(w, white, player)
    pygame.draw.rect(w, white, player2)
    pygame.draw.rect(w, (150,150,150), (250, 10, 100, 50))
    f.render_to(w, (260, 13), str(p1))
    f.render_to(w, (310, 13), str(p2))
    pygame.draw.rect(w, white, ball)
    pygame.display.flip()
    c.tick(30)