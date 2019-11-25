import pygame
pygame.init()

def draw_board()
    w = pygame.display.set_mode([900,900])
    w.fill((255,255,255))
    black = (0,0,0)
    pygame.draw.line(w, black, (0, 300), (900, 300), 5)
    pygame.draw.line(w, black, (0, 600), (900, 600), 5)
    pygame.draw.line(w, black, (300, 0), (300, 900), 5)
    pygame.draw.line(w, black, (600, 0), (600, 900), 5)
    pygame.display.flip()

def draw_x(spot):
    x = spot % 3 * 300
    y = spot // 3 * 300
    pygame.draw.line(w, black, (x,y), (x + 300, y + 300), 7)
    x = spot % 3 * 300
    y = spot // 3 * 300 + 300
    pygame.draw.line(w, black, (x,y), (x + 300, y - 300), 7)  
    
def draw_o(spot):
    x = spot % 3 * 300 + 150
    y = spot // 3 * 300 + 150
    pygame.draw.circle(w, black, (x, y), 150, 5)

p1win = False
p2win = False
p1turn = True
board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
valid = [0, 1, 2, 3, 4, 5, 6, 7, 8]
spot = 9

while not p1win and not p2win:
    while spot not in valid:
        try:
            spot = int(input("Pick a square (0-8) "))
        except:
            continue
    valid.remove(spot)
    if p1turn:
        board[spot] = 1
        draw_x(spot)
    else:
        board[spot] = 2
        draw_o(spot)
    pygame.display.flip()
    if input("asfasfsf") == "q":
        p1win = True
    p1turn = not p1turn

 