python final_exam：AircraftWar
====
运行方式
----
环境：pygame 1.9.3</br>
python 3.6.4</br>
入口：plane_main.py</br>
此项目利用images里的资源，实现一个简易的飞机大战版本</br>

项目类设计
----
主程序设计了游戏类PlaneGame,有两个方法初始化__init__(self)和启动开始start_game(self)


class PlaneGame():
    """飞机大战主游戏"""   
    def __init__(self):
        pass
    def start_game(self):
        pass
        
初始化方法：
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
        
  两个定时器，1000微秒的定时器是敌机出现间隔时间1s
  500微秒的定时器是我方英雄发射子弹间隔0.5
        
  启动游戏方法
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
            # 更新显示
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


游戏对象的类都是继承自pygame.sprite.Sprite精灵类。</br>
最基本的是游戏精灵类，定义在代码文件game_sprites.py中


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
        

背景类、敌机类、我方英雄类、子弹类都是继承自GameSprite类


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
  注意:子弹精灵构成精灵组是在我方英雄hero精灵的射击方法fire中添加的
 
 
  效果图</br>
  ![images](https://github.com/xiayuliao/AircraftWar/blob/master/images/effect.png)
