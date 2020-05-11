"""a bad whack a mole"""
import pygame
import random
pygame.init()
w = pygame.display.set_mode([600, 600])
c = pygame.time.Clock()
time = 0
points = 0
mole = 9
mole_rect = pygame.Rect(mole // 3 * 200, mole % 3 * 200, 200, 200)

while time < 300:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            time = 999
            break
        if i.type == pygame.MOUSEBUTTONDOWN:
            if pygame.Rect.collidepoint(mole_rect, pygame.mouse.get_pos()):
                points += 1
                w.fill((255, 255, 255))
                pygame.display.flip()
                break

    if time % 15 == 0:
        w.fill((255, 255, 255))
        mole = random.randint(0, 8)
        mole_rect = pygame.Rect(mole // 3 * 200, mole % 3 * 200, 200, 200)
        pygame.draw.rect(w, (0, 0, 0), mole_rect)
        pygame.display.flip()
    time += 1
    c.tick(30)
print(str(points) + "/20 moles hit")
