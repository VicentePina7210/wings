import pygame
import os
from config import HEIGHT, WIDTH, MISSILE_DEFAULT

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
    
    def update(self):
        self.handle_keys()

class asteroid(pygame.sprite.Sprite):
    def __init__(self):
        #Call the parent class constructor
        pygame.sprite.Sprite.__init__(self)
        super().__init__() # call the constructor of the parent class to initialize sprite
        self.image = pygame.image.load(os.path.join('assets', 'images', 'asteroid.png')).convert_alpha() # holds the image of the sprite
        self.rect = self.image.get_rect #creates a rectangle around the image to represent the 'space' occupied (?)
        self.rect.center = (400, 300) # sets the initial position to the center of the screen
        self.speed = 2 # the speed of movement is 2, should be substantially slower than ship

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


