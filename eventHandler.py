import pygame
import sys

from utils import checkCollision

def handleEvents(gameState):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            gameState.mouseDown = True
            x, y = pygame.mouse.get_pos()
            cell = checkCollision(gameState, x, y)
            if (cell):
                gameState.shouldDraw = not cell.isAlive

        elif event.type == pygame.MOUSEBUTTONUP:
            gameState.mouseDown = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                gameState.paused = not gameState.paused
