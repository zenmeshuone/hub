# -*- coding:utf-8 -*-
# 导入PyGame库
import pygame
from pygame.locals import *

# 初始化PyGame并设置显示窗口。
pygame.init()
width, height = 1800,1000
screen = pygame.display.set_mode((width, height))

# 加载你想要给bunny使用的图片
player = pygame.image.load("resources/images/castle.png")
#加载图片，
rabbit_img = pygame.image.load("resources/images/dude.png")
#加载风景
grass_img = pygame.image.load("resources/images/grass.png")
castle_img = pygame.image.load("resources/images/castle.png")
#加载箭头
arrow_img = pygame.image.load("resources/images/bullet.png")
#加载猹
badguy_img1 = pygame.image.load("resources/images/badguy.png")
badguy_img = badguy_img1
#加载城堡健康值图片
healthbar_img = pygame.image.load("resources/images/healthbar.png")
health_img = pygame.image.load("resources/images/health.png")
#加载胜利和失败时候的照片
gameover_img = pygame.image.load("resources/images/gameover.png")
youwin_img = pygame.image.load("resources/images/youwin.png")
#加载声音文件并配置音量
hit = pygame.mixer.Sound("resources/audio/explode.wav")
# 循环执行以下缩进的代码
while 1:

    # 在绘图前，将屏幕填充成黑色。
    screen.fill(0)
    # 将之前加载进来的bunny图片以100*100的位置显示在屏幕上。
    screen.blit(player, (100,100))

    screen.blit(rabbit_img, (100, 100))

    screen.blit(grass_img, (200, 100))
    screen.blit(castle_img, (300, 100))
    screen.blit(badguy_img1, (400, 100))
    screen.blit(healthbar_img, (500, 100))
    # 更新屏幕
    pygame.display.flip()
    # 检查任何新事件如果有的话，否则转到退出命令，退出程序。
    for event in pygame.event.get():
        # check if the event is the X button
        if event.type == pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)
