from pico2d import *

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
    for i in range(0,300 + 1, 2):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        t = i / 300

        x = (1 - t)*p1[0]+t*p2[0]
        y = (1 - t)*p1[1]+t*p2[1]

        fx = (p1[0] - p2[0])



        update_canvas()

open_canvas(KPU_WIDTH,KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

running = True
i = 0

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)


    update_canvas()
    get_events()
    delay(0.02)
    handle_events()

close_canvas()