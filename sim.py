import random
import pygame
import pygame.freetype
pygame.init()

# colors
light_color = (200, 200, 200)
mid_color = (175, 175, 175)
dark_color = (100, 100, 100)
green = (50, 100, 20)
yellow = (200, 200, 100)
red = (200, 80, 80)
white = (255, 255, 255)
black = (0, 0, 0)
kind_color = {"None": dark_color, "Economy": green, "Population": red, "Happiness": yellow}


class Block(pygame.Rect):
    def __init__(self, x, y, kind = "None", color = dark_color, width = 200, height = 200):
        self.x = x * 200
        self.y = y * 200
        self.width = width
        self.height = height
        pygame.Rect.__init__(self, self.x, self.y, width, height)
        self.kind = kind
        self.color = kind_color[kind]

    def change_kind(self, button):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.kind = button.kind
        self.color = kind_color[self.kind]


class Button(pygame.Rect):
    def __init__(self, y, kind, cost = 200, x = 600, width = 200, height = 200):
        self.x = x
        self.y = y * 200
        self.width = width
        self.height = height
        pygame.Rect.__init__(self, self.x, self.y, width, height)
        self.color = light_color
        self.kind = kind
        self.cost = cost

    def change_color(self):
        if self.collidepoint(pygame.mouse.get_pos()):
            self.color = mid_color
        else:
            self.color = light_color


def calc_money(values, blocks):
    money = values["Economy"]
    if values["Population"] <= (blocks["Economy"] * 20):
        money += ((values["Population"] * values["Happiness"]/100)+ 1) * 20

    else:
        money +=(((blocks["Economy"] * 20)* values["Happiness"]/100) + 1) * 20

    return money


def calc_happiness(values, blocks):
    happiness = values["Happiness"] - 3
    if values["Population"] > blocks["Population"] * 20:
        happiness -= 1
    happiness += blocks["Happiness"] * 3
    if happiness > 100:
        happiness = 100
    elif happiness < 0:
        happiness = 0
    return happiness


def calc_population(values, blocks):
    population = values["Population"]
    if values["Happiness"] >= 50 and values["Population"] <= (blocks["Population"] + 1)* 20:
        if random.randint(1, 100) > 90:
            population += 1
    else:
        if random.randint(1, 100) > 99:
            population -= 1
    return population


# setup
window = pygame.display.set_mode([800,600])
clock = pygame.time.Clock()
font = pygame.freetype.SysFont("Times New Roman", 20)

# create blocks
block_0 = Block(0, 0, "Economy")
block_1 = Block(1, 0, "Population")
block_2 = Block(2, 0, "Happiness")
block_3 = Block(0, 1)
block_4 = Block(1, 1)
block_5 = Block(2, 1)
block_6 = Block(0, 2)
block_7 = Block(1, 2)
block_8 = Block(2, 2)
blocks = [block_0, block_1, block_2, block_3, block_4, block_5, block_6, block_7, block_8]

buttons = (Button(0, "Economy"), Button(1, "Population"), Button(2, "Happiness"))

# variables
selected_block = block_0
middle = (300, 200)
values = {"Economy": 200, "Population": 10, "Happiness": 50}
block_count = {"None": 6, "Economy": 1, "Population": 1, "Happiness": 1}
hour = 0
minute = 0
day = 1

# main loop
running = True
while running:

    for button in buttons:
        button.change_color()

    # event loop
    for event in pygame.event.get():
        # quit
        if event.type == pygame.QUIT:
            running = False
            break
        # player click
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for button in buttons:
                button.change_color()
                if button.collidepoint(pygame.mouse.get_pos()):
                    if values["Economy"] >= button.cost:
                        selected_block.change_kind(button)
                        values["Economy"] -= button.cost
                        block_count[button.kind] += 1
                    else:
                        font.render_to(window, middle, "Not enough money")
                        pygame.display.flip()
                        pygame.time.wait(20)

            for block in blocks:
                if block.collidepoint(pygame.mouse.get_pos()):
                    selected_block = block

    # update values
    if hour == 17 and minute == 0:
        values["Economy"] = calc_money(values, block_count)
    minute += 10
    if minute == 60:
        minute = 0
        hour += 1
        if hour == 24:
            day += 1
            hour = 0
    values["Population"] = calc_population(values, block_count)
    values["Happiness"] = calc_happiness(values, block_count)
    # draw
    window.fill(white)

    for button in buttons:
        pygame.draw.rect(window, button.color, button)
    for block in blocks:
        pygame.draw.rect(window, block.color, block)
        font.render_to(window, (block.x + 10, block.y + 10), block.kind)
    for x in range(0, 800, 200):
        pygame.draw.line(window, black, (x, 0), (x, 600))
    for y in range(0, 600, 200):
        pygame.draw.line(window, black, (0, y), (800, y))
    pygame.draw.rect(window, (80, 200, 50), selected_block, 3)

    # print text
    font.render_to(window, (10, 30), "Day " + str(day))
    if minute < 10:
        font.render_to(window, (10, 50), str(hour) + ":0" + str(minute))
    else:
        font.render_to(window, (10, 50), str(hour) + ":" + str(minute))
    for button in buttons:
        font.render_to(window, (button.x + 10, button.y + 10), button.kind + ": " + str(values[button.kind]))

    pygame.display.flip()
    clock.tick(60)
