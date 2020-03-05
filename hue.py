import random
import pygame
pygame.init()

w = pygame.display.set_mode([200, 200])
p = True

while p:
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    color = (red, green, blue)

    r = pygame.Rect(0, 0, 200, 200)
    pygame.draw.rect(w, color, r)

    pygame.display.flip()
    print()
    redg = int(input("How much red? "))
    greeng = int(input("How much green? "))
    blueg = int(input("How much blue? "))
    colorg = (redg, greeng, blueg)

    wg = pygame.display.set_mode([400, 200])
    wg.fill(colorg)
    pygame.draw.rect(w, color, r)

    pygame.display.flip()

    print("You guessed " + str(colorg))
    print("It was " + str(color))
    if red > redg:
        print("Red was " + str(red - redg) + " too high")
    else:
        print("Red was " + str(redg - red) + " too low")
    if green > greeng:
        print("Green was " + str(green - greeng) + " too high")
    else:
        print("Green was " + str(greeng - green) + " too low")
    if blue > blueg:
        print("Blue was " + str(blue - blueg) + " too high")
    else:
        print("Blue was " + str(blueg - blue) + " too low")
    p = input("Again? ").lower() == "yes"
