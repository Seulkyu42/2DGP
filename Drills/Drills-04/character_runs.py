from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

x = 0
frame = 0
run_switch = 0

while(1):
    clear_canvas()
    grass.draw(400,30)
    frame = (frame + 1) % 8

    if(run_switch == 0):
        character.clip_draw(frame * 100, 100, 100, 100, x, 90)
        update_canvas()
        x += 10
        if(x >= 760):
            run_switch = 1
    elif(run_switch == 1):
        character.clip_draw(frame * 100, 0, 100, 100, x, 90)
        update_canvas()
        x -= 10
        if(x <= 20):
            run_switch = 0
    delay(0.05)
    get_events()

close_canvas()

