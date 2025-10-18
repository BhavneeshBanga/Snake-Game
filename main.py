import pygame
import random

pygame.init()

# colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
blue = (0, 0, 255)

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
snake_x = 45
snake_y = 45
velocity_x = 0
velocity_y = 0
food_x = random.randint(20, int(screen_width)-50)
food_y = random.randint(20, int(scree_height)-20)
initial_velocity = 5
score = 0
snake_size = 10
fps = 30
clock = pygame.time.Clock()


font = pygame.font.SysFont(None, 50)

def text_screen(text, color , x, y):
    screen_text = font.render(text, True, color, )
    gameWindow.blit(screen_text, [x, y])

#game loop
while not exit_game:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            exit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x = initial_velocity
                velocity_y = 0
                
            if event.key == pygame.K_LEFT:
                velocity_x = -initial_velocity
                velocity_y = 0
                
            if event.key == pygame.K_UP:
                velocity_y = -initial_velocity
                velocity_x = 0
                
            if event.key == pygame.K_DOWN:
                velocity_y = initial_velocity
                velocity_x = 0
                
    snake_x += velocity_x
    snake_y += velocity_y

    if(abs(snake_x - food_x)<6) and (abs(snake_y - food_y)<6):
        score += 10
        print("Score : ", score)
        food_x = random.randint(20, int(screen_width)-50)
        food_y = random.randint(20, int(scree_height)-20)

    gameWindow.fill(white)
    text_screen("Score : " +str(score), blue, 20, 20)

    pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
    pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()