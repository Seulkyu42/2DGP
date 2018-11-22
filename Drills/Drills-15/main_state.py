import random
import json
import os

from pico2d import *
import game_framework
import game_world

from boy import Boy
from background import InfiniteBackground as Background
from ball import Ball

name = "MainState"

boy = None
background = None
ba = []

Sound2 = None

def enter():
    global Sound2
    Sound2 = load_wav('pickup.wav')
    global boy
    boy = Boy()
    game_world.add_object(boy, 1)

    global background
    background = Background()
    game_world.add_object(background, 0)

    global ba
    ba = [Ball() for i in range(100)]

    game_world.add_objects(ba,1)

    background.set_center_object(boy)
    boy.set_background(background)



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
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)

def update():
    for game_object in game_world.all_objects():
        game_object.update()



def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






