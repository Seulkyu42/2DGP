import Framework
import math
from pico2d import *
import os

open_canvas(1600,900)

image = None
Right = None
Back = None
Front = None

Jump_Switch = False
Run_Switch = False

class Right_Sprite:
    image = None
    def __init__(self):
        global Jump_Switch
        self.x, self.y = 110, 100
        self.x1 = 110
        self.frame = 0
        os.chdir("C:\\Users\\김민규\\Documents\\Github\\2DGP\\Drills\\Game Project\\Resources")
        if Right_Sprite.image == None:
            self.Run = load_image('Right_run.png')
            self.Jump = load_image("Jump_Right.png")
            self.Idle = load_image("Idle.png")

    def draw(self):
        Right.frame = (Right.frame + 1) % 4
        self.Idle.clip_draw(self.frame * 100, 0, 100, 200, self.x, self.y)
        delay(0.15)

    def jump(self):
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
                Right.y = 100
                Jump_Switch = False

    def run(self):
        self.Run.clip_draw(self.frame * 110, 0, 110, 190, self.x, self.y)
        Right.frame = (Right.frame + 1) % 6
        if(Right.x > 500):
            Right.x1 += 10
        else:
            Right.x += 10
        delay(0.03)

    def walk(self):
        pass

    def update(self):
        pass

class Background:
    def __init__(self):
        os.chdir("C:\\Users\\김민규\\Documents\\Github\\2DGP\\Drills\\Game Project\\Resources")
        self.image = load_image("BackGround_1.png")
    def draw(self):
        self.image.draw(500 - Right.x / 5 - Right.x1/5, 1000)

class Frontground:
    def __init__(self):
        os.chdir("C:\\Users\\김민규\\Documents\\Github\\2DGP\\Drills\\Game Project\\Resources")
        self.image = load_image("Grass.png")
    def draw(self):
        for i in range(0,5):
            self.image.draw(2500 * i - Right.x - Right.x1,1000)

def enter():
    global Right,Back,Front
    Back = Background()
    Right = Right_Sprite()
    Front = Frontground()

def handle_events():
    events = get_events()
    global Jump_Switch
    global Run_Switch
    for event in events:
        if event.type == SDL_QUIT:
            pass
        if (event.type, event.key) == (SDL_KEYDOWN,SDLK_RIGHT):
            Run_Switch = True
        elif(event.type, event.key) == (SDL_KEYUP,SDLK_RIGHT):
            Run_Switch = False
        if (event.type, event.key) ==  (SDL_KEYDOWN, SDLK_SPACE):
            Right.frame = 0
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
    Back.draw()
    if(Jump_Switch == True):
        Right.jump()
    elif(Run_Switch == True):
        Right.run()
        delay(0.01)
    else:
        Right.draw()
    Front.draw()
    update_canvas()


enter()
