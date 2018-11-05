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
from Ui import Life

name = "MainState"

muk = None
back = None
grass = None
life = None

monsters = []

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b : return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True


def enter():
    global muk
    muk = Muk()
    game_world.add_object(muk, 1)

    global back
    back = Back()
    game_world.add_object(back, 0)

    global grass
    grass = Grass()
    game_world.add_object(grass,3)

    global monsters
    monsters = [Monster1() for i in range(5)]
    game_world.add_object(monsters, 2)

    global life
    life = Life()
    game_world.add_object(life,4)

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
    global muk,monster1
    for game_object in game_world.all_objects():
        game_object.update()

    for Enemy in monsters:
        if collide(muk, Enemy):
            print("충돌")
            muk.x -= 100
            muk.Life -= 1
            print("Life %d" % muk.Life)


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






