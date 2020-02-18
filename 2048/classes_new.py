import random
import pygame
import pygame.freetype
pygame.init()

class Cell(pygame.Rect):
    colors = (
        (238, 228, 218), (236, 224, 202), (247, 171, 109), (245, 149, 101), 
        (245, 124, 95), (246, 93, 59), (237, 206, 113), (237, 205, 92), 
        (237, 199, 80), (237, 196, 64), (237, 193, 46), (62, 57, 51)
        )
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
        """Draws the value of the block"""
        value_text = font.render(str(self.value))[0]
        value_position = value_text.get_rect(center = self.center)
        window.blit(value_text, value_position)
              
class Board(): 

    def __init__(self, mode):
        self.size = mode.size
        self.cell_size = mode.cell_size
        self.number_of_cells = self.size ** 2
        # creates empty board and adds 2 random blocks
        self.cells = [Cell(i, self.cell_size) for i in range(16)]
        self.make_new_block(mode)
        self.make_new_block(mode)

    def move_blocks(self, x, positive, game):
        """Moves all blocks in the board"""
        # generates indexes of cell for each row/column
        for i in range(4):
            if x:
                indexes = list(range(i * self.size, (i + 1) * self.size))
            else:
                indexes = list(range(i, self.number_of_cells, self.size))
            if positive:
                indexes.reverse()

            for j in indexes:
                has_merged = False
                current_cell = self.cells[j]
                neighbor = self.cells[indexes[indexes.index(j) - 1]]

                if current_cell.value > 0:
                    while current_cell is not self.cells[indexes[0]]:
                        # moves if neighbor is empty
                        if neighbor.value == 0:
                            neighbor.value = current_cell.value
                            current_cell.value = 0
                            j = indexes[indexes.index(j) - 1]
                            current_cell = self.cells[j]
                            neighbor = self.cells[indexes[indexes.index(j) - 1]]
                        # merges blocks
                        elif current_cell.value == neighbor.value and not has_merged:
                            current_cell.value = game.mode.increase(current_cell.value)
                            game.score += 2 ** (game.mode.values.index(current_cell.value) + 1)
                            neighbor.value = 0
                            has_merged = True   
                        else:
                            break  

    def check_can_move(self):
        """Checks if the player can move"""
        if not self.check_full():
            return True

        # checks if adjacent cells are the same
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
        """Checks if the board is full"""
        for cell in self.cells:
            if cell.value == 0:
                return False
        return True

    def make_new_block(self, mode):
        """Makes random new block"""
        empty_blocks = [i for i in range(self.size**2) if self.cells[i].value == 0]  
        empty_index = random.choice(empty_blocks)
        if random.randint(0, 10) == 10:
            value = mode.values[1]
        else:
            value = mode.values[0]
        self.cells[empty_index].value = value
    
    def draw_board(self, game):
        """Draws the board"""
        pygame.draw.rect(game.game_surface, Game.board_color, (0, 200, 800, 800))
        for i in range(0, 900, self.cell_size):
            pygame.draw.line(game.game_surface, (188, 174, 161), (i, 200), (i, 1000), Cell.offset * 2)
            pygame.draw.line(game.game_surface, (188, 174, 161), (0, i + 200), (800, i + 200), Cell.offset * 2)
    
        for cell in self.cells: 
            if cell.value > 0:
                if cell.value in game.mode.values:
                    color = Cell.colors[game.mode.values.index(cell.value)]
                else:
                    color = Cell.colors[-1]
                pygame.draw.rect(game.game_surface, color, cell)
                cell.draw_value(game.game_surface, game.font)

class GameMode():

    def __init__(self, start_value = 2, increase_expression = "value * 2", size = 4):
        self.size = size
        self.number_of_cells = size ** 2
        self.cell_size = int(800/size)
        self.values = [start_value]
        self.increase_expression = increase_expression
        for i in range(12):
            self.values.append(self.increase(self.values[-1]))
    
    def increase(self, value):
        """Increases cell value based on game mode"""
        return eval(self.increase_expression)

class Menu():

    def __init__(self, menu_dimensions, button_list, x, y, width, height, offset, window_position):
        self.surface = pygame.Surface(menu_dimensions)
        self.surface.fill(Game.background_color)
        self.buttons = {}
        self.window_position = window_position
        for button in button_list:
            self.buttons[button] = pygame.Rect(x, y, width, height)
            y += height + offset
            pygame.draw.rect(self.surface, Game.board_color, self.buttons[button])
            text = Game.font.render(button)[0]
            position = text.get_rect(center = self.buttons[button].center)
            self.surface.blit(text, position)

class Game():
    modes = {"Normal": GameMode(), "Eleven": GameMode(1, "value + 1")}
    buttons = {"Restart": "Restarting", "Menu": "Menu"}
    background_color = (252, 247, 241)
    board_color = (205, 193, 181)
    dimensions = (800, 1000)

    window = pygame.display.set_mode(dimensions)
    transparent_surface = pygame.Surface([800, 800])
    transparent_surface.set_alpha(150)
    game_surface = pygame.Surface(dimensions)
    clock = pygame.time.Clock()
    font = pygame.freetype.SysFont(None, 50)

    def __init__(self):
        self.score = 0
        # change high_score
        self.high_score = 0
        self.mode = self.modes["Normal"]
        self.state = "Menu"
        self.board = Board(self.mode) 
        self.main_menu = Menu(self.dimensions, self.modes, 300, 200, 200, 100, 20, (0, 0))
        self.game_menu = Menu((300, 200 - Cell.offset), self.buttons, 0, 0, 200, 60, 20, (500, 0))
        self.font.render_to(self.main_menu.surface, (350, 100), "2048")
        self.has_won = False
  
    def update(self):
        """Draws based on current state"""
        if self.state == "Playing":
            self.draw_game()
        elif self.state == "Menu":
            self.window.blit(self.main_menu.surface, self.main_menu.window_position)

        elif self.state == "Won" or self.state == "Lost":
            won = self.state == "Won"
            self.draw_game()
            color = Cell.colors[10] if won else Cell.colors[-1]
            self.transparent_surface.fill(color)
            text = "You won!" if won else "You lost"
            text = Game.font.render(text)[0]
            position = text.get_rect(center = self.transparent_surface.get_rect().center)
            self.window.blit(text, position)
            self.window.blit(self.transparent_surface, (0, 200 - Cell.offset))
        
        elif self.state == "Restarting":
            self.restart()
            
        elif self.state == "Testing":
            for cell in self.board.cells:
                cell.value = self.mode.values[9]
                #cell.value = random.randint(0, 1000000000)
                self.state = "Playing"
        pygame.display.flip()
        self.clock.tick(20)

    def draw_game(self):
        """Draws board and scores"""
        self.game_surface.fill(self.background_color)
        self.board.draw_board(self)
        self.font.render_to(self.game_surface, (20, 20), f"Score: {self.score}")
        self.font.render_to(self.game_surface, (20, 80), f"High Score: {self.high_score}")
        self.game_surface.blit(self.game_menu.surface, self.game_menu.window_position)
        self.window.blit(self.game_surface, (0, 0))
        
    def restart(self, mode = None):
        """Resets the game"""
        self.mode = mode if mode else self.mode
        self.score = 0
        self.board = Board(self.mode)
        self.state = "Playing"
        self.has_won = False
 
    def move(self, x, positive):
        """Moves all blocks"""
        if self.board.check_can_move():
            old_board_values = [cell.value for cell in self.board.cells]
            self.board.move_blocks(x, positive, self)

            # does not create new block if board is full or the board did not change
            if not self.board.check_full() and old_board_values != [cell.value for cell in self.board.cells]:
                self.board.make_new_block(self.mode)
        
        if self.score > self.high_score:
            self.high_score = self.score
        if not self.board.check_can_move():
            self.state = "Lost"   
        if not self.has_won:
            self.check_win() 

    def check_win(self):
        for block in self.board.cells:
            if block.value == self.mode.values[10]:
                self.state = "Won"
                self.has_won = True