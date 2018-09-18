from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def calculate(x1,y1,x2,y2)

def move_locate(x1,y1,x2,y2):
    clear_canvas()
    grass.draw(400,30)
    character.draw(x1,y1)

    calculate(x1,y1,x2,y2)


    update_canvas()
    delay(0.01)

while True:
    move_locate(203,535 , 132,243)
    move_locate(132,243 , 535,470)

close_canvas()
