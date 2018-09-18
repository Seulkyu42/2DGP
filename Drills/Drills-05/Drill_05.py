from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def move_locate(x,y):
    clear_canvas()
    grass.draw(400,30)
    character.draw(x,y)
    
    update_canvas()
    delay(0.01)

while True:
    move_locate(203,535)
    move_locate(132,243)
    move_locate(535,470)

close_canvas()
