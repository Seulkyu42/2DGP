from pico2d import *
import os
import Muk

os.chdir("C:\\Users\\김민규\\Documents\\Github\\2DGP\\Drills\\Game Project\\Resources")

class Grass:
    def __init__(self):
        self.image = load_image('Grass.png')

    def update(self):
        pass

    def draw(self):
        for i in range(0,5):
           self.image.draw(-2500 + 5000 * i - Muk.Muk.x, 1000)