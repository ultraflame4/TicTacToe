#!venv/Scripts/python
import pygame
import sys
import gameEngine

pygame.init()
screen = gameEngine.interface.hud()
pygame.display.set_caption('Python Agario')
run = True

while run:
    pygame.time.delay(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
              run = False

    screen.update()
