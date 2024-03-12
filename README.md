import pygame
from pygame.locals import *

pygame.init()

SCREENWIDTH, SCREENHEIGHT = 800, 600
PLAYER_SIZE = 50
GRAVITY = 0.3
JUMP_STRENGTH = 8
COLOR_WHITE = (255, 255, 255)
COLOR_BLUE = (0, 0, 255)

screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE))
        self.image.fill(COLOR_BLUE)
        self.rect = self.image.get_rect(center=(SCREENWIDTH/2, SCREENHEIGHT/2))
        self.vel_y = 0
        self.jumped = False

    def update(self):
        self.vel_y += GRAVITY
        self.rect.y += self.vel_y

        if self.rect.bottom > SCREENHEIGHT:
            self.rect.bottom = SCREENHEIGHT
            self.jumped = False

    def jump(self):
        if not self.jumped:
            self.vel_y -= JUMP_STRENGTH
            self.jumped = True

player = Player()
all_sprites = pygame.sprite.Group(player)

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                player.jump()

    all_sprites.update()

    screen.fill(COLOR_WHITE)
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
