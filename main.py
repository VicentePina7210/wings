#the start of the wings project
import pygame
import os #this helps us find the path to our assets
from sprites import ship
from sprites import asteroid
from config import *


pygame.display.set_caption("Wings") #Sets the title for the open window

SPACE_SHIP_WIDTH = 75
SPACE_SHIP_HEIGHT = 75

WHITE = (255, 255, 255) #RGB color code for white, used in line 18
FPS = 60 #Frames per second, used to control the speed of the game to ensure same speed across machines

#assigning assests to variables
IMAGE_MISSILE_DEFAULT = pygame.image.load(os.path.join('assets', 'images', 'missile.png'))

MISSILE_DEFAULT = pygame.transform.scale(IMAGE_MISSILE_DEFAULT, (10, 10))
        
IMAGE_ASTEROID = os.path.join('assets', 'images', 'asteroid.png')

POSITION_ASTEROID = (600, 400)

HEIGHT_ASTEROID = 50
#Create an instance of the ship class
player = ship()

asteroid_instance = asteroid(IMAGE_ASTEROID, POSITION_ASTEROID, HEIGHT_ASTEROID)
#Create sprite group and add the player sprite to it
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(asteroid_instance)
#Create the player
IMAGE_PLAYER_SHIP = pygame.image.load(
    os.path.join('assets', 'images', 'ship.png'))#using this syntax and importing os, our assets can load on any OS b/c path directories may differ

PLAYER_SHIP = pygame.transform.rotate(pygame.transform.scale(
    IMAGE_PLAYER_SHIP, (SPACE_SHIP_WIDTH, SPACE_SHIP_HEIGHT)), 270) #rotates the image to the right and scales down



projectiles_tracker = []
#Creating methods

#Draw onto screen
def draw_window():
    WIN.fill(WHITE)
    #WIN.blit(PLAYER_SHIP, (100,300)) #loads our ship onto the screen. THE ODRER IN WHICH ITS LOADED MATTERS
    all_sprites.draw(WIN)
    player.projectiles.draw(WIN) # testing code


    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        all_sprites.update()
        draw_window()#calls function from line 10
        
        #move_ship()

        # shoot()
    pygame.quit()


if __name__ == "__main__":
    main()