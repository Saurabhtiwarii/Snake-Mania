import pygame
import random
import os
pygame.init()
# for music
pygame.mixer.init()

# colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 128, 0)

screen_width = 900
screen_height = 600
game_window = pygame.display.set_mode((screen_width, screen_height))
#for backgound image
homeimg = pygame.image.load("home.jpg")
homeimage = pygame.transform.scale(homeimg,(screen_width,screen_height)).convert_alpha()
gameover = pygame.image.load("GameOver.jpg")
gameoverimg = pygame.transform.scale(gameover,(screen_width,screen_height)).convert_alpha()
snkpath = pygame.image.load("snakepath.jpg")
snkpathimg = pygame.transform.scale(snkpath,(screen_width,screen_height)).convert_alpha()
pygame.display.set_caption("SnakeMania")
pygame.display.update()

# game specific variables
game_over = False
game_exit = False
snake_x = 45
snake_y = 55
snake_size = 15
food_size = 10
clock = pygame.time.Clock()
fps = 50
velocity_x = 0
velocity_y = 0
init_velocity = 3
score = 0
food_x = random.randint(20,screen_width/1.5)
food_y = random.randint(20,screen_height/1.5)
font = pygame.font.SysFont(None,55)
highscore = ""

def score_dis(text,color,x,y):
    screen_text = font.render(text,True,color)
    game_window.blit(screen_text,[x,y])
def plot_snake(game_window,color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(game_window, color, [x, y, snake_size, snake_size])
def welcome():
    game_exit = False
    while not game_exit:
        game_window.blit(homeimage,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.load("home1.mp3")
                    pygame.mixer.music.play()
                    gameloop()
        pygame.display.update()
        clock.tick(fps)

def gameloop():
    
    game_over = False
    game_exit = False
    snake_x = 45
    snake_y = 55
    snake_size = 15
    food_size = 10
    clock = pygame.time.Clock()
    fps = 50
    velocity_x = 0
    velocity_y = 0
    init_velocity = 1
    score = 0
    food_x = random.randint(20, screen_width / 1.5)
    food_y = random.randint(20, screen_height / 1.5)
    snk_list = []
    snk_length = 1
    #check if high_score.txt is exist or not
    if not os.path.exists("high_score.txt"):
        with open("high_score.txt","w") as f:
            f.write("0")
    else:
        with open("high_score.txt", "r") as f:
            highscore = f.read()

# game loop
    while not game_exit:
        if game_over:
            with open("high_score.txt", "w") as f:
                f.write(str(highscore))
            game_window.blit(gameoverimg,(0,0))
            score_dis("Score: "+str(score),red,415,500)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                if event.type==pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x= -init_velocity
                        velocity_y =0
                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x= 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x=0
                    if event.key == pygame.K_q:
                        score += 100
                        if score>int(highscore):
                            highscore = score


            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y
            
            if abs(snake_x-food_x) < 10 and abs(snake_y-food_y) < 10:
                score = score+10

                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snk_length += 5
                if score>int(highscore):
                        highscore = score
            game_window.blit(snkpath,(0,0))
            score_dis("score :" + str(score)+" High Score: "+str(highscore), red, 5, 5)
            # pygame.draw.rect(game_window,black,[snake_x,snake_y,snake_size,snake_size])
            pygame.draw.rect(game_window, red, [food_x, food_y, food_size, food_size])
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)


            if len(snk_list)>snk_length:
                del snk_list[0]
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height or head in snk_list[:-1]:
                pygame.mixer.music.load("gameover.mp3")
                pygame.mixer.music.play()
                game_over = True
            plot_snake(game_window, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
welcome()
