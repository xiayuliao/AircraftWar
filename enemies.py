import pygame
import random
from game_sprites import GameSprite
from game_sprites import SCREEN_RECT


class Enemy(GameSprite):
    """敌机精灵"""

    def __init__(self):

        # 调用父类方法，保持垂直方向的飞行
        super().__init__("./images/enemy.png")

        # 指定敌机的初始随机速度
        self.speed = random.randint(1, 3)

        # 指定敌机的初始随机位置
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):

        # 调用父类方法
        super().update()

        # 判断是否飞出屏幕
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()