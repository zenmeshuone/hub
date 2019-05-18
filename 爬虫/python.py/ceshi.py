

import pygame
from pygame.locals import *
import math
import random


#初始化pygame,设置显示窗口
pygame.init()
width,height=640,480
screen =pygame.display.set_mode((width,height))
#keys用来记录按键情况，WASD（依次对应）
keys = [False,False,False,False]
#playerpos表示位置
playerpos = [100,100]
#跟踪玩家的精度变量，记录了射出的箭头数，和被击中数。
#之后我们会用到这些信息用来计算射击精确度
acc = []
#跟踪箭头变量
arrows = []
#定义一个定时器，使得游戏里经过一段时间就新建一直猹
badtimer = 100
badtimer1 = 0
badguys = [[640,100]]
healthvalue = 194
#播放声音初始化
pygame.mixer.init()

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
enemy = pygame.mixer.Sound("resources/audio/enemy.wav")
shoot = pygame.mixer.Sound("resources/audio/shoot.wav")
hit.set_volume(0.05)
enemy.set_volume(0.05)
shoot.set_volume(0.05)
#加载游戏的背景音乐并让音乐一直播放
#pygame.mixer.music.load('resources/audio/enemy.wav')
#pygame.mixer.music.play(-1,0.0)
#pygame.mixer.music.set_volume(0.25)


#不停的循环执行接下来的部分
#running变量会跟踪游戏是否结束
#exitcode变量会跟踪玩家是否胜利
running = True
exitcode = False
while running:
    # 在给屏幕画任何东西之前用黑色填充
    screen.fill(0)
    #添加的风景也在屏幕上
    for x in range(width//grass_img.get_width()+1):
        for y in range(height//grass_img.get_height()+1):
            screen.blit(grass_img,(x*100,y*100))
    screen.blit(castle_img,(0,30))
    screen.blit(castle_img, (0, 135))
    screen.blit(castle_img, (0, 240))
    screen.blit(castle_img, (0, 345))
    #获取鼠标和玩家的位置。然后，获取通过atan2函数得出的角度和弧度
    #当兔子被旋转的时候他的位置将会改变
    #计算兔子的新位置并将他在屏幕上显示出来
    position = pygame.mouse.get_pos()
    angle = math.atan2(position[1]-(playerpos[1]+32),position[0]-(playerpos[0]+26))
    playerrot = pygame.transform.rotate(rabbit_img,360-angle*57.29)
    playerpos1 = (playerpos[0]-playerrot.get_rect().width/2,playerpos[1]-playerrot.get_rect().height/2)
    screen.blit(playerrot,playerpos1)
    #在屏幕上画出箭头来，
    #vely和velx的值是根据三角定理算出来的
    #10是箭头的速度。if表达式是检查箭头是否超出了屏幕范围
    #如果超过，就删除这个箭头。
    #第二个for表达式是循环来把箭头根据相应的旋转画出来
    for bullet in arrows:
        index = 0
        velx = math.cos(bullet[0])*10
        vely = math.sin(bullet[0])*10
        bullet[1] += velx
        bullet[2] += vely
        if bullet[1]<-64 or bullet[1]>640 or bullet[2]<-64 or bullet[2]>480:
            arrows.pop(index)
        index += 1
        for projectile in arrows:
            arrow1 = pygame.transform.rotate(arrow_img,360-projectile[0]*57.26)
            screen.blit(arrow1),(projectile[1],projectile[2])
    #更新并显示这些坏蛋
    #检查badtimer是否为零，如果为零，创建一个新的猹然后重设badtimer
    #第一个循环是新猹的坐标，检查猹是否超出屏幕范围，如果超出将猹删掉
    #第二个循环式用来画出所有猹
    if badtimer == 0:
        badguys.append([640,random.randint(50,430)])
        badtimer = 100 -(badtimer1*2)
        if badtimer1 >=35:
            badtimer1 = 35
        else:
            badtimer1 += 5
    index_badguy = 0
    for badguy in badguys:
        if badguy[0] < -64:
            badguys.pop(index_badguy)
        badguy[0] -= 7
        #猹可以炸掉城堡
        #这段代码相当简单，如果猹的坐标小于64
        #就删除坏蛋并减少游戏里的健康值，减少的大小为5至20里的一个随机数
        #当猹冲过来的时候，并且在碰到城堡的时候消失
        badrect = pygame.Rect(badguy_img.get_rect())
        badrect.top = badguy[1]
        badrect.left = badguy[0]
        if badrect.left < 64:
            hit.play()
            healthvalue -= random.randint(5,20)
            badguys.pop(index_badguy)
        #循环所有的坏蛋和所有的箭头来检查是否有碰撞，
        #如果碰上删除猹，删除箭头，并在精确变量里加1
        #使用了pygame内建的功能来检验两个矩形是否交叉
        index_arrow = 0
        for bullet in arrows:
            bulletrect = pygame.Rect(arrow_img.get_rect())
            bulletrect.left = bullet[1]
            bulletrect.top = bullet[2]
            if badrect.colliderect(bulletrect):
                enemy.play()
                acc[0] += 1
                badguys.pop(index_badguy)
                arrows.pop(index_arrow)
            index_arrow += 1
        index_badguy += 1
    for badguy in badguys:
        screen.blit(badguy_img,badguy)
