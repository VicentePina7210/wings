#the start of the wings project
import pygame
import os #this helps us find the path to our assets
from sprites import *
from config import *
import math
import time
import random



class Projectiles(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        super().__init__()
        self.image = MISSILE_DEFAULT
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self ):
        self.rect.x += 5  # Move the projectile up
        if self.rect.left > WIDTH:
            self.kill()  # Remove the projectile if it goes off-screen

class Ship(pygame.sprite.Sprite):
    def __init__(self):
        #Call the parent class constructor
        pygame.sprite.Sprite.__init__(self)
        super().__init__() # call the constructor of the parent class to initialize sprite
        self.image = pygame.image.load(os.path.join('assets', 'images', 'ship.png')).convert_alpha() # holds the image of the sprite
        self.image = pygame.transform.rotate(pygame.transform.scale(self.image, (75, 75)), 270)
        self.rect = self.image.get_rect() #creates a rectangle around the image to represent the 'space' occupied (?)
        self.rect.center = (400, 300) # sets the initial position to the center of the screen
        self.speed = 5 # the speed of movement so currently 3 pixels per update? may need to be fixed
        self.projectiles = pygame.sprite.Group()
        self.last_shot_time = 0 # track the time since last shot
        self.shoot_cooldown = 0.2
        


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
        missile = Projectiles(self.rect.centerx, self.rect.top)
        self.projectiles.add(missile)
        

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, x_random):
        # Call the parent class constructor
        pygame.sprite.Sprite.__init__(self)
        super().__init__()  # call the constructor of the parent class to initialize sprite
        self.image = pygame.image.load(os.path.join('assets', 'images', 'asteroid.png')).convert_alpha()  # holds the image of the sprite
        self.image = pygame.transform.rotate(pygame.transform.scale(self.image, (75, 75)), 270)
        self.rect = self.image.get_rect()
        self.rect.center = (800,x_random)
        self.last_update = pygame.time.get_ticks()  # track the time since last shot
        self.update_delay = 0  # time between movements in milliseconds
        self.update_x = 0  # make these instance variables
        self.update_y = 0  # make these instance variables
        self.explosion_timer = 0
        self.health = 3

    def check_collision(self, other):
        hits = pygame.sprite.spritecollide(self, other, True)  # True removes projectile on collision
        if hits:
            print("Asteroid hit!")
            self.health -= 1
        if self.health == 1:
            self.image = IMAGE_ASTEROID_CRITICAL
        if self.health <= 0:
            self.kill()  # Remove asteroid if hit

    def update(self):
        now = pygame.time.get_ticks()
        if self.explosion_timer:
            # If explosion timer is set, check if 500ms have passed
            if pygame.time.get_ticks() - self.explosion_timer >= 500:
                self.kill()  # Remove the asteroid after 500ms
        
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




pygame.display.set_caption("Wings") #Sets the title for the open window

WHITE = (255, 255, 255) #RGB color code for white, used in line 18
FPS = 60 #Frames per second, used to control the speed of the game to ensure same speed across machine
    
#Create an instance of the ship class
player = Ship()

#Create sprite group and add the player sprite to it
all_sprites = pygame.sprite.Group()
all_sprites.add(player)


asteroid_group = pygame.sprite.Group()

background_width = background_image.get_width()

tiles = math.ceil(WIDTH / background_width) +1
print(tiles)
scroll = 0
# Here we create the instance of the asteroid 
def draw_asteroids():
    if len(asteroid_group) < 1:
        x_random = random.randint(50, 550)
        asteroid = Asteroid(x_random)
        asteroid_group.add(asteroid)
        all_sprites.add(asteroid)
        


#Draw onto screen
def draw_window():
    # WIN.fill(WHITE)
    #WIN.blit(PLAYER_SHIP, (100,300)) #loads our ship onto the screen. THE ODRER IN WHICH ITS LOADED MATTERS
    all_sprites.draw(WIN)
    player.projectiles.draw(WIN) # testing code
    asteroid_group.draw(WIN)  # Draw the asteroids

    pygame.display.update()

def main():
    global scroll
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for i in range(0, tiles):
            WIN.blit(background_image,(i * background_width + scroll,0))
        scroll -=1

        if abs(scroll) > background_width:
            scroll = 0

        



        for asteroid in asteroid_group:
            asteroid.check_collision(player.projectiles)  # Check for collisions with projectiles

        asteroid_group.update()
        all_sprites.update()
        
        draw_asteroids()
        
        draw_window()#calls function from line 10
        pygame.display.update()
        pygame.display.flip()
        
        

    pygame.quit()


if __name__ == "__main__":
    main()