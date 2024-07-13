import pygame
from dataclasses import dataclass

@dataclass
class GameState:
    display: pygame.Surface
    cells: list
    shouldDraw: bool = False
    settingsOpen: bool = True
    paused: bool = True
    mouseDown: bool = False
