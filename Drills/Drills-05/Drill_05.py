from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')

def move_locate(x1,y1,x2,y2):
    clear_canvas()
    grass.draw(400,30)

    frame = 0
    fx = (x2 - x1) / 30
    fy = (y2 - y1) / 30

    for i in range(1,30):
        clear_canvas()
        grass.draw(400, 30)
        frame = (frame + 1) % 8
        i += 1

        if (fx * 30 > 0):
            character.clip_draw(frame * 100, 100, 100, 100, x1 + fx * i, y1 + fy * i)
        if (fx * 30 < 0):
            character.clip_draw(frame * 100, 0, 100, 100, x1 + fx * i, y1 + fy * i)

        #character.draw(x1 + fx * i, y1+ fy * i)
        update_canvas()
        delay(0.025)
        get_events()



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
    move_locate(712, 349, 203, 535)

close_canvas()
