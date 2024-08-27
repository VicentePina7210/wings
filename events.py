import pygame
from sprites import *
from config import *
isalive = True

def Collision(Ship, Asteroid):
    if Ship.rect.colliderect(Asteroid.rect) and not isalive:
        Ship.image = IMAGE_EXPLOSION
        print("broken")

def Projectile_collision(self, Asteroid):
        # Check for collisions between projectiles and the target rectangle
     for projectile in self.projectiles:
         if projectile.rect.colliderect(Asteroid.rect):
             projectile.kill()  # Remove the projectile if it collides
             Asteroid.kill()
             isalive = False
             Asteroid.image = IMAGE_EXPLOSION
             Asteroid.explosion_timer = pygame.time.get_ticks()  # Start explosion timer to limit duration of explosion
             return isalive
    



    # if Projectiles.missile.colliderect(Asteroid.rect):
    #     Asteroid.image = IMAGE_EXPLOSION
    #     Ship.projectiles.remove()


    
    
    
