from pico2d import *
import os
from Muk import Muk

os.chdir("C:\\Users\\김민규\\Documents\\Github\\2DGP\\Drills\\Game Project\\Resources")

muk = None

class Life:
    def __init__(self):
        self.image = load_image('Life.png')

    def enter(self):
        pass

    def update(self):
        global muk
        muk = Muk()
        for i in range(0, muk.Life):
            self.image.draw(100 + 50 * i, 850)

    def draw(self):
        self.update()
