import pygame
pygame.init()

def setup()
    w = pygame.display.set_mode([900,900])
    w.fill((255,255,255))
    black = (0,0,0)
    pygame.draw.line(w, black, (0, 300), (900, 300), 5)
    pygame.draw.line(w, black, (0, 600), (900, 600), 5)
    pygame.draw.line(w, black, (300, 0), (300, 900), 5)
    pygame.draw.line(w, black, (600, 0), (600, 900), 5)
    pygame.display.flip()
    player_win = False
    computer_win = False
    player_turn = True
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    valid = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    spot = 9

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



while not player_win and not computer_win:
    while spot not in valid:
        try:
            spot = int(input("Pick a square (0-8) "))
        except:
            continue
    valid.remove(spot)
    if player_turn:
        board[spot] = 1
        draw_x(spot)
    else:
        board[spot] = 2
        draw_o(spot)
    pygame.display.flip()
    if input("asfasfsf") == "q":
        player_win = True
    if valid = []:
        break
    player_turn = not player_turn
if player_win:
    print("You win!")
els
