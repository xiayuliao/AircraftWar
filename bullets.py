import pygame
from game_sprites import GameSprite


class Bullet(GameSprite):
    """子弹精灵"""

    def __init__(self):
        # 调用父类方法,设置子弹图片，设置初始速度
        super().__init__("./images/bullet.png", -2)

    def update(self):

        # 调用父类方法，让子弹沿垂直方向飞行
        super().update()

        # 判断子弹是否飞出屏幕
        if self.rect.bottom < 0:
            self.kill()
