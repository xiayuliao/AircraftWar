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
项目中使用了多个类,都是继承自pygame.sprite.Sprite精灵类。</br>
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
