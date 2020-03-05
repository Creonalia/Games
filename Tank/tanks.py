"""
tanks

Description:
"""
import pygame
pygame.init()
shot_speed = 20
tank_speed = 10


class Tank(pygame.Rect):
    color = (0, 0, 0)
    def __init__(self, x, y, controls):

        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        super().__init__(self.x, self.y, self.width, self.height)
        self.controls = controls
        self.direction = "Up"
        self.shot = Shot(-1000, -1000, self.direction)
        self.health = 3
        self.wins = 3

    def shoot(self):

        if self.shoot:
            self.shot = Shot(self.x + 25, self.y + 25, self.direction)

    def move(self):

        keys = pygame.key.get_pressed()
        if keys[self.controls[0]]:
            self.direction = "Up"
            self.y -= tank_speed

        if keys[self.controls[1]]:
            self.direction = "Left"
            self.x -= tank_speed

        if keys[self.controls[2]]:
            self.direction = "Down"
            self.y += tank_speed

        if keys[self.controls[3]]:
            self.direction = "Right"
            self.x += tank_speed


class Shot(pygame.Rect):

    color = (200, 50, 50)
    def __init__(self, x, y, direction):

        self.x = x
        self.y = y
        self.width = 10
        self.height = 10
        super().__init__(self.x, self.y, self.width, self.height)
        self.direction = direction

    def move(self):
        if self.direction == "Up":
            self.y -= shot_speed
        elif self.direction == "Left":
            self.x -= shot_speed
        elif self.direction == "Down":
            self.y += shot_speed
        elif self.direction == "Right":
            self.x += shot_speed
