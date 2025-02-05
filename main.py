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

#start pygame
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()

#set up display
pygame.display.set_caption("Fortnite 2")
screen = pygame.display.set_mode((420, 340))
clock = pygame.time.Clock()
player = Player()
colour = (0, 128, 255)

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


    #draw screen
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, colour, player.rect)
    pygame.display.flip()

pygame.quit()
