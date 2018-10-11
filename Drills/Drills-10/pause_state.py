import game_framework
from pico2d import *

name = "Pause"
image = None

def enter():
    global image
    image = load_image('pause.png')

def exit():
    global image
    del(image)


def update():
    pass

def draw():
    global image
    image.draw(400, 300)

def handle_events():
    events = get_events()
    pass


def pause():
    pass

def resume():
    pass