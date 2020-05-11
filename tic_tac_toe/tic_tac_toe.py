"""tic tac toe clone"""
import pygame
import pygame.freetype
pygame.init()

# constants
WINDOW_DIMENSIONS = (600, 600)
WINDOW_X = WINDOW_DIMENSIONS[0]
CELL_DIMENSIONS = [dimension // 3 for dimension in WINDOW_DIMENSIONS]
CELL_X = CELL_DIMENSIONS[0]
BLACK = (0, 0, 0)
LINE_WIDTH = 5

font = pygame.freetype.SysFont(None, 100)

# windows and surfaces
window = pygame.display.set_mode(WINDOW_DIMENSIONS)
window.fill((255, 255, 255))
board_surface = pygame.Surface(WINDOW_DIMENSIONS)
board_surface.fill((255, 255, 255))
for i in range(CELL_X, WINDOW_X, CELL_X):
    pygame.draw.line(board_surface, BLACK, (0, i), (WINDOW_X, i), LINE_WIDTH)
    pygame.draw.line(board_surface, BLACK, (i, 0), (i, WINDOW_X), LINE_WIDTH)
window.blit(board_surface, (0, 0))

x_surface = pygame.Surface(CELL_DIMENSIONS)
x_rect = x_surface.get_rect()
x_surface.fill((255, 255, 255))
pygame.draw.line(x_surface, BLACK, x_rect.topleft, x_rect.bottomright, LINE_WIDTH)
pygame.draw.line(x_surface, BLACK, x_rect.topright, x_rect.bottomleft, LINE_WIDTH)
o_surface = pygame.Surface((CELL_DIMENSIONS))
o_surface.fill((255, 255, 255))
pygame.draw.circle(o_surface, BLACK, o_surface.get_rect().center, CELL_X // 2 - 2, LINE_WIDTH)

win_surface = pygame.Surface(WINDOW_DIMENSIONS)
win_surface.fill((255, 255, 255))

# game vars
board = [None for _ in range(9)]  # None is empty, True is X, False is O
x_turn = True


def position_to_cell(x, y):
    return (x // CELL_X) + (y // CELL_X * 3)


def cell_to_position(cell, offset=2):
    return (cell % 3) * CELL_X + offset, (cell // 3) * CELL_X + offset


pygame.display.flip()

# main game loop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            index = position_to_cell(*pygame.mouse.get_pos())
            if board[index] is None:
                board[index] = x_turn
                x_turn = not x_turn
                window.blit(
                    x_surface if board[index] else o_surface,
                    cell_to_position(index), (0, 0, 195, 195)
                )
                pygame.display.flip()

                # check for win
                winner = None
                rows = [board[i * 3:(i + 1) * 3] for i in range(3)]
                columns = [board[i::3] for i in range(3)]
                diagonals = [[board[i] for i in indexes] for indexes in ((0, 4, 8), (2, 4, 6)) ]
                for thing in rows + columns + diagonals:
                    if all([i == thing[0] for i in thing]) and None not in thing:  # all aresame so they won
                        winner = "X" if thing[0] else "O"

                if winner:
                    win_text = font.render(f"{winner} won")[0]
                    win_position = win_text.get_rect(center=window.get_rect().center)
                    win_surface.blit(win_text, win_position)
                    pygame.time.wait(200)
                    window.blit(win_surface, (0, 0))
                    pygame.display.flip()
                    pygame.time.wait(500)
                    running = False


