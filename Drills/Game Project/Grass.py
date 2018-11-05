from pico2d import *
import os
from Muk import Muk

os.chdir("C:\\Users\\김민규\\Documents\\Github\\2DGP\\Drills\\Game Project\\Resources")

muk = None

class Grass:
    def __init__(self):
        self.image = load_image('Grass.png')

    def enter(self):
        pass

    def update(self):
        update_canvas()

    def draw(self):
        global muk
        muk = Muk()
        for i in range(0,5):
           self.image.draw(-2500 + 5000 * i - muk.x,  1000)