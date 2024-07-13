from constants import CELLS, WHITE
from cell import Cell
from gameState import GameState
import pygame
import random

def createCells():
    cells = [[] for _ in range(CELLS)]
    for y in range(CELLS):
        for x in range(CELLS):
            cell = Cell(x, y, False)
            cells[y].append(cell)

    return cells

def clearCells(gameState):
    for row in gameState.cells:
        for cell in row:
            cell.isAlive = False

def generateRandomPattern(gameState: GameState):
    for row in gameState.cells:
        for cell in row:
            alive = random.randint(0,1)
            if (alive):
                cell.isAlive = True
            else:
                cell.isAlive = False

def checkCollision(gameState: GameState, x,y):
    for row in gameState.cells:
        for cell in row:
            if (cell.checkCollision(x,y)):
                return cell

def set_text(string, coordx, coordy, fontSize):
    font = pygame.font.Font('freesansbold.ttf', fontSize) 
    text = font.render(string, True, WHITE) 
    textRect = text.get_rect()
    textRect.center = (coordx, coordy) 
    return (text, textRect)
