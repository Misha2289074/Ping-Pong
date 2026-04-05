from pygame import *

back = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

clock = time.Clock()
FPS = 60
game = True
finish = False

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, sizex, sizey):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (sizex, sizey))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 380:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys [K_DOWN] and self.rect.y < 380:
            self.rect.y += self.speed

wall_1 = Player('wall.png', 5, win_height - 300, 4, 20, 115)
wall_2 = Player('wall.png', 575, win_height - 300, 4, 20, 115)
ball = GameSprite('ball.jpg', 250, win_height - 300, 4, 65, 65)

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        window.fill(back)  
        wall_1.update_l()
        wall_2.update_r()
        ball.update()

    if ball.rect.y > win_height-50:
        or ball.rect.y < 0:
            speed.y *= -1


    wall_1.reset()
    wall_2.reset()
    ball.reset()
    display.update()
    clock.tick(FPS) 
