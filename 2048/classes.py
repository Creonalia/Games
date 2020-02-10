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
    def __init__(self, position, value=2):
        self.x = (position % 4) * size + Block.offset
        self.y = (position // 4)* size + Block.offset + 200
        self.width = size - Block.offset * 2
        self.height = self.width
        super().__init__(self.x, self.y, self.width, self.height)
        self.value = value
        
class Board(): 

    def __init__(self):
        self.board = [None for i in range(16)]
        # make radom starting block

    def fill_board_with_2048s(self):
        self.board = [Block(i, 2048) for i in range(16)]

    def move(self, x, positive):
        for i in range(4):
            if x:
                indexes = [j for j in range(15) if j // 4 == i]
            else:
                indexes = list(range(i, i + 4))
            if positive:
                indexes.reverse()

            for j in indexes:
                block = self.board[j]
                if self.board[j] != None:
                    while block != self.board[indexes[0]]:
                        if self.board[indexes[indexes.index(j) - 1]] == None:
                            self.board[j].move(-size if x else 0, -size if not x else 0)
                            self.board[indexes[indexes.index(j) - 1]] = self.board[j]
                            self.board[j] = None
                            j = indexes[indexes.index(j) - 1]
                        elif self.board[j].value == self.board[indexes[indexes.index(j) - 1]].value:
                            self.board[j].value *= 2
                            self.board[indexes[indexes.index(j) - 1]] = None
                        else:
                            break
               
        empty_index = random.choice([i for i in range(15) if self.board[i] == None])
        self.board[empty_index] = Block(empty_index)

    def draw(self, window, font):
        pygame.draw.rect(window, (205, 193, 181), (0, 200, 800, 800))
        for i in range(0, 900, size):
            pygame.draw.line(window, (188, 174, 161), (i, 200), (i, 1000), Block.offset * 2)
            pygame.draw.line(window, (188, 174, 161), (0, i + 200), (800, i + 200), Block.offset * 2)

        for block in [block for block in self.board if block != None]:
            if block.value in Block.colors:
                pygame.draw.rect(window, Block.colors[block.value], block)
            else:
                pygame.draw.rect(window, Block.colors[4096], block)
            #font.render_to(surf, block., block.value)

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
    def check_end_game():
            pass
    def restart(self):
        self.score = 0
        self.board.board = [None for i in range(16)]

# high score
# credits
