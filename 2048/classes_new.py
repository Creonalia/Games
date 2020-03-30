import random
# import shelve
import pygame
import pygame.freetype
pygame.init()


class Cell(pygame.Rect):
    colors = [
        (238, 228, 218), (236, 224, 202), (247, 171, 109), (245, 149, 101),
        (245, 124, 95), (246, 93, 59), (237, 206, 113), (237, 205, 92),
        (237, 199, 80), (237, 196, 64), (237, 193, 46), (62, 57, 51)
    ]
    shuffled_colors = colors[:]
    random.shuffle(shuffled_colors)
    offset = 10

    def __init__(self, position, mode, value=0):
        x = (position % mode.size) * mode.cell_size + Cell.offset
        y = (position // mode.size) * mode.cell_size + Cell.offset + 200
        width = mode.cell_size - Cell.offset * 2
        height = width
        self.value = value
        self.position = position
        self.has_merged = False
        super().__init__(x, y, width, height)

    def __repr__(self):
        return f"<cell {self.value}, {self.x}, {self.y}, {self.width}, {self.height}>"

    def draw_value(self, font_size):
        """Draws the value of the block"""
        value_text = Game.font.render(str(self.value), size=font_size)[0]
        value_position = value_text.get_rect(center=self.center)
        Game.game_surface.blit(value_text, value_position)


class Board():

    def __init__(self, mode):
        self.size = mode.size
        self.cell_size = mode.cell_size
        self.number_of_cells = self.size ** 2
        # creates empty board and adds 2 random blocks
        self.cells = [Cell(i, mode) for i in range(self.number_of_cells)]
        self.make_new_block(mode)
        self.make_new_block(mode)
        self.value_font = pygame.freetype.SysFont(None, mode.cell_size // 3)

    def move_blocks(self, x, positive, game):
        """Moves all blocks in the board"""
        # generates indexes of cell for each row/column
        for i in range(self.size):
            if x:
                indexes = list(range(i * self.size, (i + 1) * self.size))
            else:
                indexes = list(range(i, self.number_of_cells, self.size))
            if positive:
                indexes.reverse()

            for j in indexes:
                current_cell = self.cells[j]
                current_cell.has_merged = False
                neighbor = self.cells[indexes[indexes.index(j) - 1]]

                if current_cell.value > 0:
                    while current_cell is not self.cells[indexes[0]]:
                        # moves if neighbor is empty
                        if neighbor.value == 0:
                            neighbor.value = current_cell.value
                            neighbor.has_merged = current_cell.has_merged
                            current_cell.value = 0
                            j = indexes[indexes.index(j) - 1]
                            current_cell = self.cells[j]
                            neighbor = self.cells[indexes[indexes.index(j) - 1]]
                        # merges blocks
                        elif (
                                current_cell.value == neighbor.value and not
                                current_cell.has_merged and not neighbor.has_merged
                                ):
                            current_cell.value = game.mode.increase(current_cell.value)
                            game.score += game.mode.increase_score(current_cell.value)
                            neighbor.value = 0
                            current_cell.has_merged = True
                        else:
                            break

    def check_can_move(self):
        """Checks if the player can move"""
        if not self.check_full():
            return True

        # checks if adjacent cells are the same
        for i in range(self.size):
            row_indexes = list(range(i * self.size, i * self.size + self.size))
            column_indexes = list(range(i, self.number_of_cells, self.size))
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
        empty_blocks = [cell for cell in self.cells if cell.value == 0]
        empty_cell = random.choice(empty_blocks)
        if random.randint(0, 10) == 10:
            value = mode.values[1]
        else:
            value = mode.values[0]
        empty_cell.value = value

    def draw_board(self, game):
        """Draws the board"""
        pygame.draw.rect(game.game_surface, Game.board_color, (0, 200, 800, 800))
        for i in range(0, 900, self.cell_size):
            pygame.draw.line(game.game_surface, (188, 174, 161),
                             (i, 200), (i, 1000), Cell.offset * 2)
            pygame.draw.line(game.game_surface, (188, 174, 161),
                             (0, i + 200), (800, i + 200), Cell.offset * 2)

        for cell in self.cells:
            if cell.value > 0:
                if cell.value in game.mode.values[:12]:
                    color = game.mode.colors[game.mode.values.index(
                        cell.value)]
                else:
                    color = game.mode.colors[-1]
                pygame.draw.rect(game.game_surface, color, cell)
                cell.draw_value(game.mode.cell_size // 3)


class GameMode():

    def __init__(
        self, mode, start_value=2, increase_type="normal",
        size=4, win_value=None, values=None, colors=Cell.colors
            ):
        self.size = size
        self.number_of_cells = size ** 2
        self.cell_size = int(800 / size)
        self.increase_type = increase_type
        """
        with shelve.open(Game.score_file, writeback=True) as score_shelf:
            if mode not in score_shelf:
                score_shelf[mode] = 0
            self.high_score = score_shelf[mode]
        """
        self.high_score = 0
        if values:
            self.values = values
        else:
            self.values = [start_value]
            for i in range(12):
                self.values.append(self.increase(self.values[-1]))
        self.win_value = win_value if win_value else self.values[10]
        self.colors = colors

    def increase(self, value):
        """Increases cell value based on game mode"""
        if self.increase_type == "normal":
            next_value = value * 2
        elif self.increase_type == "plus one":
            next_value = value + 1
        elif self.increase_type == "random":
            next_value = self.values[self.values.index(value) + 1]

        return next_value

    def increase_score(self, value):
        if self.increase_type == "normal":
            points = value
        elif self.increase_type == "plus one":
            points = 2 ** value
        elif self.increase_type == "random":
            points = 2 ** (self.values.index(value) + 1)

        return points


class Menu():

    def __init__(self, menu_dimensions, button_list, x, y, width, height, offset, window_position):
        # setup the menu surface
        self.surface = pygame.Surface(menu_dimensions)
        self.surface.fill(Game.background_color)
        self.buttons = {}
        self.window_position = window_position
        # create each button
        for button in button_list:
            self.buttons[button] = pygame.Rect(x, y, width, height)
            y += height + offset
            pygame.draw.rect(self.surface, Game.board_color, self.buttons[button])
            text = Game.font.render(button)[0]
            position = text.get_rect(center=self.buttons[button].center)
            self.surface.blit(text, position)


class Game():
    score_file = "score"
    shuffled = [i for i in range(100)]
    random.shuffle(shuffled)
    modes = {
        "Normal": GameMode("Normal"),
        "65536": GameMode("65536", size=5, win_value=65536),
        str(2 ** 20): GameMode(str(2 ** 20), size=6, win_value=2 ** 20),
        "Eleven": GameMode("Eleven", 1, "plus one"),
        "Twenty": GameMode("Twenty", 1, "plus one", win_value=20),
        "Confusion": GameMode("Confusion", 1, "random", values=shuffled, colors=Cell.shuffled_colors)
    }
    buttons = ("Restart", "Menu", "Quit")
    background_color = (252, 247, 241)
    board_color = (205, 193, 181)
    dimensions = (800, 1000)

    window = pygame.display.set_mode(dimensions)
    transparent_surface = pygame.Surface([800, 800])
    transparent_surface.set_alpha(150)
    game_surface = pygame.Surface(dimensions)
    end_surface = pygame.Surface(dimensions)

    clock = pygame.time.Clock()
    font = pygame.freetype.SysFont(None, 50)

    def __init__(self):
        self.score = 0
        self.mode = self.modes["Normal"]
        self.state = "Menu"
        self.board = Board(self.mode)
        self.main_menu = Menu(self.dimensions, self.modes, 200, 150, 400, 100, 15, (0, 0))
        self.game_menu = Menu((300, 200 - Cell.offset), self.buttons, 0, 0, 200, 60, 5, (600, 0))
        self.font.render_to(self.main_menu.surface, (300, 50), "2048", size=100)
        self.draw_end()

    def draw_end(self):
        self.end_surface.fill(Game.background_color)
        end_text = ("Thanks for playing!", "Made by Chendi")
        y = 100
        for text in end_text:
            text = Game.font.render(text)[0]
            position = text.get_rect(center=(400, y))
            self.end_surface.blit(text, position)
            y += 100

    def update(self):
        """Draws based on current state"""
        wait = False
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
            position = text.get_rect(center=self.transparent_surface.get_rect().center)
            self.window.blit(text, position)
            self.window.blit(self.transparent_surface, (0, 200 - Cell.offset))
            wait = won
            if won:
                self.state = "Playing"

        elif self.state == "Restart":
            self.restart()

        elif self.state == "Quit":
            self.update_high_scores()
            self.window.blit(self.end_surface, (0, 0))
            wait = True

        elif self.state == "Testing":
            # only used for development/debugging
            # change the starting state of the game from Menu to Testing to trigger
            for cell in self.board.cells:
                cell.value = self.mode.win_value // 2
                # cell.value = random.randint(0, 1000000000)
                self.state = "Playing"

        pygame.display.flip()
        if wait:
            pygame.time.wait(750)

        self.clock.tick(20)

    def draw_game(self):
        """Draws board and scores"""
        self.game_surface.fill(self.background_color)
        self.board.draw_board(self)
        self.font.render_to(self.game_surface, (20, 20),
                            f"Score: {self.score}")
        self.font.render_to(self.game_surface, (20, 80),
                            f"High Score: {self.mode.high_score}")
        self.game_surface.blit(self.game_menu.surface, self.game_menu.window_position)
        self.window.blit(self.game_surface, (0, 0))

    def restart(self, mode=None):
        """Resets the game"""
        self.mode = mode if mode else self.mode
        self.score = 0
        self.state = "Playing"
        if self.mode == Game.modes["Confusion"]:
            self.setup_confusion()
        self.board = Board(self.mode)
        pygame.event.clear()

    def move(self, x, positive):
        """Moves all blocks"""
        if self.board.check_can_move():
            old_board_values = [cell.value for cell in self.board.cells]
            self.board.move_blocks(x, positive, self)

            # does not create new block if board is full or the board did not change
            if not self.board.check_full() and old_board_values != [cell.value for cell in self.board.cells]:
                self.board.make_new_block(self.mode)

        if self.score > self.mode.high_score:
            self.mode.high_score = self.score
        if not self.board.check_can_move():
            self.state = "Lost"
        if self.state != "Won":
            self.check_win()

    def check_win(self):
        for block in self.board.cells:
            if block.value == self.mode.win_value:
                self.state = "Won"

    def update_high_scores(self):
        pass
        """
        with shelve.open(self.score_file, writeback=True) as score_shelf:
            for mode in Game.modes:
                score_shelf[mode] = Game.modes[mode].high_score
        """

    def setup_confusion(self):
        random.shuffle(Cell.shuffled_colors)
        random.shuffle(self.shuffled)
        Game.modes["Confusion"].win_value = Game.modes["Confusion"].values[10]
