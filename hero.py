import pygame
from game_sprites import GameSprite
from game_sprites import SCREEN_RECT
from bullets import Bullet

class Hero(GameSprite):
    """英雄精灵"""

    def __init__(self):
        # 调用父类方法
        super().__init__("./images/hero.png", 0)

        # 设置英雄的初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

        # 创建子弹的精灵组
        self.bullets = pygame.sprite.Group()

    def update(self):

        # 英雄在水平方向移动
        self.rect.x += self.speed

        # 控制英雄不能离开屏幕
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > SCREEN_RECT.width:
            self.rect.right = SCREEN_RECT.width

    def fire(self):

        # 一次发射3枚子弹
        for i in (0, 1, 2):
            # 创建子弹精灵
            bullet = Bullet()

            # 设置精灵的位置
            bullet.rect.bottom = self.rect.y - i*20
            bullet.rect.centerx = self.rect.centerx

            # 将子弹精灵添加到子弹精灵组中
            self.bullets.add(bullet)