import pygame
import os

WIDTH, HEIGHT = 800, 600

# Load missile image
IMAGE_MISSILE_DEFAULT = pygame.image.load(os.path.join('assets', 'images', 'missile.png'))
MISSILE_DEFAULT = pygame.transform.scale(IMAGE_MISSILE_DEFAULT, (10, 10))