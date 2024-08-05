import pygame
from sprites import *
from config import *

def Collision(Ship, Asteroid):
    if Ship.rect.colliderect(Asteroid.rect):
        Ship.image = IMAGE_EXPLOSION

    # if Projectiles.missile.colliderect(Asteroid.rect):
    #     Asteroid.image = IMAGE_EXPLOSION
    #     Ship.projectiles.remove()


    
    
    
