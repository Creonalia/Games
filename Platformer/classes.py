"""
classes

Description: Defines classes for platformer
Do not run! The main game is platformer.py
"""
import pygame
import pygame.freetype
pygame.init()

gravity = 10

class Player(pygame.Rect):
    default_jumps = 15
    jump_height = 20
    speed = 5
    bounce_height = 30

    # initalizing player
    def __init__(self):
        super().__init__(0, 500, 50, 50)
        self.deaths = 0
        self.jumps = self.default_jumps
        self.bounces = 0
        self.died = False    
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
    
    def reset_position(self, block):
        self.x = block.x 
        self.bottom = block.y

class Block(pygame.Rect):

    colors = {"Normal": (100, 100, 100), "Lava": (200, 50, 50), "Bouncy": (50, 50, 200), "Exit": (0,0,0)}

    def __init__(self, x, y, width, height, kind = "Normal", offset = 0, movement_distance = 0, axis = "", speed = 6):
        super().__init__(x * 25, y * 25 - offset, width * 25, height * 25 + abs(offset))
        self.kind = kind
        self.movement_distance = movement_distance
        self.axis = axis
        self.speed = speed
        self.default_y = self.y
        self.default_x = self.x
    
    def move_block(self):
        """Moves moving blocks"""
        if self.axis == "x":
            self.x += self.speed
            if self.x == self.default_x or self.x >= self.default_x + self.movement_distance:
                self.speed *= -1
        if self.axis == "y":
            self.y += block.speed
            if self.y == self.default_y or self.x >= self.default_y + self.movement_distance:
                self.speed *= -1

    def change_size(self, increase):
        """Changes the size of exit blocks"""
        self.x += 1 * increase
        self.y += 1 * increase
        self.width -= 2 * increase
        self.height -= 2 * increase
        
class Text():
    # initalize blocks
    def __init__(self, point, message):
        self.message = message
        self.point = point
        
# class which holds blocks and text for each room       
class Room():

    def __init__(self, blocks = (), text = ()):
        self.blocks = blocks
        self.text = text
    
    # draws all blocks and text in room
    def animate(self, window, font, ticks_30):
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
                    block.change_size(1)
                elif ticks_30 % 2 == 0 or block.width <= 34:
                    block.change_size(-1)
            
            # move moving blocks
            if block.movement_distance:
                block.move_block()
            
        for text in self.text:
            font.render_to(window, text.point, text.message) 