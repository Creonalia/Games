import pygame
import random
pygame.init()
w = pygame.display.set_mode([600,600])
c = pygame.time.Clock()
time = 0
points = 0
mole = 9
while time < 300:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            time = 999
            break
        if i.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            if x >= (mole//3)*200 and x <=((mole//3)+1)*200 and y > (mole%3)*200 and y <((mole%3+1))*200:
                points += 1
                w.fill((255,255,255))
                pygame.display.flip()
                break
    if time % 15 == 0:     
        w.fill((255,255,255))
        mole = random.randint(0,8)
        pygame.draw.polygon(w, (0,0,0), [((mole//3)*200,(mole%3)*200),(((mole//3)+1)*200,(mole%3)*200), (((mole//3)+1)*200,((mole%3+1))*200), ((mole//3)*200,((mole%3+1))*200)])
        pygame.display.flip()
    time += 1
    c.tick(30)
print(str(points) + "/20 moles hit")