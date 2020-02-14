import random
import pygame
import pygame.freetype
pygame.init()

class Cell(pygame.Rect):
    colors = {
        2: (238, 228, 218), 4: (236, 224, 202), 8: (247, 171, 109), 
        16: (245, 149, 101), 32: (245, 124, 95), 64: (246, 93, 59), 
        128: (237, 206, 113), 256: (237, 205, 92), 512: (237, 199, 80), 
        1024: (237, 196, 64), 2048: (237, 193, 46), 4096: (62, 57, 51)
        }
    offset = 10
    def __init__(self, position, size, value = 0):
        x = (position % 4) * size + Cell.offset
        y = (position // 4)* size + Cell.offset + 200
        width = size - Cell.offset * 2
        height = width
        self.value = value
        self.position = position
        super().__init__(x, y, width, height)
    
    def __repr__(self):
        return f"<cell {self.value}, {self.x}, {self.y}, {self.width}, {self.height}>"

    def draw_value(self, window, font):
        value_text = font.render(str(self.value))[0]
        value_position = value_text.get_rect(center = self.center)
        window.blit(value_text, value_position)
              
class Board(): 

    def __init__(self, size = 4, cell_size = 200):
        self.size = size
        self.cell_size = cell_size
        self.number_of_cells = self.size ** 2
        # creates empty board and adds 2 random blocks
        self.cells = [Cell(i, cell_size) for i in range(16)]
        self.make_new_block()
        self.make_new_block()

    def move_blocks(self, x, positive, game):
        # generates indexes of cell for each row/column
        for i in range(4):
            if x:
                indexes = list(range(i * 4, i * 4 + 4))
            else:
                indexes = list(range(i, 16, 4))
            if positive:
                indexes.reverse()

            for j in indexes:
                has_merged = False
                current_cell = self.cells[j]
                neighbor = self.cells[indexes[indexes.index(j) - 1]]
                if current_cell.value > 0:
                    while current_cell is not self.cells[indexes[0]]:
                        if neighbor.value == 0:
                            neighbor.value = current_cell.value
                            current_cell.value = 0
                            j = indexes[indexes.index(j) - 1]
                            current_cell = self.cells[j]
                            neighbor = self.cells[indexes[indexes.index(j) - 1]]
                        elif current_cell.value == neighbor.value and not has_merged:
                            current_cell.value *= 2
                            game.score += self.cells[j].value
                            neighbor.value = 0
                            has_merged = True   
                        else:
                            break  

    def check_can_move(self):
        if not self.check_full():
            return True
        for i in range(4):
            row_indexes = list(range(i * self.size, i * self.size + self.size))
            column_indexes = list(range(i, 16, 4))
            for indexes in (row_indexes, column_indexes):
                for j in indexes:
                    if j is indexes[0]:
                        continue
                    if self.cells[j].value == self.cells[indexes[indexes.index(j) - 1]].value:
                        return True
        return False
    
    def check_full(self):
        for cell in self.cells:
            if cell.value == 0:
                return False
        return True

    def make_new_block(self):
        empty_blocks = [i for i in range(self.size**2) if self.cells[i].value == 0]  
        empty_index = random.choice(empty_blocks)
        self.cells[empty_index].value = 2
    
    def draw_board(self, window, font):
        pygame.draw.rect(window, (205, 193, 181), (0, 200, 800, 800))
        for i in range(0, 900, self.cell_size):
            pygame.draw.line(window, (188, 174, 161), (i, 200), (i, 1000), Cell.offset * 2)
            pygame.draw.line(window, (188, 174, 161), (0, i + 200), (800, i + 200), Cell.offset * 2)
    
        for cell in self.cells: 
            if cell.value > 0:
                if cell.value in Cell.colors:
                    pygame.draw.rect(window, Cell.colors[cell.value], cell)
                    cell.draw_value(window, font)
                else:
                    pygame.draw.rect(window, Cell.colors[4096], cell)
                    cell.draw_value(window, font)
                
class Button(pygame.Rect):

    def __init__(self, type_, visible, x, y, width, height):              
        super().__init__(x, y, width, height)
        self.type_ = type_
        self.visible = visible

class Game_Mode():

    def __init__(self, mode, start_value, size = 4):
        self.mode = mode
        self.size = size
        self.number_of_cells = size ** 2
        self.cell_size = int(800/size)
        self.start_value = start_value

    def increase(self, value):
        if self.mode == "Normal":
            return value * 2
        elif self.mode == "Eleven":
            return value + 1
class Game():
    #game_mode = {"Normal": (4, 200)}
    window = pygame.display.set_mode([800, 1000])
    clock = pygame.time.Clock()
    font = pygame.freetype.SysFont(None, 50)
    def __init__(self, mode):
        self.score = 0
        # change high_score
        self.high_score = 0
        self.mode = mode
        self.board = Board(self.mode.size, self.mode.cell_size)
        
    
    def draw(self):
        self.window.fill((252, 247, 241))
        self.board.draw_board(self.window, self.font)
        self.font.render_to(self.window, (20, 20), f"Score: {self.score}")
        self.font.render_to(self.window, (20, 80), f"High Score: {self.high_score}")
        # draw restart button
        pygame.display.flip()

    def end_game(self):
        self.restart()

    def restart(self):
        if self.score > self.high_score:
            self.high_score = self.score 
        self.score = 0
        # change game type ?
        self.board = Board(Game.game_mode[mode][0], Game.game_mode[mode][1])
        # end game screen
    

