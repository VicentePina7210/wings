#the start of the wings project
import pygame
import os #this helps us find the path to our assets
from sprites import *
from config import *
from events import Collision#, Projectile_collision
import math

pygame.display.set_caption("Wings") #Sets the title for the open window

WHITE = (255, 255, 255) #RGB color code for white, used in line 18
FPS = 60 #Frames per second, used to control the speed of the game to ensure same speed across machine

#Create sprite group and add the player sprite to it
all_sprites = pygame.sprite.Group()
# all_sprites.add(player)
all_sprites.add(asteroid_instance)


background_width = background_image.get_width()

# def Projectile_collision(self, Asteroid):
#     # Check for collisions between projectiles and the target rectangle
#     for projectile in self.projectiles:
#         if projectile.rect.colliderect(Asteroid.rect):
#             projectile.kill()  # Remove the projectile if it collides
#             Asteroid.explosion_timer = pygame.time.get_ticks()  # Start explosion timer to limit duration of explosion
#             Asteroid.kill()  # Remove the asteroid immediately to remove the hitbox
#             pygame.sprite.Sprite.kill(Asteroid)
#             Asteroid.image = None

#             return True  # Collision detected
#     return False  # No collision detected
tiles = math.ceil(WIDTH / background_width) +1
print(tiles)
scroll = 0
#Draw onto screen
def draw_window():
    # WIN.fill(WHITE)
    #WIN.blit(PLAYER_SHIP, (100,300)) #loads our ship onto the screen. THE ODRER IN WHICH ITS LOADED MATTERS
    all_sprites.draw(WIN)
    # player.projectiles.draw(WIN) # testing code
    pygame.display.update()


    
    player_instance.draw(WIN)

missile_speed = 2


def main():
    global scroll
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # for i in range(0, tiles):
        #     WIN.blit(background_image,(i * background_width + scroll,0))
        # scroll -=1

        # if abs(scroll) > background_width:
        #     scroll = 0


        draw_window() #calls function from line 10
        # Collision(player, asteroid_instance)
        # Projectile_collision(player, asteroid_instance)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] :
            player_instance.y -= player_instance.speed
        if keys[pygame.K_s] :
            player_instance.y += player_instance.speed
        if keys[pygame.K_a] :
            player_instance.x -= player_instance.speed
        if keys[pygame.K_d] :
            player_instance.x += player_instance.speed
        if keys[pygame.K_SPACE]:
             player_instance.shoot()
             print("space")
        
        player_instance.move_missiles(missile_speed, asteroid_instance)
        asteroids.draw(WIN)
        asteroids.update()
        # player.draw(WIN)
        # player.update()
            
        pygame.display.flip()
        pygame.display.update()
        
    pygame.quit()


if __name__ == "__main__":
    main()