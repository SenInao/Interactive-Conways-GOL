import pygame
import sys
from gameState import GameState

from utils import checkCollision, clearCells, generateRandomPattern

def handleEvents(gameState: GameState):
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

            elif event.key == pygame.K_ESCAPE:
                gameState.paused = True
                gameState.settingsOpen = not gameState.settingsOpen

            elif event.key == pygame.K_r:
                generateRandomPattern(gameState)

            elif event.key == pygame.K_c:
                clearCells(gameState)
