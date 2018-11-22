import random
from pico2d import *
import game_world
import game_framework
import main_state

class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y= random.randint(500,2100), random.randint(350,1400)

    def set_background(self, bg):
        self.bg = bg
        self.x = self.bg.w / 2
        self.y = self.bg.h / 2

    def get_bb(self):
        return self.x -main_state.boy.x  - 10, self.y -main_state.boy.y - 10, self.x -main_state.boy.x + 10, self.y -main_state.boy.y + 10

    def draw(self):
        self.image.draw(self.x-main_state.boy.x,self.y-main_state.boy.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass
