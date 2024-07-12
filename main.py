#the start of the wings project
import pygame
import os #this helps us find the path to our assets

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wings") #Sets the title for the open window

SPACE_SHIP_WIDTH = 75
SPACE_SHIP_HEIGHT = 75

WHITE = (255, 255, 255) #RGB color code for white, used in line 18
FPS = 60 #Frames per second, used to control the speed of the game to ensure same speed across machines

PLAYER_SHIP_IMAGE = pygame.image.load(
    os.path.join('assets', 'images', 'ship.png'))#using this syntax and importing os, our assets can load on any OS b/c path directories may differ

PLAYER_SHIP = pygame.transform.rotate(pygame.transform.scale(
    PLAYER_SHIP_IMAGE, (SPACE_SHIP_WIDTH, SPACE_SHIP_HEIGHT)), 270) #rotates the image to the right and scales down

def draw_window():
    WIN.fill(WHITE)
    WIN.blit(PLAYER_SHIP, (100,300)) #loads our ship onto the screen. THE ODRER IN WHICH ITS LOADED MATTERS
    pygame.display.update()

# Starting below this comment; This is the the main loop of the game. 
# It will run until the user closes the window, 
# the loops constantly checks if the widow is open
def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()#calls function from line 10
    pygame.quit()


if __name__ == "__main__":
    main()