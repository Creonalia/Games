import tanks
import pygame
import pygame.freetype
pygame.init()

w = pygame.display.set_mode([600, 600])
c = pygame.time.Clock()
font = pygame.freetype.SysFont("Times New Roman", 40)

tank1 = tanks.Tank(50, 270, (pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d))
tank2 = tanks.Tank(500, 270, (pygame.K_UP, pygame.K_LEFT, pygame.K_DOWN, pygame.K_RIGHT))
end_round = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                tank1.shoot()
            if event.key == pygame.K_RETURN:
                tank2.shoot()

    stuff = [tank1, tank2, tank1.shot, tank2.shot]
    w.fill((255, 255, 255))
    for i in stuff:
        i.move()
        if isinstance(i, tanks.Tank):
            if i.x > 600 - i.width:
                i.x = 600 - i.width
            elif i.x < 0:
                i.x = 0
            if i.y < 0:
                i.y = 0
            elif i.y > 600 - i.height:
                i.y = 600 - i.height

            if i is tank1:
                other_tank = tank2
            else:
                other_tank = tank1
            if pygame.Rect.colliderect(i, other_tank):
                if i.y > other_tank.y:
                    i.y = other_tank.y + other_tank.height
                elif i.y < other_tank.y:
                    i.y = other_tank.y - i.height
                elif i.x > other_tank.x:
                    i.x = other_tank.x + other_tank.width
                elif i.x < other_tank.x:
                    i.x = other_tank.x - i.width
            if pygame.Rect.colliderect(i, other_tank.shot):
                i.health -= 1
                other_tank.shot = tanks.Shot(-100, -100, i.direction)
                if i.health <= 0:
                    other_tank.wins += 1
                    end_round = True
                    break

        pygame.draw.rect(w, i.color, i)

    if end_round:
        if other_tank is tank1:
            winner = "Player 1"
        else:
            winner = "Player 2"
        font.render_to(w, (200, 200), str(winner + " wins"))
        pygame.display.flip()
        pygame.time.wait(300)
        running = False

    c.tick(30)
    pygame.display.flip()
