import random
import pygame
import pygame.freetype
pygame.init()

size = 200

class Block(pygame.Rect):
    colors = {
        2: (0,0,0), 4: (0,0,0), 8: (0,0,0), 16: (0,0,0), 32: (0,0,0), 
        64: (0,0,0), 128: (0,0,0), 256: (0,0,0), 512: (0,0,0), 1024: (0,0,0), 
        2048: (0,0,0), 4096: (0,0,0)
        }
    offset = 10
    def __init__(self, column, row, value=2):
        self.column = column
        self.row = row
        self.x = self.column * size + Block.offset
        self.y = self.row * size + Block.offset
        self.width = size - Block.offset * 2
        super().__init__(self.x, self.y, self.width, self.height)
        self.value = value
        
class Board(): 

    def __init__(self):
        self.board = [[None for column in range(0, 4)] for row in range(0, 4)]

    def fill_board_with_2048s_for_no_apparent_reason(self):
        self.board = [[Block(column, row, 2048) for column in range(0, 4)] for row in range(0, 4)]

    def move(self):
        pass

    def draw(self, window, font):
        for block in [block for row in self.board for block in row]:
            if block.value in colors:
                pygame.draw.rect(window, Block.colors[block.value], block)
            else:
                pygame.draw.rect(window)


    def check_end_game():
        pass

class Game():

    def __init__(self):
        self.score = 0

s = Board()
s.draw(1, 1)
# high score
# credits
