import os
import random
import pygame

#start pygame
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()

#set up display
pygame.display.set_caption("Fortnite 2")
screen = pygame.display.set_mode((420, 340))

colour = (0, 128, 255)

#main loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #draw screen
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, colour, pygame.Rect(30, 30, 60, 60))
    pygame.display.flip()
pygame.quit()