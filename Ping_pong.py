from pygame import*

w = 1600
h = 900

window = display.set_mode((w, h))
display.set_caption("Пинг-Понг")
background = transform.scale(image.load("pin-pong_fon.jpg"), (w, h))

clock = time.Clock()

game = True
finish = False

class GameSprite(sprite.Sprite):
    def __init__(self, player_imaige, player_x, player_y, player_speed, player_w, player_h):
        super().__init__()
        self.image = transform.scale(image.load(player_imaige), (player_w, player_h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):    #метод отрисовки спрайтов
        window.blit(self.image, (self.rect.x, self.rect.y))
    
class Player(GameSprite):
    def update1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y < 800:
            self.rect.y += self.speed
        if keys_pressed[K_s] and self.rect.y > 0:
            self.rect.y -= self.speed
    def update2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_d] and self.rect.y < 800:
            self.rect.y += self.speed
        if keys_pressed[K_a] and self.rect.y > 0:
            self.rect.y -= self.speed

class Ball(GameSprite):
    def __init__(self, player_imaige, player_x, player_y, player_speed, player_w, player_h):
        super().__init__(player_imaige, player_x, player_y, player_speed, player_w, player_h)
        self.speed_x = player_speed
        self.speed_y = player_speed
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y


player1 = Player("platform.png", 100, 350, 20, 30, 200)
player2 = Player("platform.png", 1470, 350, 20, 30, 200)

ball = Ball("ball.png", 750, 400, 20, 100, 100)

while game:
    window.blit(background, (0, 0))
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        player1.update1()
        player2.update2()
        ball.update()

        player1.reset()
        player2.reset()
        ball.reset()
    display.update()
    clock.tick(60)