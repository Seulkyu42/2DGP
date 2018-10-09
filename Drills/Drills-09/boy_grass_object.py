from pico2d import *
import random

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400,30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100,700),90
        self.frame = random.randint(0,7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame+1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100,0,100,100,self.x,self.y)

class Ball:
    def __init__(self):
        self.x, self.y = random.randint(100,700),599

        self.speed = random.randint(1, 10)
        self.make = random.randint(1,2)

        if(self.make == 1):
            self.image = load_image('ball21x21.png')
        elif(self.make == 2):
            self.image = load_image('ball41x41.png')

    def draw(self):
        self.image.draw(self.x,self.y)

    def drop(self):
        if(self.make == 1 and self.y > 65):
            self.y = self.y - self.speed
        elif(self.make == 2 and self.y > 75):
            self.y = self.y - self.speed

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas()

team = [Boy() for i in range(11)]
teamBall = [Ball() for i in range(20)]
ball = Ball()
boy = Boy()
grass = Grass()

running = True;

while running:
    handle_events()

    for boy in team:
        boy.update()

    for boy in team:
        boy.draw()

    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()

    delay(0.05)


# finalization code