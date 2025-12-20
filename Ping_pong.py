from pygame import*

w = 1600
h = 900

window = display.set_mode((w, h))
display.set_caption("Пинг-Понг")
background = transform.scale(image.load("pic_fon.jpg"), (w, h))