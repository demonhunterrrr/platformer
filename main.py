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
    player = Player(400,585,background)

    # blitting everything to screen
    screen.blit(background,(0,0))
    pygame.display.update()

    # game loop
    on_ground = True
    jumping = False
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # listening for quit events
                return
        
        starting_coords = player.coords

        # listening for key presses
        keys = pygame.key.get_pressed()
        if keys[K_a]: player.coords = player.move(-5, 0)
        if keys[K_d]: player.coords = player.move(5, 0)
        if keys[K_w] and on_ground:
            jumping = True

        if jumping:
            player.coords = player.jump()

        on_ground = starting_coords[1] == player.coords[1] and abs(player.jump_vel) > 1

        if on_ground:
            jumping = False
            player.jump_vel = 15

        screen.blit(background, (0,0))
        pygame.display.update()

if __name__ == "__main__": main()


