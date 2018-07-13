import pygame
import random

# 屏幕大小的常量
SCREEN_RECT = pygame.Rect(0,0, 480, 700)
# 刷新的帧率
FRAME_PER_SEC = 60
# 创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 英雄发射子弹事件的定时器常量
HERO_FIRE_EVENT = pygame.USEREVENT+1


