import random
import json
import pickle
import os
import sys

from pico2d import *
import game_framework
import game_world

import main_state
import world_build_state

boy = None
name = "WorldBuildState"

menu = None
font = None
data_str = None
line = 0

def enter():
    global menu
    menu = load_image('rank.png')
    hide_cursor()
    hide_lattice()

def __getstate__(self):
    state = {'Score' : main_state.boy.score}
    return state

def __setstate__(self, state):
    self.__init__()
    self.__dict__.update(state)

def exit():
    global menu
    del menu

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
            game_framework.change_state(world_build_state)

def update():
    global data_str,line,font
    if font == None:
        font = load_font('ENCR10B.TTF', 20)
    file = open('ranking_data.json', 'r')
    data_str = file.read()

    for i in range (5):
        font.draw(get_canvas_width() // 2 - 100, get_canvas_height() // 2, data_str, (0, 0, 0))

def draw():
    clear_canvas()
    menu.draw(get_canvas_width()//2, get_canvas_height()//2)
    update()
    update_canvas()






