import game_framework
from pico2d import *
import title_state
import main_state

name = "Pause"
image = None

def enter():
    global image
    image = load_image('pause.png')

def exit():
    global image
    del(image)


def update():

    update_canvas()

def draw():
    global image
    clear_canvas()
    image.draw(400, 300)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.change_state(title_state)
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                game_framework.pop_state()


def pause():
    pass

def resume():
    pass