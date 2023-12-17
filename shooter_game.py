#Создай собственный Шутер!

from pygame import *
from random import randint

display.set_caption("Shooter")
window = display.set_mode((1440, 720))
background = transform.scale(image.load('galaxy.jpg'), (1440, 720))

# СДЕЛАТЬ
# кол-во врагов увеличивалось 1 - Егор(if score % 20 = 0: новый монст +)
# создать бонус для стрельбы бешенной 2 - Aмирхан (random, добавить метод)
# создать дубликат корабля как бонус 3
# сердечки интерфейса жизней 4 - Кирилл (health = 3, png jpg, for) if health == 0: endgame =True
# дружеские кораблики по которым нельзя стрелять 5 - Лев (спрайты, группа, событие на столкновение)


# босс лвл сделать


lost = 0 # количество пропущенных врагов######################################3
score = 0 # счетчик убитых
value_hearts = 3 #кол-во хп игрока

#фоновая музыка
mixer.init()
mixer.music.load('space.mp3')
mixer.music.play()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        # самостоятельно
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x >5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x <1360:
            self.rect.x += self.speed

    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx+10, self.rect.top, 15, 20, 10)
        bullets.add(bullet)

    def fire_update(self):
        bullet = Bullet('bullet.png', self.rect.centerx-10, self.rect.top, 15, 20, 10)
        bullets.add(bullet)


class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost 
        global value_hearts
        if self.rect.y >= 800:
            lost += 1 
            value_hearts -= 1
            hearts.delete()
            self.rect.y = randint(-500, -50)
            self.rect.x = randint(100, 1200)

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()

ship = Player('rocket.png', 5, 620, 80, 100, 20)
ship_min1 = Player('rocket.png', 105, 620, 40, 50, 20)
ship_min2 = Player('rocket.png', -105, 620, 40, 50, 20)

monsters = sprite.Group()
bullets = sprite.Group()
hearts = sprite.Group()
heart = GameSprite('heart.png', 1370, 15, 50, 50, 0)

for i in range(7):
    monster = Enemy("ufo.png", randint(100, 1200), randint(-600, -100), 128, 65, 5)
    monsters.add(monster)


finish = False
game = True
clock = time.Clock()

fire_sound = mixer.Sound('fire.ogg')
font.init()
fint_universal = font.Font(None, 36)

# также необходимо создать поле текста отвечающее за убитых врагов
# текст который необходимо выводить "Врагов убито:" + переменная score
# отобразить данное поле текста под полем с количеством пропущенных врагов

strelyat_on = False
from random import randint

class Bonus(GameSprite):
    def update(self):
        self.rect.y += self.speed

bonus_x2 = Bonus('bonus.png', randint(100, 1200), randint(100, 200), 215, 225, 5)
check_bonus = False
stop_bonus = True



while game:
    chance_bonus = randint(0, 1)


    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                strelyat_on = True
        elif e.type == KEYUP:
            if e.key == K_SPACE:
                strelyat_on = False

                                            # сделать так, чтобы когда вы зажимаете пробел пули лети постоянно


    # СДЕЛАТЬ
    # кол-во врагов увеличивалось 1 - Егор (if score % 20 = 0: новый монст +)
    # создать бонус для стрельбы бешенной 2 - Aмирхан (random, добавить метод)
    # создать дубликат корабля как бонус 3
    # сердечки интерфейса жизней 4 - Кирилл (health = 3, png jpg, for) if health == 0: endgame =True
    # дружеские кораблики по которым нельзя стрелять 5 - Лев (спрайты, группа, событие на столкновение)
    
    # if chance_bonus == 1 and stop_bonus:
    #     bonus_x2.reset()
    #     bonus_x2.update()
    #     print('Created')
    #     stop_bonus = False

    # if sprite.collide_rect(ship, bonus_x2) or check_bonus :
    #     ship_min1.reset()
    #     ship_min2.reset()

    #     ship_min1.update()
    #     ship_min2.update()
    #     if strelyat_on:
    #         ship_min1.fire()
    #         ship_min2.fire()



    # столкновение пуль и врагов
    collides = sprite.groupcollide(monsters, bullets, True, True)
    for collide in collides:
        score += 1
        monster = Enemy("ufo.png", randint(100, 1200), randint(-600, -100), 128, 65, 5)
        monsters.add(monster)

    # столкновение игрока и врага
    if sprite.spritecollide(ship, monsters, False) or lost >= 5:
        finish = True
        # сообщение: ты проиграл
    
   
    if strelyat_on:
        ship.fire()

        

    window.blit(background,(0,0))

    text_lost_enemys = fint_universal.render('Пропущено: ' + str(lost), 1, (255,255,255))
    test_score_enemys = fint_universal.render('Врагов убито: ' + str(score), 1, (255,255,255))


    


    if not finish: # пока идет игра
        x=0
        for i in range(value_hearts):
            heart = GameSprite('heart.png', 1370-x, 15, 50, 50, 0)
            hearts.add(heart)
            x += 60
        hearts.draw(window)

        ship.reset()
        ship.update()

        
        monsters.draw(window)
        monsters.update()

        bullets.draw(window)
        bullets.update()

        window.blit(text_lost_enemys, (10,10))
        window.blit(test_score_enemys, (10,50))


        display.update()
    clock.tick(60)

