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

frame = 0
def draw_line(p1,p2):
    global frame
    for i in range(0,300 + 1, 1):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        t = i / 300
        frame = (frame + 1) % 8
        x = (1 - t)*p1[0]+t*p2[0]
        y = (1 - t)*p1[1]+t*p2[1]

        fx = (p1[0] - p2[0])

        if (fx < 0):
            character.clip_draw(frame * 100, 100, 100, 100, x, y)
        elif (fx > 0):
            character.clip_draw(frame * 100, 0, 100, 100, x, y)

        update_canvas()

x = [random.randint(50,1100) for i in range(20)]
y = [random.randint(50,900) for i in range(20)]

open_canvas(KPU_WIDTH,KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

running = True
i = 0

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)

    draw_line((x[i - 1], y[i - 1]), (x[i], y[i]))
    i = (i + 1) % 20

    update_canvas()
    get_events()
    delay(0.02)
    handle_events()

close_canvas()