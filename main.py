import pygame
from pygame.locals import *

def main():
    # Setting up pygame and game settings like gravity
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Platformer")

    # Creating background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255,255,150))

    # drawing shapes
    rects = [pygame.draw.rect(background,(255,0,51),(550,500,200,20),border_radius=7)]
    character = pygame.draw.circle(background,(0,255,204),(400,300),15)

    # blitting everything to screen
    screen.blit(background,(0,0))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # listening for quit events
                return

        screen.blit(background,(0,0)) # blitting to screen every frame
        pygame.display.update(character)
        character = pygame.draw.circle(background, (0,255,204), (charatcer.x,character.y - 5, 15))

if __name__ == "__main__": main()