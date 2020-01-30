"""
classes

Description: Defines classes for platformer
Do not run! The main game is platformer.py
"""
# setup pygame
import pygame
import pygame.freetype
pygame.init()

gravity = 10

# class for player
class Player(pygame.Rect):
    default_jumps = 15
    jump_height = 20
    speed = 5
    bounce_height = 30

    # initalizing player
    def __init__(self):
        self.x = 0
        self.y = 500
        self.width = 50
        self.height = 50
        super().__init__(self.x, self.y, self.width, self.height)
        self.deaths = 0
        self.jumps = self.default_jumps
        self.bounces = 0
    
    # moving player
    def move(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_w] or keys[pygame.K_UP]) and self.jumps:
            self.y -= self.jump_height
            self.jumps -= 1
        else:
            self.jumps = 0
            
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.y += self.speed
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.x += self.speed
        
        self.y += gravity
        
        # makes player bounce off bouncy blocks
        if self.bounces:
            self.y -= self.bounce_height
            self.bounces -= 1
            self.jumps = 0
 

# class for blocks
class Block(pygame.Rect):
    # colors for differnt blocks
    colors = {"Normal": (100, 100, 100), "Lava": (200, 50, 50), "Bouncy": (50, 50, 200), "Exit": (0,0,0)}
    # initalize blocks
    def __init__(self, x, y, width, height, kind = "Normal", offset = 0, movement_distance = 0, axis = "", speed = 6):
        self.offset = offset
        self.x = x * 25
        self.y = (y * 25) - self.offset
        self.width = width * 25
        self.height = height * 25 + abs(self.offset)
        super().__init__(self.x, self.y, self.width, self.height)
        self.kind = kind
        self.movement_distance = movement_distance
        self.axis = axis
        self.speed = speed
        self.default_y = self.y
        self.default_x = self.x

# class for text
class Text():
    # initalize blocks
    def __init__(self, point, message):
        self.message = message
        self.point = point
        
# class which holds blocks and text for each room       
class Room():
    # initalize room
    def __init__(self, blocks = (), text = ()):
        self.blocks = blocks
        self.text = text
    
    # draws all blocks and text in room
    def animate(self, window, font, ticks):
        ticks_30 = ticks % 30
        for block in self.blocks:
            if block.kind != "Exit":
                pygame.draw.rect(window, block.colors[block.kind], block)
                if block.kind == "Lava" and block.height < block.width:
                    pygame.draw.line(window,  (255, 100, 100), (block.x, block.y + ticks_30//2), (block.x + block.width, block.y + ticks_30//2), 2)
                elif block.kind == "Bouncy":
                    if ticks_30 <= 15 and block.y > block.default_y - 7:
                        block.y -= 1
                    else:
                        block.y += 1
            else:
                pygame.draw.ellipse(window, block.colors[block.kind], block)
                if ticks_30 < 15 and ticks_30 % 2 == 0:
                    block.x += 1
                    block.y += 1
                    block.width -= 2
                    block.height -= 2
                elif ticks_30 % 2 == 0 or block.width <= 34:
                    block.x -= 1
                    block.y -= 1
                    block.width += 2
                    block.height += 2
            # move moving blocks
            if block.movement_distance:
                if block.axis == "x":
                    block.x += block.speed
                    if block.x == block.default_x or block.x >= block.default_x + block.movement_distance:
                        block.speed *= -1
                if block.axis == "y":
                    block.y += block.speed
                    if block.y == block.default_y or block.x >= block.default_y + block.movement_distance:
                        block.speed *= -1
            
        for text in self.text:
            font.render_to(window, text.point, text.message) 