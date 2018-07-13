import pygame
from game_sprites import GameSprite
from game_sprites import SCREEN_RECT


class Background(GameSprite):
    """游戏背景精灵"""

    def __init__(self, is_alt = False):

        super().__init__("./images/background.png")

        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):

        # 调用父类的方法实现
        super().update()

        # 判断是否移出屏幕
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height