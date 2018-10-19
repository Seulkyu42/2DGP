import Framework
import math
from pico2d import *
import os

open_canvas(1600,900)

image = None
Right = None

Jump_Switch = False

class Right_Sprite:
    def __init__(self):
        global Jump_Switch
        self.x, self.y = 110, 190
        self.frame = 0
        os.chdir("C:\\Users\\김민규\\Documents\\Github\\2DGP\\Drills\\Game Project\\Resources")
        self.Run = load_image('Right_run.png')
        self.Jump = load_image("Jump_Right.png")

    def draw(self):
        global Jump_Switch
        self.Jump.clip_draw(self.frame * 120, 0, 120, 190, self.x, self.y)
        if (Jump_Switch == True):
            Right.frame = (Right.frame + 1) % 8
            Right.x += 20
            Right.y += 70 * math.sin(Right.frame)
            delay(0.06)
            if (Right.frame == 4):
                Right.y += 25
                Right.x += 40
            if (Right.frame == 0):
                Right.x = 100
                Right.y = 190
                Jump_Switch = False

    def jump(self):

        self.Jump.clip_draw(self.frame * 120, 0, 120, 190, self.x, self.y)




    def run(self):
        self.Run.clip_draw(self.frame * 110, 0, 110, 190, self.x, self.y)
        Right.frame = (Right.frame + 1) % 6
        Right.x += 15

    def walk(self):
        pass

    def update(self):
        pass


def enter():
    global Right
    Right = Right_Sprite()

def handle_events():
    events = get_events()
    global Jump_Switch
    for event in events:
        if event.type == SDL_QUIT:
            pass
        if (event.type, event.key) == (SDLK_RIGHT):
            Right.run()

        if (event.type, event.key) ==  (SDL_KEYDOWN, SDLK_SPACE):
            Jump_Switch = True

def exit():
    pass

def pause():
    pass

def resume():
    pass

def update():
    Right.update()

def draw():
    clear_canvas()
    Right.draw()
    update_canvas()


enter()
