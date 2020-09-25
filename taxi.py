# libraries
import random
import pygame
import pygame.freetype
pygame.init()

# setup
window = pygame.display.set_mode([600, 600])
clock = pygame.time.Clock()
font = pygame.freetype.SysFont("Times New Roman", 40)

# game variables
lane = 1
car1_lane = 1
car2_lane = 2
car_speed = 10

# drawing variables
road = [(50, 100), (550, 100), (600, 600), (0, 600)]
ground = pygame.Rect(0, 100, 600, 500)
line_color = (130, 130, 75)
player = pygame.Rect(250, 400, 100, 100)
car1 = pygame.Rect((car1_lane * 200) + 50, 601, 100, 100)
car2 = pygame.Rect((car2_lane * 200) + 50, 0, 100, 100)
car1_color = (random.randint(100,255), random.randint(100,255), random.randint(100,255))
car2_color = (random.randint(100,255), random.randint(100,255), random.randint(100,255))

r = int(input("How much red? "))
g = int(input("How much green? "))
b = int(input("How much blue? "))

if r > 255:
    r = 255
elif r < 0:
    r = 0
if g > 255:
    g = 255
elif g < 0:
    g = 0
if b > 255:
    b = 255
elif b < 0:
    b = 0

# main loop
running = True
while running:

    # event loop
    for event in pygame.event.get():

        # check for quit
        if event.type == pygame.QUIT:
            running = False
            break

        # check for player input
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                if lane > 0:
                    lane -= 1

            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                if lane < 2:
                    lane += 1
    # move cars
    player.x = (lane * 200) + 50
    car1.y += car_speed
    car2.y += car_speed

    # check collision
    if pygame.Rect.colliderect(player, car1):
        if car1_lane == lane:
            running = False
    elif pygame.Rect.colliderect(player, car2):
        if car2_lane == lane:
            running = False

    # check car offscreen
    if car1.y > 800:
        car1.y = 0
        car1_lane = random.randint(0,2)
        car1.x = (car1_lane * 200) + 50
        car1_color = (random.randint(100,255), random.randint(100,255), random.randint(100,255))

    if car2.y > 800:
        car2.y = 0
        car2_lane = random.randint(0,2)
        car2.x = (car2_lane * 200) + 50
        car2_color = (random.randint(100,255), random.randint(100,255), random.randint(100,255))
    # draw
    window.fill((175,200,255))
    pygame.draw.rect(window, (50, 100, 50), ground)
    pygame.draw.polygon(window, (30, 30, 30), road)
    pygame.draw.line(window, line_color, (230, 100), (180, 600), 3)
    pygame.draw.line(window, line_color, (370, 100), (420, 600), 3)
    pygame.draw.rect(window, (r,g,b), player)
    pygame.draw.rect(window, car1_color, car1)
    pygame.draw.rect(window, car2_color, car2)
    font.render_to(window, (10, 10), str((pygame.time.get_ticks() / 1000)))


    pygame.display.flip()
    clock.tick(30)