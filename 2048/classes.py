import random
import pygame
import pygame.freetype
pygame.init()

size = 200

class Cell(pygame.Rect):
    colors = {
        2: (238, 228, 218), 4: (236, 224, 202), 8: (247, 171, 109), 
        16: (245, 149, 101), 32: (245, 124, 95), 64: (246, 93, 59), 
        128: (237, 206, 113), 256: (237, 205, 92), 512: (237, 199, 80), 
        1024: (237, 196, 64), 2048: (237, 193, 46), 4096: (62, 57, 51)
        }
    offset = 10
    def __init__(self, position, value = 2):
        x = (position % 4) * size + Cell.offset
        y = (position // 4)* size + Cell.offset + 200
        width = size - Cell.offset * 2
        height = width
        self.value = 2
        super().__init__(x, y, width, height)
                
class Board(): 

    def __init__(self):
        self.cells = [None for i in range(16)]
        # make radom starting block

    def fill_board_with_2048s(self):
        self.cells = [Cell(i, 2048) for i in range(16)]

    def move(self, x, positive):
        for i in range(4):
            if x:
                indexes = [j for j in range(15) if j // 4 == i]
            else:
                indexes = list(range(i * 4, i * 4 + 4))
            if positive:
                indexes.reverse()

            for j in indexes:
                if self.cells[j] != None:
                    while self.cells[j] != self.cells[indexes[0]]:
                        if self.cells[indexes[indexes.index(j) - 1]] == None:
                            self.cells[j] = self.cells[j].move(-size if x else 0, -size if not x else 0) 
                            self.cells[indexes[indexes.index(j) - 1]] = self.cells[j]
                            self.cells[j] = None
                            j = indexes[indexes.index(j) - 1]
                        elif self.cells[j].value == self.cells[indexes[indexes.index(j) - 1]].value:
                            self.cells[j].value *= 2
                            self.cells[indexes[indexes.index(j) - 1]] = None
                        else:
                            break
               
        empty_index = random.choice([i for i in range(16) if self.cells[i] == None])
        self.cells[empty_index] = Cell(empty_index)
        pass

    def draw(self, window, font):
        pygame.draw.rect(window, (205, 193, 181), (0, 200, 800, 800))
        for i in range(0, 900, size):
            pygame.draw.line(window, (188, 174, 161), (i, 200), (i, 1000), Cell.offset * 2)
            pygame.draw.line(window, (188, 174, 161), (0, i + 200), (800, i + 200), Cell.offset * 2)

        for block in self.cells: #[block for block in self.cells if block != None]:
            if block == None:
                continue
            print(block)
            if block.value in Cell.colors:
                pygame.draw.rect(window, Cell.colors[block.value], block)
            else:
                pygame.draw.rect(window, Cell.colors[4096], block)
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
        self.board.cells = [None for i in range(16)]

# high score
# credits
