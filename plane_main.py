import pygame
from game_sprites import *
from background import Background
from enemies import Enemy
from hero import Hero
from bullets import Bullet


class PlaneGame():
    """飞机大战主游戏"""

    def __init__(self):

        # 创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 创建游戏的时钟
        self.clock = pygame.time.Clock()
        # 调用私有方法，精灵和精灵组的创建
        self.__create_sprites()
        # 击中飞机数量
        self.score = 0
        # 设置定时器事件
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)


    def __create_sprites(self):

        # 创建背景精灵和精灵组
        bg1 = Background(False)
        bg2 = Background(True)
        self.back_group = pygame.sprite.Group(bg1, bg2)
        # 创建敌机的精灵组
        self.enemy_group = pygame.sprite.Group()
        # 创建英雄精灵和精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):

        while True:
            # 设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            # 事件监听
            self.__event_handler()
            # 碰撞检测
            self.__check_collide()
            # 更新/绘制精灵组
            self.__update_sprites()
            #更新显示
            pygame.display.update()

    def __event_handler(self):

        for event in pygame.event.get():

            #判断是否退出游戏
            if event.type == pygame.QUIT:
                self.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                # 创建敌机精灵
                enemy = Enemy()
                # 将敌机精灵添加到敌机精灵组
                self.enemy_group.add(enemy)

            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()

            # 使用键盘提供的方法获取键盘按键-按键元组
            keys_pressed = pygame.key.get_pressed()
            # 判断元组中对应的按键索引值
            if keys_pressed[pygame.K_RIGHT]:
                self.hero.speed = 2
            elif keys_pressed[pygame.K_LEFT]:
                self.hero.speed = -2
            else:
                self.hero.speed = 0

    def __check_collide(self):

        # 子弹销毁敌机
        enemies = pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)

        # 判断击中敌机个数
        self.score += len(enemies)

        # 敌机撞毁英雄
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)

        # 判断列表是否有内容
        if len(enemies) > 0:
            # 英雄牺牲
                self.hero.kill()
            # 结束游戏
                self.__game_over()

    def __update_sprites(self):

        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    def __game_over(self):
        print("游戏结束，击毁敌机数量为%d"%self.score)
        pygame.quit()
        exit()


if __name__ == '__main__':
    # c创建游戏对象
    game = PlaneGame()
    # 启动游戏
    game.start_game()
