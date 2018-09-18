from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def calculate(x1,y1,x2,y2):
    

def move_locate(x1,y1,x2,y2):
    clear_canvas()
    grass.draw_now(400,30)
    character.draw_now(x1, y1)

    calculate(x1,y1,x2,y2)

    delay(0.01)

while True:
    move_locate(203, 535, 132, 243)
    move_locate(132, 243, 535, 470)
    move_locate(535, 470, 477, 203)
    move_locate(477, 203, 715, 136)
    move_locate(715, 136, 316, 225)
    move_locate(316, 225, 510, 92)
    move_locate(510, 92, 692, 518)
    move_locate(692, 518, 682, 336)
    move_locate(682, 336, 712, 349)

close_canvas()
