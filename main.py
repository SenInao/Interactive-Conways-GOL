import pygame
from eventHandler import handleEvents
from utils import createCells, checkCollision, set_text
from constants import *
from gameState import GameState

def drawGrid(display):
    for x in range(1, CELLS, 1):
        pygame.draw.line(display, GRAY, (x*CELLWIDTH, 0), (x*CELLWIDTH, WIDTH), 1)

    for y in range(1, CELLS, 1):
        pygame.draw.line(display, GRAY, (0, y*CELLWIDTH), (WIDTH, y*CELLWIDTH), 1)

def drawCells(cells, display):
    for row in cells:
        for cell in row:
            cell.draw(display)

def drawSettings(display):
    rect = pygame.rect.Rect(WIDTH/4, WIDTH/4, WIDTH/2, WIDTH/2)
    pygame.draw.rect(display, GRAY, rect)
    text = set_text("Settings: ESC", WIDTH/2, WIDTH/3, FONTSIZE)
    display.blit(text[0], text[1])
    text = set_text("Pause/Play simulation: SPACE", WIDTH/2, WIDTH/3 + 2*FONTSIZE, FONTSIZE)
    display.blit(text[0], text[1])
    text = set_text("Generate random world: R", WIDTH/2, WIDTH/3 + 4*FONTSIZE, FONTSIZE)
    display.blit(text[0], text[1])
    text = set_text("Clear world: C", WIDTH/2, WIDTH/3 + 6*FONTSIZE, FONTSIZE)
    display.blit(text[0], text[1])

def drawGameState(gameState: GameState):
    gameState.display.fill(BLACK)

    if (gameState.settingsOpen):
        drawSettings(gameState.display)

    else:
        drawCells(gameState.cells, gameState.display)
        drawGrid(gameState.display)

def updateCells(gameState: GameState):
    newCells = [[] for _ in range(CELLS)]
    for y, row in enumerate(gameState.cells):
        for cell in row:
            updatedCell = cell.updateState(gameState)
            newCells[y].append(updatedCell)

    gameState.cells = newCells


def updateGameState(gameState: GameState):
    if (gameState.mouseDown):
        x,y = pygame.mouse.get_pos()
        cell = checkCollision(gameState, x, y)
        if (cell):
            cell.isAlive = gameState.shouldDraw

    if (not gameState.paused):
        updateCells(gameState)

def gameLoop(gameState: GameState):
    clock = pygame.time.Clock()

    while True:
        clock.tick(FPS)
        handleEvents(gameState)
        updateGameState(gameState)
        drawGameState(gameState)
        pygame.display.update()

def main():
    pygame.init()
    display = pygame.display.set_mode((WIDTH, WIDTH))
    cells = createCells()
    gameState = GameState(display, cells)
    gameLoop(gameState)

if __name__ == "__main__":
    main()
