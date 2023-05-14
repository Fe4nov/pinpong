from pygame import *

x_size = 700
y_size = 500
FPS = 60
speed_x = 5
speed_y = 5


window = display.set_mode((x_size, y_size))
display.set_caption('Пин понг')
background = transform.scale(image.load('+pin.jpg'), (700,500))

clock = time.Clock()
game = True
finish = False


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y ))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x =  player_x
        self.rect.y = player_y


    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):

    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < y_size - 80:
            self.rect.y += self.speed
    def update2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < y_size - 80:
            self.rect.y += self.speed

        
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > y_size:
            self.rect.x = get_rand_x(x_size)
            self.rect.y = 0
            lost += 1 





ball = GameSprite('pog.png', 150, 225, 50, 50, 10)
racket1 = Player('rak.png', 20, 225, 50, 150, 10)
racket2 = Player('rak.png', 620, 225, 50, 150, 10)

font.init()
font = font.Font(None, 35)
win1 = font.render('Player 1 Win!', True, (0, 180, 0))
win2 = font.render('Player 2 Win!', True, (0, 180, 0))






while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
        window.blit(background, (0, 0))
        racket1.update()
        racket2.update2()


        ball.rect.x += speed_x
        ball.rect.y += speed_y
    


        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= 1
        if ball.rect.y > y_size - 50 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x > x_size:
            finish = True
            window.blit(win1, (250, 250))
            game = True
        if ball.rect.x < 0:
            finish = True
            window.blit(win2, (250, 250))
            game = True
        racket1.reset()
        racket2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)