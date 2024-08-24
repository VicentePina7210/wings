import pygame
import os


# Load missile image
IMAGE_MISSILE_DEFAULT = pygame.image.load(os.path.join('assets', 'images', 'missile.png'))
MISSILE_DEFAULT = pygame.transform.scale(IMAGE_MISSILE_DEFAULT, (20, 20))
MISSILE_DEFAULT = pygame.transform.rotate(MISSILE_DEFAULT, -90)
IMAGE_ASTEROID = os.path.join('assets', 'images', 'asteroid.png')
IMAGE_EXPLOSION = pygame.image.load(os.path.join('assets', 'images', 'explosion.png'))
IMAGE_EXPLOSION = pygame.transform.scale(IMAGE_EXPLOSION, (75, 75))
SPACE_SHIP_WIDTH = 75
SPACE_SHIP_HEIGHT = 75

background_image = pygame.image.load(os.path.join('assets', 'images', 'background.png'))
background_image = pygame.transform.scale(background_image,(400,600))



# Establish height and width of game window
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255) #RGB color code for white, used in line 18
FPS = 60 #Frames per second, used to control the speed of the game to ensure same speed across machines