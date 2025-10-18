import pygame
pygame.init()

# colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)


# creating window
screen_width = 900
scree_height = 600
gameWindow = pygame.display.set_mode((screen_width, scree_height))

# title
pygame.display.set_caption("Snakes with Bhavi")

pygame.display.update()

# Game specific variables
exit_game = False
game_over = False


#game loop
while not exit_game:
    for event in pygame.event.get():
        print(event)
        if(event.type == pygame.QUIT):
            exit_game = True


    gameWindow.fill(white)
    pygame.display.update()

pygame.quit()
quit()