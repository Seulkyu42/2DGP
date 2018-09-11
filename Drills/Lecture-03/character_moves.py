from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 410
y = 90
switch = 0
cnt = 0

sin_degree = 0
cos_degree = 0
while (1):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    
    if(cnt == 0):
        if (switch == 0):
            x = x + 10
            
        if (x >= 780):
            switch = 1
            y = y + 10
            
        if (y >= 550):
            if (switch == 1):
                x = x - 10
                
        if (x <= 20):
            if (switch == 1):
                y = y - 10
            
        if (y <= 90):
            switch = 0

        if(x > 392 and x < 408):
            if(y <= 100):
                cnt = 1


    if (cnt == 1):
        sin_degree = sin_degree + 10
        cos_degree = cos_degree + 10
        
        x = 400 + 210*math.sin(sin_degree/360)
        y = 300 - 210*math.cos(cos_degree/360)

        if(x <= 400 ):
            if(y <= 91):
                sin_degree =0
                cos_degree =0
                x = 410
                y = 90
                cnt = 0


    delay(0.01)
    
close_canvas()
