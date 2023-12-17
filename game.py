from pygame import *

window = display.set_mode((700, 500))
display.set_caption("Догонялки")

background = transform.scale(image.load("background.png"),(700, 500))

sprite_1 = transform.scale(image.load("sprite1.png"),(200, 100))
sprite_2 = transform.scale(image.load("sprite2.png"),(100, 100))
game = 1

############################################

clock = time.Clock()
x1 = 50
y1 = 150

x2 = 250
y2 = 150
speed = 10


# третий спрайт - управление клавишами мыши, Space, Ctrl, Shift
# добавьте ускорение на шифт

# фруктики, для хп или ускорения - столкновения и взаимодействия спрайтов


while game:

    window.blit(background, (0,0))
    window.blit(sprite_1, (x1,y1))
    window.blit(sprite_2, (x2,y2))


    for e in event.get():
        if e.type == QUIT:
            game = False


    clock.tick(120)

    display.update()

  










