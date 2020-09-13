import pygame
import sys
from pygame.locals import *
import time
import random

def start_text_Display():
    screen = pygame.display.set_mode((1000,700))
    text_font = pygame.font.Font(None, 90)
    text = text_font.render("Welcome to", 1, (255,0,0))
    name_font = pygame.font.Font(None, 90)
    name = name_font.render("The Game of Snake", 1, (255,0,0))
    tip_font = pygame.font.Font(None,40)
    tip = tip_font.render("Press '0' to start.    Press 'ESC' to quit.", 1, (0,64,64,0))
    STARTFLAG = 1
    while STARTFLAG:
        for event in pygame.event.get():
            screen.fill(pygame.Color(0,0,0))
            screen.blit(text, (300, 250))
            screen.blit(name, (200, 350))
            screen.blit(tip, (250, 650))
            pygame.display.update()
            if event.type == KEYDOWN:
                if event.key == K_0:
                    STARTFLAG = 0
                if event.key == K_ESCAPE:
                    sys.exit()

def end_text_Display():
    screen = pygame.display.set_mode((1000,700))
    text_font = pygame.font.Font(None, 90)
    text = text_font.render("Game Over:)", 1, (255,0,0))
    name_font = pygame.font.Font(None, 40)
    name = name_font.render("Designed by SOHOYA", 1, (64,64,64,0))
    while True:
        for event in pygame.event.get():
            if event.type in (QUIT, KEYDOWN):
              sys.exit()
        screen.fill(pygame.Color(0,0,0))
        screen.blit(text, (300, 250))
        screen.blit(name, (600, 600))
        pygame.display.update()

def GameOver():
    end_text_Display()
    pygame.quit()
    sys.exit()

# 好戏开始了:)
start = True
while start:
    #初始化
    pygame.init()
    #蛇移动的速度，即控制每个循环多长时间运行一次，循环一次，蛇移动一单位(距离需要自己设置)
    snake_speed = pygame.time.Clock()
    #游戏界面
    screen = pygame.display.set_mode((1000,700))
    #给游戏起个名字
    pygame.display.set_caption("Snake_Game")
    snake_Position = [200,200]     #蛇的起始位置，即蛇头的位置
    snakeBody = [[100,100],[90,100],[80,100]]       #列表的嵌套，每一个子列表代表一节身子
    foodPosition = [500,350]      #初始时食物的位置
    flag = 1   ##标识食物是否被吃的标识符
    direction = 'down'
    changeDirection = direction
    start_text_Display()   ##游戏开始界面
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == QUIT:
                GameOver()
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    changeDirection = 'right'
                if event.key == K_LEFT:
                    changeDirection = 'left'
                if event.key == K_UP:
                    changeDirection = 'up'
                if event.key == K_DOWN:
                    changeDirection = 'down'
                    #Esc键
                if event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))
        #确定方向
        if changeDirection == 'left' and not direction == 'right':
            direction = changeDirection
        if changeDirection == 'right' and not direction == 'left':
            direction = changeDirection
        if changeDirection == 'up' and not direction == 'down':
            direction = changeDirection
        if changeDirection == 'down' and not direction == 'up':
            direction = changeDirection
        #移动蛇头坐标 snake_Position[0]和snake_Position[1]分别代表蛇头横坐标和纵坐标
        if direction == 'up':
            snake_Position[1] -= 10
        if direction == 'down':
            snake_Position[1] += 10
        if direction == 'right':
            snake_Position[0] += 10
        if direction == 'left':
            snake_Position[0] -= 10

        #每次循环先增加一个蛇头，在进行判断，不然的话蛇不会移动
        snakeBody.insert(0,list(snake_Position))
        #吃到了食物
        if snake_Position[0] == foodPosition[0] and snake_Position[1] == foodPosition[1]:
            flag = 0
        #没吃到食物，把增加的头砍掉0.0
        else:
            snakeBody.pop()
        # 随机位置产生一个食物
        if flag == 0:
            x = random.randrange(1,10)
            y = random.randrange(1,7)
            foodPosition = [int(x*100),int(y*100)]
            flag = 1

        screen.fill(pygame.Color(0,0,0))
        ##绘制蛇身和食物
        for body in snakeBody:
            pygame.draw.rect(screen, pygame.Color(255,255,255), Rect(body[0], body[1],10,10))
        pygame.draw.rect(screen, pygame.Color(255,0,255), Rect(foodPosition[0], foodPosition[1], 10, 10))
        pygame.display.update()
        #判断蛇头是否与身子相撞
        if len(snakeBody)>=5:
            for section in snakeBody[4:]:
                if snake_Position == section:
                    GameOver()
                else:
                    continue
        #判断蛇头是否与墙相撞
        if snake_Position[0] > 1000 or snake_Position[0] < 0:
            GameOver()
        elif snake_Position[1] > 700 or snake_Position[1] < 0:
            GameOver()

        #控制速度，tick(n)，n表示每秒主函数main()循环次数,每秒循环次数越多看起来越流畅,但是游戏难度更大
        snake_speed.tick(10)
