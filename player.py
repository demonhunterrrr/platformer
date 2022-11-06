import pygame
from pygame.locals import * 

class Player:
    def __init__(self, x: int, y: int, surf: pygame.Surface):
        self.coords = (x, y)
        self.surf = surf # surf is short for surface
        self.rect = pygame.draw.circle(self.surf, (0,255,204), self.coords, 15)
    
    def move(self, x: int, y: int) -> tuple:
        if self.coords[0] + x not in range(15,786) or self.coords[1] + y not in range(15,586): # checking if the player's coords are outside of the window. We subtract 15 from the window sizes because the circle has a radius of 15
            return (self.coords[0], self.coords[1])
        self.surf.fill((255,255,150), rect=self.rect)
        self.rect = pygame.draw.circle(self.surf, (0,255,204), (self.coords[0] + x, self.coords[1] + y), 15)
        return (self.coords[0] + x, self.coords[1] + y)