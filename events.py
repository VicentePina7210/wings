import pygame
from sprites import *
from config import *

def Collision(Ship, Asteroid, Projectiles):
    if Ship.rect.colliderect(Asteroid.rect):
        Ship.image = IMAGE_EXPLOSION
    if Projectiles.rect.colliderect(Asteroid.rect):
        Asteroid.image = IMAGE_EXPLOSION
        print("Collision detected")



    # if Projectiles.missile.colliderect(Asteroid.rect):
    #     Asteroid.image = IMAGE_EXPLOSION
    #     Ship.projectiles.remove()


    
    
    
