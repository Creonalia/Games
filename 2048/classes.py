import random
import pygame
import pygame.freetype
pygame.init()

size = 200

class Block(pygame.Rect):
    colors = {
        2: (238, 228, 218), 4: (236, 224, 202), 8: (247, 171, 109), 
        16: (245, 149, 101), 32: (245, 124, 95), 64: (246, 93, 59), 
        128: (237, 206, 113), 256: (237, 205, 92), 512: (237, 199, 80), 
        1024: (237, 196, 64), 2048: (237, 193, 46), 4096: (62, 57, 51)
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
        pygame.draw.rect(window, (205, 193, 181), (0, 200, 800, 800))
        for i in range(int(Block.offset/2), 800, size):
            pygame.draw.line(window, (188, 174, 161), (i, 200), (i, 1000), Block.offset)
            pygame.draw.line(window, (188, 174, 161), (0, i + 200), (800, i + 200), Block.offset)
        for block in [block for row in self.board for block in row if block]:
            if block.value in colors:
                pygame.draw.rect(window, Block.colors[block.value], block)
            else:
                pygame.draw.rect(window, Block.colors[4096], block)
            # text


    def check_end_game():
        pass

class Game():

    def __init__(self):
        self.score = 0
        self.high_score = 0
        self.board = Board()
    
    def draw(self, window, font):
        window.fill((252, 247, 241))
        self.board.draw(window, font)
        # draw score
        # draw restart button
        pygame.display.flip()

    def restart(self):
        self.score = 0
        self.board.board = [[None for column in range(0, 4)] for row in range(0, 4)]

# high score
# credits
