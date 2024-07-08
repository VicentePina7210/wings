#the start of the wings project
import pygame

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wings") #Sets the title for the open window

WHITE = (255, 255, 255) #RGB color code for white, used in line 18

FPS = 60 #Frames per second, used to control the speed of the game to ensure same speed across machines

def draw_window():
    WIN.fill(WHITE)
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