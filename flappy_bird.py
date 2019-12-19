import pygame
import pygame.freetype
import random
pygame.init()
w = pygame.display.set_mode([500,400])
f = pygame.freetype.SysFont("Times New Roman", 50, bold=False, italic=False)
r = True
start = False
c = pygame.time.Clock()
width = 100
at = pygame.Rect(150, 0, width, 200)
ab = pygame.Rect(150, 300, width, 300)
bt = pygame.Rect(400, 0, width, 100)
bb = pygame.Rect(400, 200, width, 300)
ct = pygame.Rect(650, 0, width, 150)
cb = pygame.Rect(650, 250, width, 350)
player = pygame.Rect(75, 200, 20, 20)
btl = (at,bt,ct)
bl = (at, ab, bt, bb, ct, cb)
bspeed = 3
score = 0
bc = (70, 50, 70)
while not start:
    w.fill((200,220,255))
    pygame.draw.rect(w, (100,100,100), player)
    f.render_to(w, (5,5), str(score))
    f.render_to(w, (100,175), "Click to start")
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            start = True
pygame.time.wait(100)
#loop
while r:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            r = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            player.y -= 30
    # move blocks
    for b in btl:
        b.x -= bspeed
    player.y += 5
    # reset blocks
    for b in btl:
        if b.x <= -width:
            b.x = 650
            b.height = random.randint(0, 250)
            
    for b in btl:
        if b.x + width >= player.x  and b.x + width < player.x + bspeed:
            score += 1
            
    ab.x = at.x
    bb.x = bt.x
    cb.x = ct.x
    ab.y = at.height + width
    bb.y = bt.height + width
    cb.y = ct.height + width
    #check for end game
    if player.y >= 400 or player.y <= -player.height:
        r = False
    for i in btl:
        if player.x + player.height >= i.x and player.x <= i.x + width:
             if player.y <= i.height or player.y >i.height + width- player.height:
                r = False


    # draw
    w.fill((200,220,255))
    pygame.draw.rect(w, (100,100,100), player)
    for i in bl:
        pygame.draw.rect(w, bc, i)

    f.render_to(w, (5,5), str(score))
    c.tick(25)
    pygame.display.flip()

print("Your score is " + str(score))