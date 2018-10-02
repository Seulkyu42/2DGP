from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def handle_events():
    global running
    global x,y,x1,y1,x2,y2
    global fx, fy
    global count
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            count = 0
            x1,y1 = x2 ,y2
            x2, y2 = event.x, KPU_HEIGHT - 1 - event.y

            fx = (x1 - x2) // 30
            fy = (y1 - y2) // 30


        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas(KPU_WIDTH,KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
cursor = load_image('hand_arrow.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
x1,y1 = KPU_WIDTH // 2, KPU_HEIGHT // 2
x2, y2 = x1,y1

fx,fy = 0,0

frame = 0
hide_cursor()

i = 0
count = 0

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    cursor.draw(x, y)
    if (fx * 30 < 0):
        character.clip_draw(frame * 100, 100, 100, 100, x1-30, y1+30 )
    elif (fx * 30 > 0):
        character.clip_draw(frame * 100, 0, 100, 100, x1-30, y1+30)
    if(count < 30):
        x1 -= fx
        y1 -= fy
    count += 1

    update_canvas()
    update_canvas()
    get_events()
    frame = (frame + 1) % 8
    delay(0.02)
    handle_events()



close_canvas()