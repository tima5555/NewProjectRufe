from pygame import *

mixer.init()

# Загрузка и воспроизведение музыки
mixer.music.load('sky-phonk-soundtrack-145571.mp3')
mixer.music.set_volume(0.1)
mixer.music.play(-1)# -1 означает, что музыка будет играть в бесконечном цикле

# Загрузка звуков учавствующих в игре
kill_sound = mixer.Sound('wilhelm_scream.mp3')
shoot_sound = mixer.Sound('cd876701a06be1f.mp3')
death_sound = mixer.Sound('69a8d818418e916.mp3')
victory_sound = mixer.Sound('952782968e924cf.mp3')



#constanta
ppurple = (128, 0, 128)
Silver = (192, 192, 192)
yyelow = (231, 235, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 51)
BlUE = (0, 0, 255)
ORANGE = (255, 123, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
LIGHT_GREEN = (200, 255, 200)
LIGHT_RED = (250, 128, 114)
BLACK = (0, 0, 0)
DARK_BLUE = (0, 0, 100)
LIGHT_BLUE = (80, 80, 255)



#Задний фон
window = display.set_mode((800, 600))
window.fill(Silver)


background = transform.scale(image.load('back fon.jpg'), (800, 600))
victory_image = transform.scale(image.load('Winner dsp.jpg'), (800, 600))
game_over_image = transform.scale(image.load('game_over.jpg'), (800, 600))

#Клас для стен
class GameSprite(sprite.Sprite):
    def __init__ (self, picture, w, h, x, y):
        super().__init__()
        self.image = transform.scale(image.load(picture), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
#Клас для персонажей
class player(GameSprite):
    def __init__(self, picture, w, h, x, y, speed_x, speed_y):
        super().__init__(picture, w, h, x, y)
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.prev_x = x
        self.prev_y = y

    def fire(self):
        shoot_sound.play()
        bullet = bullets('bullet1.png', 25, 25, self.rect.right, self.rect.centery, 3, 3)
        bulletss.add(bullet)

    def update(self):
        Key = key.get_pressed()
        self.prev_x = self.rect.x
        self.prev_y = self.rect.y

        if Key[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed_y
        if Key[K_DOWN] and self.rect.y < 550:
            self.rect.y += self.speed_y
        if Key[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed_x
        if Key[K_RIGHT] and self.rect.x < 720:
            self.rect.x += self.speed_x
        if Key[K_SPACE]:
            self.fire()

        # Проверка столкновений со стенами
        for wall in wallss:
            if sprite.collide_rect(self, wall):
                self.rect.x = self.prev_x
                self.rect.y = self.prev_y

    
class bullets(GameSprite):
    def __init__(self, picture, w, h, x, y, speed_x, speed_y):
        super().__init__(picture, w, h, x, y)
        self.speed_x = speed_x
        self.speed_y = speed_y
    def update(self):
        self.rect.x += self.speed_x
        sprite.groupcollide(bulletss, wallss, True, False)
        collisions = sprite.groupcollide(bulletss, policemann, True, False)
        for bullet, enemies in collisions.items():
            for enemy in enemies:
                kill_sound.play()
                enemy.kill()
        
        for bullet in bulletss:
            if bullet.rect.x > 800:
                bulletss.remove(bullet)
        sprite.groupcollide(bulletss, policemann, True, True)
        

class Enemy(GameSprite):
    def __init__(self, picture, w, h, x, y, speed_x, speed_y):
        super().__init__(picture, w, h, x, y)
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.direction = "left"
    def update(self):

        
        if self.rect.x < 200:
            self.direction = "right"
        if self.rect.x > 720:
            self.direction = "left"

        if self.direction == "left":
            self.rect.x -= self.speed_x
        if self.direction == "right":
            self.rect.x += self.speed_x
        
    
    def kill(self):
        self.rect.x = -100  # Переместим врага за пределы экрана
        self.rect.y = -100  # Переместим врага за пределы экрана
        policemann.remove(self)  # Удалим его из группы спрайтов


#Персонажи
policeman = Enemy('policeman.png', 120, 120, 340, 200, 6, 6)
exit_guy = GameSprite('exit guy.png', 80, 80, 700, 20,)
main_guy = player('main guy.png', 50, 50, 20, 300, 5, 5)


bulletss = sprite.Group()
wallss = sprite.Group()
policemann = sprite.Group()
policemann.add(policeman)

#стены
walls = [
    GameSprite('wall2.png', 80, 150, 150, 150),
    GameSprite('wall2.png', 80, 150, 150, 10),
    GameSprite('wall2.png', 80, 150, 400, 340),
    GameSprite('wall2.png', 80, 150, 400, 470)

    

]
for i in walls:
    wallss.add(i)

#Игровой цикл
Finish = False  # Изменено на False, чтобы начать игру в нормальном режиме
work = True
while work:
    for e in event.get():
        if e.type == QUIT:
            work = False

    if not Finish:  # Добавлено условие для проверки состояния игры
        window.fill(Silver)
        window.blit(background, (0, 0))
        wallss.draw(window)
        bulletss.draw(window)
        bulletss.update()
        main_guy.update()
        policemann.update()
        main_guy.draw()
        policemann.draw(window)
        exit_guy.draw()

        for wall in walls:
            if sprite.collide_rect(main_guy, wall):
                work = False
            if sprite.collide_rect(main_guy, exit_guy):
                victory_sound.play()
                Finish = True  # Изменение состояния игры при достижении победного спрайта
                break
            if sprite.spritecollideany(main_guy, policemann):
                death_sound.play()
                Finish = True  # Изменение состояния игры при столкновении с врагом
                window.blit(game_over_image, (0, 0))  # Отображение изображения проигрыша
                display.update()
                time.delay(1000)  # Задержка перед завершением игры
                work = False

        display.update()
    else:
        window.blit(victory_image, (0, 0))  # Отображение изображения победы
        display.update()

    time.delay(15)

    

