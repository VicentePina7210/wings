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

#Create the player
IMAGE_PLAYER_SHIP = pygame.image.load(
    os.path.join('assets', 'images', 'ship.png'))#using this syntax and importing os, our assets can load on any OS b/c path directories may differ

PLAYER_SHIP = pygame.transform.rotate(pygame.transform.scale(
    IMAGE_PLAYER_SHIP, (SPACE_SHIP_WIDTH, SPACE_SHIP_HEIGHT)), 270) #rotates the image to the right and scales down

#assigning assests to variables
IMAGE_MISSILE_DEFAULT = pygame.image.load(os.path.join('assets', 'images', 'missile.png'))

MISSILE_DEFAULT = pygame.transform.scale(IMAGE_MISSILE_DEFAULT, (10, 10))
#Create sprite groups
# projectiles_group = pygame.sprite.Group()

#Creating classes
class projectiles(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = MISSILE_DEFAULT
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.y -= 5  # Move the projectile up
        if self.rect.bottom < 0:
            self.kill()  # Remove the projectile if it goes off-screen

    def draw(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def kill(self):
        # Placeholder for removing the projectile, could be removing it from a list or group
        pass

projectiles_tracker = []
#Creating methods

#Draw onto screen
def draw_window():
    WIN.fill(WHITE)
    WIN.blit(PLAYER_SHIP, (100,300)) #loads our ship onto the screen. THE ODRER IN WHICH ITS LOADED MATTERS

    pygame.display.update()

def move_ship(): #function to move the ship
    global projectiles
    X_SHIP = 100 #X coordinate of the ship
    Y_SHIP = 300
    run = True
    while run:
        WIN.fill(WHITE)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            Y_SHIP -= 1
        if keys[pygame.K_s]:
            Y_SHIP += 1
        if keys[pygame.K_a]:
            X_SHIP -= 1
        if keys[pygame.K_d]:
            X_SHIP += 1
        if keys[pygame.K_SPACE]:
            projectiles_tracker.append(projectiles(X_SHIP, Y_SHIP))

        for projectile in projectiles_tracker:
            projectile.update()
            projectile.draw(WIN)
        WIN.blit(PLAYER_SHIP, (X_SHIP, Y_SHIP))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()

# def shoot():
#     X_MISSILE = 100
#     Y_MISSILE = 300
#     SPEED_MISSILE_DEFAULT = 3
#     run = True
#     while run:
#         WIN.fill = WHITE
#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_SPACE]:
#             MISSILE_DEFAULT = projectiles(self.rect.centerx,self.rect.top )
#         WIN.blit(IMAGE_MISSILE_DEFAULT,(X_MISSILE, Y_MISSILE))
#         pygame.display.flip()
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run = False
#     pygame.QUIT



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
        move_ship()

        # shoot()
    pygame.quit()


if __name__ == "__main__":
    main()