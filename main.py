import os
import random
import pygame

#player
class Player(object):
    def __init__(self):
        self.rect = pygame.Rect(30, 30, 60, 60)

    def move(self, dx, dy):
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)

    def move_single_axis(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

class PlayerSprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("fortnite_char.png").convert_alpha()
        self.image.set_colorkey([255, 255, 255])

        self.rect = self.image.get_rect()

    def move(self, dx, dy):
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)

    def move_single_axis(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

class Wall(object):
    def __init__(self, wx, wy):
        walls.append(self)
        self.rect = pygame.Rect(wx, wy, 30, 30)

#start pygame
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()

#set up display
pygame.display.set_caption("Fortnite 2")
width = 620
height = 540
screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

walls = []

player = Player()
player_sprite = PlayerSprite()
colour = (0, 128, 255)

level = [
    "WWWWWWWWWWWWWWWWWWWW",
    "W                  W",
    "W               EE W",
    "W               EE W",
    "W                  W",
    


]

#main loop
running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_SPACE):
            if colour == (0, 128, 255):
                colour = (255, 100, 0)
            else:
                colour = (0, 128, 255)

    #allow player to move
    user_input = pygame.key.get_pressed()

    if user_input[pygame.K_UP]:
        player.move(0, -5)
    elif player.rect.y < (height - 60):
        player.move(0, 5)

    if user_input[pygame.K_DOWN]:
        player.move(0, 5)

    if user_input[pygame.K_LEFT]:
        player.move(-5, 0)
        if player.rect.x < 0:
            player.rect.x = width - 1

    if user_input[pygame.K_RIGHT]:
        player.move(5, 0)
        if player.rect.x > width:
            player.rect.x = -59

    #draw screen
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, colour, player.rect)

    all_sprites_list = pygame.sprite.Group()

    player_sprite.rect.x = 100
    player_sprite.rect.y = 100
    all_sprites_list.add(player_sprite)

    all_sprites_list.draw(screen)

    pygame.display.flip()

pygame.quit()
