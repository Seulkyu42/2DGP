import random
from pico2d import *
import game_world
import Framework
import os

os.chdir("C:\\Users\\김민규\\Documents\\Github\\2DGP\\Drills\\Game Project\\Resources")

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0
Frame_Monster1 = 8

class Monster1:
    image = None

    def __init__(self):
        if Monster1.image == None:
            Monster1.image = load_image('Monster1.png')
        self.x,self.y = 700, 50
        self.frame = 0


    def update(self):
        pass

    def do(self):
        Monster1.frame = (Monster1.frame + Frame_Monster1 * ACTION_PER_TIME * Framework.frame_time) % 8

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        self.image.clip_draw(int(self.frame) * 100, 0 , 100, 150, self.x,self.y)
        draw_rectangle(*self.get_bb())
