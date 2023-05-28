from pygame import *
from random import randint

clock = time.Clock()
FPS = 120
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('PingPong')
background = transform.scale(image.load('Stol.jpg'),(700, 500))
speed = 13



font.init()
font = font.Font(None, 50)
lose1 = font.render('The First player - unskill', True, (200, 0, 0))
lose2 = font.render('The Second player - unskill', True, (200, 0, 0))

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

# points = 0
# lost = 0
# font.init()
# font1 = font.Font(None, 40)
# font2 = font.Font(None, 36)


class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > 500:
            self.rect.x = randint(1, 400)
            self.rect.y = 0
            lost = lost + 1


class Ball(GameSprite):
    def update(self):
        self.rect.y += self.speed
        

# bullets = sprite.Group()
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:                       
            self.rect.y-= self.speed
        if keys[K_s] and self.rect.y < 300:
            self.rect.y += self.speed
    def update_l(self):                                           
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 300:
            self.rect.y += self.speed    

 

win_width = 700
win_height = 500
display.set_caption("PingPong")
window = display.set_mode((win_width, win_height))
# background = transform.scale(image.load(img_back), (win_width, win_height))

# Raketka1 = Player(img=Raketka, 5, win_height - 100, 80, 100, 20)

# monsters = sprite.Group()
# for i in range (1, 5):
#     monster = Enemy('ufo.png', randint (50, 600), 0, 100, 50, randint(5, 5))
#     monsters.add(monster)
# asteroids = sprite.Group()
# for i in range (1, 1):
#     asteroid = Enemy('asteroid.png', randint (50, 600), 0, 100, 60, randint(7, 8))
#     asteroids.add(asteroid)

# font.init()
# font = font.SysFont('Arial', 70)
# win = font.render(
#     'Умничка', True, (0, 255, 0)

# )
# lose = font.render(
#     'Балбес', True, (255, 0, 0)
# )
# player = GameSprite('Raketka.png', 290, 400, 90, 90, 6)
raketka1 = Player("Raketka.png", 20, 100, 50, 300, 7)
raketka2 = Player("Raketka.png", 630, 100, 50, 300, 7)
ball = GameSprite("sharik.png", 300, 250, 50, 50, 13)



speed_x = 6
speed_y = 6


finish = False
game = True 
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background, (0, 0))
        raketka1.update_l()
        raketka2.update_r()
        raketka1.reset()
        raketka2.reset()
        ball.reset()
        ball.rect.x +=  speed_x
        ball.rect.y +=  speed_y
        if sprite.collide_rect(raketka1, ball) or sprite.collide_rect(raketka2, ball):
            speed_x *= -1
            speed_y *= -1
        if ball.rect.y > 500 or ball.rect.y < 0:
            speed *= -1
        if ball.rect.x <0:
            finish = True
            window.blit(lose1, (200, 200))
        if ball.rect.x >650:
            finish = True
            window.blit(lose2, (200, 200))
        if ball.rect.y > 450 or ball.rect.y < 0:
            speed_y *= -1

        
    
        # elif e.type == KEYDOWN:
#             if e.key == K_SPACE:
#                 # fire_sound.play()
#                 ship.fire()
            # if e.key  == K_r:
            #     if finish == True:
            #         finish = False

#                     for b in bullets:
#                         b.kill()

#                     for m in monsters:
#                         m.kill()
#                     lost = 0
#                     points = 0
#                     for i in range (5, 5):
#                         monster = Enemy('ufo.png', (50, 600), 0, 100, 50, randint(1, 5))
#                         monsters.add(monster)

#     if not finish:
#         window.blit(background,(0,0))
#         monsters.draw(window)
#         monsters.update()
#         bullets.update()
#         ship.update()
#         ship.reset() 
#         asteroids.update()
#         asteroids.draw(window)
#         bullets.draw(window)
#         unskill = font2.render('Пропущено:' + str(lost), 1, (255, 210, 210))
#         Shots = font1.render('Счёт:' + str(points), 1, (255, 250, 250))
#         window.blit(Shots, (10, 20))
#         window.blit(unskill, (10, 60))
#         collides = sprite.groupcollide(monsters, bullets, True, True)
#         ast = sprite.groupcollide(monsters, bullets, True, True)
#         for collide in collides:
#             points = points +1
#             monster = Enemy("ufo.png", randint(80, 600), 0, 100, 50, randint(1, 3))
#             monsters.add(monster)
#         if points >= 11:
#             window.blit(win, (100, 100))
#             finish = True
#         if lost >= 10:
#             window.blit(lose, (100, 100))
#             finish = True
    display.update()
    time.delay(50)
    clock.tick(FPS)