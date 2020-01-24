"""
classes

Description: Defines classes for platformer
Do not run! The main game is platformer.py
"""

#portal block(color, type, draw circle, collide, fix x colision)
# moving block
# floor collision

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
    colors = {"Normal": (100, 100, 100), "Lava": (200, 50, 50), "Bouncy": (50, 50, 200)}
    # initalize blocks
    def __init__(self, x, y, width, height, kind = "Normal", offset = 0):
        self.offset = offset
        self.x = x * 25
        self.y = (y * 25) - self.offset
        self.width = width * 25
        self.height = height * 25 + abs(self.offset)
        super().__init__(self.x, self.y, self.width, self.height)
        self.kind = kind
        if self.kind == "Bouncy":
            self.y -= 7
    
        
        
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
    def draw(self, window, font, ticks):
        for block in self.blocks:
            pygame.draw.rect(window, block.colors[block.kind], block)
            if block.kind == "Lava" and block.height < block.width:
                pygame.draw.line(window,  (230, 150, 150), (block.x, block.y + ticks//2), (block.x + block.width, block.y + ticks//2), 2)
            elif block.kind == "Bouncy":
                if ticks <= 15:
                    block.y += 1
                else:
                    block.y -= 1
        for text in self.text:
            font.render_to(window, text.point, text.message) 