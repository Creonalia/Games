import pygame
import pygame.freetype
import random
pygame.init()


class Obstacle(pygame.sprite.Sprite):

    def __init__(self, x):
        super().__init__()
        self.image = pygame.Surface([50, 50])
        self.image.fill((200, 100, 100))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, random.choice((50, 100, 150, 200)))

    def update(self):
        if self.rect.right <= 0:
            self.rect.left = 1000
            self.rect.top = random.choice((50, 100, 150, 200))
        self.rect = self.rect.move(-5, 0)


class Game():
    window = pygame.display.set_mode([800, 300])
    clock = pygame.time.Clock()
    font = pygame.freetype.SysFont(None, 50)
    ground = pygame.Rect(0, 250, 800, 50)
    surface = pygame.Surface([800, 300])
    surface.set_alpha(100)
    text_surface = font.render("You lost")[0]
    surface.blit(text_surface, text_surface.get_rect(center=(400, 150)))

    def __init__(self):
        self.obstacles = pygame.sprite.Group()
        for i in range(1, 6):
            self.obstacles.add(Obstacle(i * 200))
        # create 2 players, one formal, one ducking
        self.normal_player = pygame.sprite.Sprite()
        self.normal_player.image = pygame.Surface([50, 100])
        self.normal_player.rect = self.normal_player.image.get_rect(topleft=(50, 150))
        self.ducking_player = pygame.sprite.Sprite()
        self.ducking_player.image = pygame.Surface([50, 50])
        self.ducking_player.rect = self.ducking_player.image.get_rect(topleft=(50, 200))
        self.player = pygame.sprite.GroupSingle(self.normal_player)
        self.state = "Not Playing"
        self.jumps = 15
        self.score = 0
        self.high_score = 0
        self.ticks = 0

    def update(self):
        self.ticks += 1
        if self.state == "Playing":
            if self.ticks % 30 == 0:
                self.score += 1
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP] or keys[pygame.K_w] and self.jumps:
                self.player.sprite.rect = self.player.sprite.rect.move(0, -20)
                self.jumps -= 1
            else:
                self.jumps = 0

            if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and self.player.sprite is self.normal_player:
                self.ducking_player.rect.bottomleft = self.normal_player.rect.bottomleft
                self.player.add(self.ducking_player)

            elif self.player.sprite is self.ducking_player and not (keys[pygame.K_DOWN] or keys[pygame.K_s]):
                self.normal_player.rect.bottomleft = self.ducking_player.rect.bottomleft
                self.player.add(self.normal_player)
            self.obstacles.update()

            # player collisions
            self.player.sprite.rect.top += 7
            if self.player.sprite.rect.top <= 0:
                self.player.sprite.rect.top = 0
            if pygame.sprite.groupcollide(self.player, self.obstacles, False, False):
                self.state = "Lost"
            if pygame.Rect.colliderect(self.player.sprite.rect, self.ground):
                self.player.sprite.rect.bottom = self.ground.top
                self.jumps = 15
        if self.score > self.high_score:
            self.high_score = self.score

    def draw(self):
        Game.window.fill((255, 255, 255))
        pygame.draw.rect(Game.window, (50, 10, 10), self.ground)
        self.font.render_to(Game.window, (10, 10), str(self.score))
        high_score_surface = self.font.render(str(self.high_score))[0]
        Game.window.blit(high_score_surface, high_score_surface.get_rect(topright=(790, 10)))
        self.player.draw(Game.window)
        self.obstacles.draw(Game.window)
        if self.state == "Lost":
            Game.window.blit(Game.surface, (0, 0))
        pygame.display.update()

    def reset(self):
        self.score = 0
        i = 200
        for sprite in self.obstacles:
            sprite.rect.topleft = (i, random.choice((50, 100, 150, 200)))
            i += 200
        self.player.sprite = self.normal_player
        self.player.sprite.rect.bottom = self.ground.bottom
