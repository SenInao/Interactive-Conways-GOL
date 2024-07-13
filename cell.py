import pygame
from constants import *

class Cell:
    def __init__(self, x, y, isAlive) -> None:
        self.x = x
        self.y = y
        self.isAlive = isAlive

    def draw(self, display):
        if (self.isAlive):
            rect = pygame.rect.Rect(self.x * CELLWIDTH, self.y * CELLWIDTH, CELLWIDTH, CELLWIDTH)
            pygame.draw.rect(display, WHITE, rect)

    def checkCollision(self, x, y):
        if (self.x*CELLWIDTH <= x and self.x*CELLWIDTH+CELLWIDTH >= x and self.y*CELLWIDTH <= y and self.y*CELLWIDTH+CELLWIDTH >= y):
            return True
        return False

    def updateState(self, gameState):
        cells = gameState.cells
        aliveNeighbours = 0

        for y in range(self.y-1, self.y+2, 1):
            for x in range(self.x-1, self.x+2, 1):
                if (x == self.x and y == self.y):
                    continue

                if (y > CELLS-1):
                    y = 0
                if (x > CELLS-1):
                    x = 0

                if (cells[y][x].isAlive):
                    aliveNeighbours += 1

        if (self.isAlive):
            if aliveNeighbours < 2:
                return Cell(self.x, self.y, False)
            elif aliveNeighbours > 3:
                return Cell(self.x, self.y, False)
            else:
                return Cell(self.x, self.y, True)
        else:
            if aliveNeighbours == 3:
                return Cell(self.x, self.y, True)
            else:
                return Cell(self.x, self.y, False)
