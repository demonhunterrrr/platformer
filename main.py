import pygame
from pygame.locals import *
from player import Player

def main():
    # Setting up pygame
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Platformer")

    # Creating background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255,255,150))

    # drawing shapes
    platforms = [pygame.draw.rect(background,(255,0,51),(550,500,200,20),border_radius=7),
        pygame.draw.rect(background,(255,0,51),(200,400,200,20),border_radius=7),
        pygame.draw.rect(background,(255,0,51),(25,200,200,20),border_radius=7),
        pygame.draw.rect(background,(255,0,51),(700,300,200,20),border_radius=7)
    ]  # list of platforms

    # creating player
    player = Player(400,300,background)

    # blitting everything to screen
    screen.blit(background,(0,0))
    pygame.display.update()

    # game loop
    while True:
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # listening for quit events
                return
        
        # listening for key presses
        keys = pygame.key.get_pressed()
        if keys[K_a]: player.coords = player.move(-5, 0)
        if keys[K_d]: player.coords = player.move(5, 0)
        if keys[K_w]: player.coords = player.move(0, -10)

        player.coords = player.move(0, 5    ) # gravity
        screen.blit(background, (0,0))
        pygame.display.update()

if __name__ == "__main__": main()


