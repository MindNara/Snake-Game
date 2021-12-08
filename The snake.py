import pygame
import random
import sys
from pygame.locals import *

pygame.init()

yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)

dis_width = 1000
dis_height = 800

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("The Snake that's not a snake")

bg = pygame.image.load("background.png")
menu_bg = pygame.image.load("game menu bg.png")
credits_bg = pygame.image.load("credits bg.png")

clock = pygame.time.Clock()

snake_block = 20

font_style = pygame.font.SysFont("bahnschrift", 40)
score_font = pygame.font.SysFont("comicsansms", 35)

def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

def our_snake(snake_block, snake_list, colors):
    for x in snake_list:
        pygame.draw.rect(dis, colors, [x[0], x[1], snake_block, snake_block])
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 20, dis_height / 2.5])
 
 
def game():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1
    snake_speed = 15
    
    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.play(-1)
 
    foodx = round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, dis_height - snake_block) / 20.0) * 20.0
    
    num = 10
    colors = black
    random_colors = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    while not game_over:
        while game_close == True:
            dis.blit(bg, [0, 0]) 
            message("You Lost! Press C-Play Again or Q-Quit or M-Menu", red)
            your_score(Length_of_snake - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game()
                    if event.key == pygame.K_m:
                        pygame.mixer.music.stop ()
                        main_menu()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
 
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        dis.blit(bg, [0, 0])
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        
        if (Length_of_snake - 1) == num:
            colors = random_colors
 
        our_snake(snake_block, snake_List, colors)
        your_score(Length_of_snake - 1)
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, dis_height - snake_block) / 20.0) * 20.0
            Length_of_snake += 1
        
        if (Length_of_snake - 1) == num:
            colors = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            num += 10
            snake_speed += 1

        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 click = False
 
 def main_menu():
    while True:
        dis.blit(menu_bg, [0, 0])
        mx, my = pygame.mouse.get_pos()

        button_play = pygame.Rect(120, 296, 200, 50)
        button_credits = pygame.Rect(120, 371, 200, 50)
        button_exit = pygame.Rect(120, 446, 200, 50)

        if button_play.collidepoint((mx, my)):
            if click:
                game()
        if button_credits.collidepoint((mx, my)):
            if click:
                credits()
        if button_exit.collidepoint((mx, my)):
            if click:
                quit()

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(60)

def credits():
    running = True
    while running:
        dis.blit(credits_bg, [0, 0]) # bg credits

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        clock.tick(60)

main_menu()
