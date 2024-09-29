import pgzrun
import random
import time

WIDTH = 1200
HEIGHT = 715

wonder_num = 7
wonders = []
lines = []
next_wonder = 0
start_time = 0
end_time = 0
total_time = 0

def make_wonders():
    global start_time
    for item in range(wonder_num):
        #wonder = random.randint(1,7)
        if item == 1:
            wonder = Actor("chichen_itza")
            wonder.pos = (random.randint(206,219), random.randint(373,400))
        elif item == 2:
            wonder = Actor("colosseum")
            wonder.pos = (random.randint(597,604), random.randint(300,309))
        elif item == 3:
            wonder = Actor("great_wall")
            wonder.pos = (random.randint(910,959), random.randint(309,365))
        elif item == 4:
            wonder = Actor("jesus_christ")
            wonder.pos = (random.randint(374,434), random.randint(477,530))
        elif item == 5:
            wonder = Actor("machu_picchu")
            wonder.pos = (random.randint(300,317), random.randint(479,511))
        elif item == 6:
            wonder = Actor("petra")
            wonder.pos = (random.randint(678,686), random.randint(350,357))
        else:
            wonder = Actor("taj_mahal")
            wonder.pos = (random.randint(800,830), random.randint(365,412))
        
        wonders.append(wonder)
    start_time = time.time()

def draw():
    global total_time 
    screen.blit("bgmap", (0,0))
    number = 1
    for item in wonders:
        screen.draw.text(str(number), (item.pos[0]-5, item.pos[1]+55), fontsize=30, color=(255,0,0))
        item.draw()
        number += 1
    
    for line in lines:
        screen.draw.line(line[0], line[1], color=(255,255,255))

    if next_wonder < wonder_num:
        total_time = time.time()-start_time
        screen.draw.text(str(round(total_time,1)), (10,10), fontsize=30, color=(255,255,255))
    else:
        screen,draw.text(str(round(total_time,1)), (10,10), fontsize=30, color=(255,255,255))


def update():
    pass

def on_mouse_down(pos):
    global next_wonder
    global lines
    global wonder_num
    global wonders

    if next_wonder < wonder_num:
        if wonders[next_wonder].collidepoint(pos):
            if next_wonder:
                lines.append((wonders[next_wonder-1].pos, wonders[next_wonder].pos))
                next_wonder += 1
                print(lines)
            else:
                lines = []
                next_wonder = 0

make_wonders()
pgzrun.go()
