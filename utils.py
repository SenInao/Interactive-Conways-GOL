from constants import CELLS
from cell import Cell

def createCells():
    cells = [[] for _ in range(CELLS)]
    for y in range(CELLS):
        for x in range(CELLS):
            cell = Cell(x, y, False)
            cells[y].append(cell)

    return cells

def checkCollision(gameState, x,y):
    for row in gameState.cells:
        for cell in row:
            if (cell.checkCollision(x,y)):
                return cell
