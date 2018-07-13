import pygame


# 屏幕大小的常量
SCREEN_RECT = pygame.Rect(0,0, 480, 700)
# 刷新的帧率
FRAME_PER_SEC = 60
# 创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 英雄发射子弹事件的定时器常量
HERO_FIRE_EVENT = pygame.USEREVENT+1


class GameSprite(pygame.sprite.Sprite):

    def __init__(self, image_name, speed = 1):

        # 调用父类的初始化方法
        super().__init__()

        # 定义对象的属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):

        # 在屏幕的垂直方向上移动
        self.rect.y += self.speed