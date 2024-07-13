import pygame
import sys

FPS = 30
WIDTH = 600
CELLS = 20

WHITE = (255, 255, 255)

def drawGrid(display):
    for x in range(CELLS):
        pygame.draw.line(display, WHITE, (x*(WIDTH*CELLS+(WIDTH-1))/(CELLS**2), 0), (x*(WIDTH*CELLS+(WIDTH-1))/(CELLS ** 2), WIDTH), 1)

    for y in range(CELLS):
        pygame.draw.line(display, WHITE, (0, y*(WIDTH*CELLS+(WIDTH-1))/(CELLS**2)), (WIDTH, y*(WIDTH*CELLS+(WIDTH-1))/(CELLS ** 2)), 1)

def gameLoop(display):
    clock = pygame.time.Clock()
    drawGrid(display)

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
