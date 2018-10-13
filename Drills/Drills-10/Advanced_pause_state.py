import game_framework
from pico2d import *
import title_state
import main_state

name = "AdvancedPause"
image = None
grass = None
boy = None
stop = None
pause_time = 0

class Pause:
    def __init__(self):
        self.image = load_image('PAUSE.png')

    def draw(self):
        global pause_time
        if(pause_time > 50):
            pause_time += 1
            if(pause_time > 100):
                pause_time = 0
        else :
            self.image.draw(400, 300)
            pause_time += 1

    def update(self):
        pass

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)
class Boy:
    def __init__(self):
        self.x, self.y = main_state.boy.x ,90
        self.frame = 0
        self.image = load_image('run_animation.png')
        self.dir = 1

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        if self.x >= 800:
            self.dir = -1
        elif self.x <= 0:
            self.dir = 1

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

def enter():
    global boy,grass,stop
    boy = Boy()
    grass = Grass()
    stop = Pause()

def exit():
    global boy, grass, stop
    del(boy)
    del(grass)
    del(stop)

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

def update():
    stop.update()

def draw():
    clear_canvas()
    grass.draw()
    boy.draw()
    stop.draw()
    update_canvas()