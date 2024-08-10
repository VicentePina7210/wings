import pygame
from sprites import *
from config import *

def Collision(Ship, Asteroid):
    if Ship.rect.colliderect(Asteroid.rect):
        Ship.image = IMAGE_EXPLOSION


def Projectile_collision(self, Asteroid):
        # Check for collisions between projectiles and the target rectangle
     for projectile in self.projectiles:
         if projectile.rect.colliderect(Asteroid.rect):
             projectile.kill()  # Remove the projectile if it collides
             Asteroid.image = IMAGE_EXPLOSION
             Asteroid.explosion_timer = pygame.time.get_ticks()  # Start explosion timer to limit duration of explosion
             return True  # Collision detected
     return False  # No collision detected
    



    # if Projectiles.missile.colliderect(Asteroid.rect):
    #     Asteroid.image = IMAGE_EXPLOSION
    #     Ship.projectiles.remove()


    
    
    
