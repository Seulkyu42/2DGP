from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def move_locate(x1,y1,x2,y2):
    clear_canvas()
    grass.draw_now(400,30)
    character.draw_now(x1, y1)

    calculate(203,535,132,243)


    delay(0.01)

while True:
    move_locate(203,535,132,243)


close_canvas()
