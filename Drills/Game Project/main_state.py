import random
import json
import os

from pico2d import *
import Framework
import game_world

from Muk import Muk
from background import Back
from Grass import Grass
from Enemy import Monster1

name = "MainState"

muk = None
back = None
grass = None
monster1 = None

def enter():
    global muk,back,grass,monster1
    muk = Muk()
    back = Back()
    grass = Grass()
    monster1 = Monster1
    game_world.add_object(back, 0)
    game_world.add_object(muk, 1)
    game_world.add_object(monster1, 2)
    game_world.add_object(grass,3)

def exit():
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            Framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                Framework.quit()
        else:
            muk.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






