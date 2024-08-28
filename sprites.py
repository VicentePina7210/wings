import pygame
import os
from config import *
import time

class Projectiles(pygame.sprite.Sprite):
    def __init__(self, x, y, img):
        pygame.sprite.Sprite.__init__(self)
        super().__init__()
        self.rect.x = x
        self.rect.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self,window):
        window.blit(self.img, (self.x, self.y))

    def move(self, vel):
        self.y += vel

    def off_screen(self, height):
        return self.y <= height and self.y >=0
    
    def collision(self, obj):
        return collide(obj, self)
    

    def update(self):
        self.rect.x += 5  # Move the projectile up
        if self.rect.left > WIDTH:
            self.kill()  # Remove the projectile if it goes off-screen

def collide(obj1, obj2 ):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2,(offset_x, offset_y)) != None


class Ship(pygame.sprite.Sprite):
    def __init__(self):
        #Call the parent class constructor
        pygame.sprite.Sprite.__init__(self)
        super().__init__() # call the constructor of the parent class to initialize sprite
        self.image = pygame.image.load(os.path.join('assets', 'images', 'ship.png')).convert_alpha() # holds the image of the sprite
        self.image = pygame.transform.rotate(pygame.transform.scale(self.image, (75, 75)), 270)
        self.rect = self.image.get_rect() #creates a rectangle around the image to represent the 'space' occupied (?)
        self.rect.center = (400, 300) # sets the initial position to the center of the screen
        self.speed = 3 # the speed of movement so currently 3 pixels per update? may need to be fixed
        self.projectiles = []
        self.last_shot_time = 0 # track the time since last shot
        self.shoot_cooldown = .2
        


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
        missile = Projectiles(x, y, self.missile_img)
        self.projectiles.add(missile)
        
player_instance = Ship()
player = pygame.sprite.Group()
player.add(player_instance)

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, x, y):
        # Call the parent class constructor
        pygame.sprite.Sprite.__init__(self)
        super().__init__()  # call the constructor of the parent class to initialize sprite
        self.image = pygame.image.load(os.path.join('assets', 'images', 'asteroid.png')).convert_alpha()  # holds the image of the sprite
        self.image = pygame.transform.rotate(pygame.transform.scale(self.image, (75, 75)), 270)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.last_update = pygame.time.get_ticks()  # track the time since last shot
        self.update_delay = 0  # time between movements in milliseconds
        self.update_x = 0  # make these instance variables
        self.update_y = 0  # make these instance variables
        self.explosion_timer = None

    def update(self):
        now = pygame.time.get_ticks()
        if asteroid_instance.rect.colliderect(player_instance):
            self.kill()
        
        if now - self.last_update > self.update_delay:  
            self.rect.x += self.update_x
            self.rect.y += self.update_y
            self.last_update = now

        if self.rect.bottom >= 600:  # assuming screen height is 600
            self.update_y *= -1  # reverse direction to move up
        elif self.rect.top <= 0:
            self.update_y *= -1  # reverse direction to move down

        if self.rect.left <= 0:
            self.update_x = 1  # move right
        elif self.rect.right >= 800:  # assuming screen width is 800
            self.update_x = -1  # move left
            #move the self rect x and y into variables outside the update fuinction

asteroid_instance = Asteroid(800, 300)
asteroids = pygame.sprite.Group()
asteroids.add(asteroid_instance)







        
