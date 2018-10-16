from pico2d import *
import os

open_canvas(1600,900)

image = None
Right = None

class Right_Sprite:
    def __init__(self):
        self.x, self.y = 110, 190
        self.frame = 0
        os.chdir("C:\\Users\\김민규\\Documents\\Github\\2DGP\\Drills\\Game Project\\Resources")
        self.image = load_image('Right_run.png')

    def run(self):
        self.image.clip_draw(self.frame * 110, 0, 110, 190, self.x, self.y)

    def update(self):
        pass


def enter():
    global Right
    Right = Right_Sprite()

RunSwitch = False

def handle_events():
    events = get_events()
    global RunSwitch
    for event in events:
        if event.type == SDL_QUIT:
            pass
        if event.key == SDLK_RIGHT:
            RunSwitch = True
            Right.frame = (Right.frame + 1) % 6
            Right.x += 15

        if event.key == SDLK_RIGHT:
            RunSwitch = True
            Right.frame = (Right.frame + 1) % 6
            Right.x += 15



enter()

while(1):
    clear_canvas()
    Right.run()
    Right.update()
    handle_events()
    update_canvas()

close_canvas()