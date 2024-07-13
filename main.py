import pygame
import sys

FPS = 30
WIDTH = 600
CELLS = 10
CELLWIDTH = WIDTH/CELLS
CELLOFFSET = 0.1

WHITE = (255, 255, 255)

class Cell:
    def __init__(self, x, y, isAlive) -> None:
        self.x = x
        self.y = y
        self.isAlive = isAlive

    def draw(self, display):
        rect = pygame.rect.Rect(self.x * CELLWIDTH + CELLWIDTH*CELLOFFSET, self.y * CELLWIDTH + CELLWIDTH*CELLOFFSET, CELLWIDTH * (1 - CELLOFFSET*2), CELLWIDTH * (1 - CELLOFFSET*2))
        pygame.draw.rect(display, WHITE, rect)

def createCells():
    cells = [[] for _ in range(CELLS)]
    for y in range(CELLS):
        for x in range(CELLS):
            cell = Cell(x, y, True)
            cells[y].append(cell)

    return cells

def drawGrid(display):
    for x in range(1, CELLS, 1):
        pygame.draw.line(display, WHITE, (x*CELLWIDTH, 0), (x*CELLWIDTH, WIDTH), 1)

    for y in range(1, CELLS, 1):
        pygame.draw.line(display, WHITE, (0, y*CELLWIDTH), (WIDTH, y*CELLWIDTH), 1)

def drawCells(cells, display):
    for row in cells:
        for cell in row:
            cell.draw(display)

def gameLoop(display):
    clock = pygame.time.Clock()
    cells = createCells()
    drawGrid(display)
    drawCells(cells, display)

    while True:
        clock.tick(FPS)
  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

def main():
    pygame.init()
    display = pygame.display.set_mode((WIDTH, WIDTH))
    gameLoop(display)

if __name__ == "__main__":
    main()
