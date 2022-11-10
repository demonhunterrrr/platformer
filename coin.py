import random 
import pygame
coin = random.randint(1,100)==x and random.randint(1,100)==y
if player(x,y) == coin(x,y)
    print(x+1)


coin.draw()
class Coin(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
 
        self.image = pygame.image.load("Coin.png")
        self.rect = self.image.get_rect()
 
        self.rect.topleft = pos