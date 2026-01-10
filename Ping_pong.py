from pygame import*

w = 1600
h = 900

p1 = 0
p2 = 0

window = display.set_mode((w, h))
display.set_caption("Пинг-Понг")
background = transform.scale(image.load("pin-pong_fon.jpg"), (w, h))

clock = time.Clock()

game = True
finish = False

font.init()
font1 = font.Font(None, 100)
font2 = font.Font(None, 170)

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
        if keys_pressed[K_s] and self.rect.y < 700:
            self.rect.y += self.speed
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
    def update2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_DOWN] and self.rect.y < 700:
            self.rect.y += self.speed
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed

class Ball(GameSprite):
    def __init__(self, player_imaige, player_x, player_y, player_speed, player_w, player_h):
        super().__init__(player_imaige, player_x, player_y, player_speed, player_w, player_h)
        self.speed_x = player_speed
        self.speed_y = player_speed
    def update(self):
        global p1, p2
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y >= 800 or self.rect.y <= 0:
            self.speed_y *= -1
        if sprite.collide_rect(player1, self) or sprite.collide_rect(player2, self):
            self.speed_x *= -1
        if self.rect.x <= 0:
            self.rect.x = 730
            self.rect.y = 400
            self.speed_x *= -1
            p2 += 1
        if self.rect.x >= 1500:
            self.rect.x = 730
            self.rect.y = 400
            self.speed_x *= -1
            p1 += 1

player1 = Player("platform.png", 100, 350, 20, 30, 200)
player2 = Player("platform.png", 1470, 350, 20, 30, 200)

ball = Ball("ball.png", 730, 400, 20, 100, 100)

while game:
    window.blit(background, (0, 0))
    text_score1 = font1.render("Пропущено: " + str(p1), 1, (255, 255, 255))
    window.blit(text_score1, (250, 10))
    text_score2 = font1.render("Пропущено: " + str(p2), 1, (255, 255, 255))
    window.blit(text_score2, (850, 10))
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

    if p1 >= 5:
        text_score2 = font2.render("Победа левого игрока" , 1, (255, 50, 50))
        window.blit(text_score2, (170, 390))
        finish = True

    if p2 >= 5:
        text_score2 = font2.render("Победа правого игрока" , 1, (255, 50, 50))
        window.blit(text_score2, (170, 390))
        finish = True

    display.update()
    clock.tick(60)