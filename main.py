import pygame
from eventHandler import handleEvents
from dataclasses import dataclass
from utils import createCells, checkCollision
from constants import *

@dataclass
class GameState:
    display: pygame.Surface
    cells: list
    shouldDraw: bool = False
    paused: bool = True
    mouseDown: bool = False

def drawGrid(display):
    for x in range(1, CELLS, 1):
        pygame.draw.line(display, GRAY, (x*CELLWIDTH, 0), (x*CELLWIDTH, WIDTH), 1)

    for y in range(1, CELLS, 1):
        pygame.draw.line(display, GRAY, (0, y*CELLWIDTH), (WIDTH, y*CELLWIDTH), 1)

def drawCells(cells, display):
    for row in cells:
        for cell in row:
            cell.draw(display)

def drawGameState(gameState):
    gameState.display.fill(BLACK)
    drawCells(gameState.cells, gameState.display)
    drawGrid(gameState.display)

def updateCells(gameState):
    newCells = [[] for _ in range(CELLS)]
    for y, row in enumerate(gameState.cells):
        for cell in row:
            updatedCell = cell.updateState(gameState)
            newCells[y].append(updatedCell)

    gameState.cells = newCells


def updateGameState(gameState):
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
