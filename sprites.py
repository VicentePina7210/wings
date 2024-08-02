import pygame
import os
from config import *
import time
import random

class ship(pygame.sprite.Sprite):
    def __init__(self):
        #Call the parent class constructor
        pygame.sprite.Sprite.__init__(self)
        super().__init__() # call the constructor of the parent class to initialize sprite
        self.image = pygame.image.load(os.path.join('assets', 'images', 'ship.png')).convert_alpha() # holds the image of the sprite
        self.image = pygame.transform.rotate(pygame.transform.scale(self.image, (75, 75)), 270)
        self.rect = self.image.get_rect() #creates a rectangle around the image to represent the 'space' occupied (?)
        self.rect.center = (400, 300) # sets the initial position to the center of the screen
        self.speed = 5 # the speed of movement so currently 5 pixels per update? may need to be fixed
        self.projectiles = pygame.sprite.Group()
        self.last_shot_time = 0 # track the time since last shot
        self.shoot_cooldown = 0.5


    def handle_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed
        if keys[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_d] and self.rect.right < WIDTH:
            self.rect.x += self.speed

        current_time = time.time()
        if keys[pygame.K_SPACE] and current_time - self.last_shot_time > self.shoot_cooldown:
            self.shoot()
            self.last_shot_time = current_time
    
    def update(self):
        self.handle_keys()
        self.projectiles.update()
   
    def shoot(self):
        missile = projectiles(self.rect.centerx, self.rect.top)
        self.projectiles.add(missile)

    class projectiles(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__()
            self.x = x
            self.y = y
            self.image = MISSILE_DEFAULT
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.speed = 4

        def update(self):
            self.rect.x += 4  # Move the projectile up
            if self.rect.bottom < 0:
                self.kill()  # Remove the projectile if it goes off-screen


class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        #Call the parent class constructor
        pygame.sprite.Sprite.__init__(self)
        super().__init__() # call the constructor of the parent class to initialize sprite
        self.image = pygame.image.load(os.path.join('assets', 'images', 'asteroid.png')).convert_alpha() # holds the image of the sprite
        self.image = pygame.transform.rotate(pygame.transform.scale(self.image, (75, 75)), 270)
        self.rect = self.image.get_rect() 
        self.rect.center = (600, 300) 
        self.speed = 1 
        self.last_update = pygame.time.get_ticks()  # track the time since last shot
        self.update_delay = 0 #time between movements in milliseconds
        collision = False
        update_y = 1

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.update_delay: #move to main function
            self.rect.x += 0
            self.rect.y += 3
            self.last_update = now
        # Check if the asteroid goes off of the screen
        if self.rect.bottom >= 600:  # assuming screen height is 600
            update_y = self.rect.y * -1  # reverse direction to move up
        elif self.rect.top <= 0:
            update_y = self.rect.y * -1
        
        if self.rect.x <= 0:
            self.direction_x = -1
        elif self.rect.x >= 800:
            self.direction_x = 1

            #move the self rect x and y into variables outside the update fuinction

    




class projectiles(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = MISSILE_DEFAULT
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x += 5  # Move the projectile up
        if self.rect.left > WIDTH:
            self.kill()  # Remove the projectile if it goes off-screen