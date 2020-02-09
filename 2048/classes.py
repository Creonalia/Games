import random
import pygame
import pygame.freetype
pygame.init()

size = 200

class Block(pygame.Rect):
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

    def move(self)

    def draw(self, window, font):
        for block in [self.board]

    def check_end_game()

class Game():

    def __init__(self):
        self.score = 0


# high score
# credits
