from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def draw_curve_3_points(p1, p2, p3):
    frame = 0
    global fx,fx1
    for i in range(0,1000+1,1):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        t = i / 1000
        frame = (frame + 1) % 8
        x = (2*t**2-3*t+1)*p1[0]+(-4*t**2+4*t)*p2[0]+(2*t**2-t)*p3[0]
        y = (2*t**2-3*t+1)*p1[1]+(-4*t**2+4*t)*p2[1]+(2*t**2-t)*p3[1]

        fx = (p1[0] - p2[0])
        fx1 = (p2[0] - p3[0])

        if (fx < 0 and i < 500):

            character.clip_draw(frame * 100, 100, 100, 100, x, y)
        elif (fx > 0 and i <500):
            character.clip_draw(frame * 100, 0, 100, 100, x, y)

        if (fx1 < 0 and i > 499):
            character.clip_draw(frame * 100, 100, 100, 100, x, y)
        elif (fx1 > 0 and i > 499):
            character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()

x = [random.randint(50,1100) for i in range(11)]
y = [random.randint(50,900) for i in range(11)]

open_canvas(KPU_WIDTH,KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

running = True

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)

    #draw_curve_3_points((x[0], y[0]), (x[1], y[1]),(x[2], y[2]))
    #draw_curve_3_points((x[2], y[2]), (x[3], y[3]), (x[4], y[4]))
    #draw_curve_3_points((x[4], y[4]), (x[5], y[5]), (x[6], y[6]))
    #draw_curve_3_points((x[6], y[6]), (x[7], y[7]), (x[8], y[8]))
    #draw_curve_3_points((x[8], y[8]), (x[9], y[9]), (x[10], y[10]))
    #draw_curve_3_points((x[10], y[10]), (x[11], y[11]), (x[0], y[0]))


    update_canvas()
    get_events()

    handle_events()

close_canvas()