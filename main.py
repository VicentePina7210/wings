#the start of the wings project
import pygame
import os #this helps us find the path to our assets
from sprites import *
from config import *
from events import Collision, Projectile_collision

pygame.display.set_caption("Wings") #Sets the title for the open window

WHITE = (255, 255, 255) #RGB color code for white, used in line 18
FPS = 60 #Frames per second, used to control the speed of the game to ensure same speed across machine
    
#Create an instance of the ship class
player = Ship()
Asteroid_instance = Asteroid()

#Create sprite group and add the player sprite to it
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(Asteroid_instance)

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
        Collision(player, Asteroid_instance)
        Projectile_collision(player, Asteroid_instance)

        

    pygame.quit()


if __name__ == "__main__":
    main()