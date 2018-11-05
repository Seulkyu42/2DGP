import Framework
from pico2d import *
import os

os.chdir("C:\\Users\\김민규\\Documents\\Github\\2DGP\\Drills\\Game Project\\Resources")

PIXEL_PER_METER = (10.0/0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0
Frame_Idle = 4
Frame_Run = 6


RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SPACE,Mode1,Mode2,Mode3,Mode4 = range(9)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE,
    (SDL_KEYDOWN, SDLK_1): Mode1,
    (SDL_KEYDOWN, SDLK_2): Mode2,
    (SDL_KEYDOWN, SDLK_3): Mode3,
    (SDL_KEYDOWN, SDLK_4): Mode4,
}

class IdleState:
    @staticmethod
    def enter(muk, event):
        if event == RIGHT_UP:
            muk.velocity -= RUN_SPEED_PPS

    @staticmethod
    def exit(muk, event):
        pass

    @staticmethod
    def do(muk):
        if SDL_KEYDOWN == SDLK_1:
            muk.x, muk.y = 0, 90
            muk.Mode = 1
        elif SDL_KEYDOWN == SDLK_2:
            muk.x, muk.y = 1500, 90
            muk.Mode = 2
        elif SDL_KEYDOWN == SDLK_3:
            muk.x, muk.y = 1500, 800
            muk.Mode = 3
        elif SDL_KEYDOWN == SDLK_4:
            muk.x, muk.y = 0, 800
            muk.Mode = 4

        muk.frame = (muk.frame + Frame_Idle * ACTION_PER_TIME * Framework.frame_time) % 4

    @staticmethod
    def draw(muk):
        muk.Idle_image.clip_draw(int(muk.frame) * 100, 0, 100, 200, muk.x, muk.y)

class RunState:
    @staticmethod
    def enter(muk, event):
        if event == RIGHT_DOWN:
            muk.velocity += RUN_SPEED_PPS
        elif event == RIGHT_UP:
            muk.velocity -= RUN_SPEED_PPS

        if muk.Mode == 1:
            print("Mode : 1")
            muk.add_event(Mode1)
        if muk.Mode == 2:
            print("Mode : 2")
            muk.add_event(Mode2)
        if muk.Mode == 3:
            print("Mode : 3")
            muk.add_event(Mode3)
        if muk.Mode == 4:
            print("Mode : 4")
            muk.add_event(Mode4)

    @staticmethod
    def exit(muk, event):
        pass

    @staticmethod
    def do(muk):
        pass

    @staticmethod
    def draw(muk):
        pass

class RunState_Mode1:
    @staticmethod
    def enter(muk, event):
        if event == RIGHT_DOWN:
            muk.velocity += RUN_SPEED_PPS
        elif event == RIGHT_UP:
            muk.velocity -= RUN_SPEED_PPS

    @staticmethod
    def exit(muk, event):
        pass

    @staticmethod
    def do(muk):
        muk.frame = (muk.frame + Frame_Run * ACTION_PER_TIME * Framework.frame_time) % 6
        muk.x += muk.velocity * Framework.frame_time

    @staticmethod
    def draw(muk):
        muk.Run_image.clip_draw(int(muk.frame) * 110, 0, 110, 200, muk.x, muk.y)

class RunState_Mode2:
    @staticmethod
    def enter(muk, event):
        if event == RIGHT_DOWN:
            muk.velocity += RUN_SPEED_PPS
        elif event == RIGHT_UP:
            muk.velocity -= RUN_SPEED_PPS

    @staticmethod
    def exit(muk, event):
        pass

    @staticmethod
    def do(muk):
        muk.frame = (muk.frame + Frame_Run * ACTION_PER_TIME * Framework.frame_time) % 6
        muk.y += muk.velocity * Framework.frame_time

    @staticmethod
    def draw(muk):
        muk.Run_image.clip_composite_draw(int(muk.frame) * 110,0,110,200, 3.141492/2, '',muk.x,muk.y,110,200)

class RunState_Mode3:
    @staticmethod
    def enter(muk, event):
        if event == RIGHT_DOWN:
            muk.velocity += RUN_SPEED_PPS
        elif event == RIGHT_UP:
            muk.velocity -= RUN_SPEED_PPS

    @staticmethod
    def exit(muk, event):
        pass

    @staticmethod
    def do(muk):
        muk.frame = (muk.frame + Frame_Run * ACTION_PER_TIME * Framework.frame_time) % 6
        muk.x -= muk.velocity * Framework.frame_time

    @staticmethod
    def draw(muk):
        muk.Run_image.clip_composite_draw(int(muk.frame) * 110,0,110,200, 3.141492, '',muk.x,muk.y,110,200)

class RunState_Mode4:
    @staticmethod
    def enter(muk, event):
        if event == RIGHT_DOWN:
            muk.velocity += RUN_SPEED_PPS
        elif event == RIGHT_UP:
            muk.velocity -= RUN_SPEED_PPS

    @staticmethod
    def exit(muk, event):
        pass

    @staticmethod
    def do(muk):
        muk.frame = (muk.frame + Frame_Run * ACTION_PER_TIME * Framework.frame_time) % 6
        muk.y -= muk.velocity * Framework.frame_time

    @staticmethod
    def draw(muk):
        muk.Run_image.clip_composite_draw(int(muk.frame) * 110,0,110,200, -3.141492/2, '',muk.x,muk.y,110,200)


next_state_table = {
    IdleState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, SPACE: IdleState,
                Mode1: RunState_Mode1, Mode2: RunState_Mode2, Mode3: RunState_Mode3, Mode4: RunState_Mode4},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, SPACE: RunState,
                Mode1 : RunState_Mode1,Mode2 : RunState_Mode2,Mode3 : RunState_Mode3,Mode4 : RunState_Mode4},
    RunState_Mode1: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, SPACE: RunState,
                     Mode1: RunState_Mode1, Mode2: RunState_Mode2, Mode3: RunState_Mode3, Mode4: RunState_Mode4},
    RunState_Mode2: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, SPACE: RunState,
                     Mode1: RunState_Mode1, Mode2: RunState_Mode2, Mode3: RunState_Mode3, Mode4: RunState_Mode4},
    RunState_Mode3: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, SPACE: RunState,
                     Mode1: RunState_Mode1, Mode2: RunState_Mode2, Mode3: RunState_Mode3, Mode4: RunState_Mode4},
    RunState_Mode4: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, SPACE: RunState
                     ,Mode1 : RunState_Mode1,Mode2 : RunState_Mode2,Mode3 : RunState_Mode3,Mode4 : RunState_Mode4},
}

class Muk:
    def __init__(self):
        self.x, self.y = 500, 90
        self.Idle_image = load_image("Idle.png")
        self.Run_image = load_image("Right_run.png")
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.font = load_font('ENCR10B.TTF', 16)
        self.Mode = 1
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def get_bb(self):
        if self.Mode == 1 or self.Mode == 3:
            return self.x - 50, self.y - 100, self.x + 50, self.y + 100
        elif self.Mode == 2 or self.Mode == 4:
            return self.x - 100, self.y - 50, self.x + 100, self.y + 50



    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        self.font.draw(self.x - 55, self.y + 110, '(Mode : %d)' % self.Mode, (255, 0, 0))
        draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

