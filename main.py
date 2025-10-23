import pygame
import random
import os

pygame.mixer.init()

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


# Background image
bgimg = pygame.image.load("images/snake.jpg")
bgimg = pygame.transform.scale(bgimg, (screen_width, scree_height)).convert_alpha()


window_img = pygame.image.load("images/window.jpg")
window_img = pygame.transform.scale(window_img, (screen_width, scree_height)).convert_alpha()


clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 50)


def text_screen(text, color , x, y):
    screen_text = font.render(text, True, color, )
    gameWindow.blit(screen_text, [x, y])


def plot_snake(gameWindow, color, snake_list, snake_size):
    for x, y in snake_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])


def welcome():
    exit_game = False
    green = (70, 255, 0)
    while not exit_game:
        gameWindow.fill((233, 220, 229))
        gameWindow.blit(window_img, (0, 0))

        text_screen("Welcome to snakes", green, 280, 100)
        text_screen("Press space to play the game", green, 230, 500)
        
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    my_sound = pygame.mixer.Sound('audio/nagin.mp3')
                    my_sound.set_volume(0.3)
                    my_sound.play()
                    GameLoop()

        pygame.display.update()
        clock.tick(60)

#game loop
def GameLoop():
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
    snake_list = []
    snake_length = 1
    if(not os.path.exists("highscore.txt")):
        with open("highscore.txt", "w") as f:
            f.write("0")
    with open("highscore.txt", "r") as f:
        highscore = f.read()

    while not exit_game:
        if game_over:
            with open("highscore.txt", "w") as f:
                f.write(str(highscore))

            gameWindow.fill(white)
            text_screen("Game over! Press enter to continue", red , 150, 250)
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    exit_game = True
                if event.type == pygame.KEYDOWN:  
                    if(event.key == pygame.K_RETURN):
                        welcome()
                    
        else:
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

                    if event.key == pygame.K_c:             #cheat code to increase score
                        score += 10
                        
            snake_x += velocity_x
            snake_y += velocity_y

            if(abs(snake_x - food_x)<6) and (abs(snake_y - food_y)<6):
                score += 10
                food_x = random.randint(20, int(screen_width)-50)
                food_y = random.randint(20, int(scree_height)-20)
                snake_length += 5
                if score>int(highscore):
                    highscore = score

            gameWindow.fill(white)
            gameWindow.blit(bgimg, (0, 0))
            text_screen("Score : " +str(score) + "   Highscore : " + str(highscore), blue, 20, 20)

            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
            
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list)>snake_length:
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over = True
                my_sound2 = pygame.mixer.Sound('audio/bomb.mp3')
                my_sound2.set_volume(0.3)
                my_sound2.play()

            if snake_x <0 or snake_x > screen_width or snake_y > scree_height or snake_y < 0:
                game_over = True
                my_sound2 = pygame.mixer.Sound('audio/bomb.mp3')
                my_sound2.set_volume(0.3)
                my_sound2.play()
                
            plot_snake(gameWindow, black, snake_list, snake_size)
            
        pygame.display.update()
        clock.tick(fps)

    pygame.quit() 
    quit()

welcome()