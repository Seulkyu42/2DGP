import random
from pico2d import *
import game_world
import game_framework
import main_state

class Ball:
    image = None

    def __init__(self):
        self.bx,self.by = 0,0
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y= random.randint(500,2100), random.randint(350,1400)

    def get_bb(self):
        return self.bx - 10, self.by - 10, self.bx + 10, self.by + 10

    def draw(self):
        self.image.draw(self.bx, self.by)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.bx = self.x - main_state.boy.x
        self.by = self.y - main_state.boy.y
