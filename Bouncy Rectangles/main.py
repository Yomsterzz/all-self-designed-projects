import pgzrun
import random

WIDTH = 800
HEIGHT = 800
TITLE = "Bouncy Rectangles!"

color1 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
color2 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
color3 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
color4 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

width1 = random.randint(100, 175)
width2 = random.randint(100, 175)
width3 = random.randint(100, 175)
width4 = random.randint(100, 175)

height1 = random.randint(100, 200)
height2 = random.randint(100, 200)
height3 = random.randint(100, 200)
height4 = random.randint(100, 200)

gravity = 4000.0

class Rectangle:
    def __init__(self, color, width, height, x, y, xvel):
        self.color = color
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.xvel = xvel
        self.yvel = 0
    
    def draw_rectangle(self):
        rect = Rect((self.x, self.y), (self.width, self.height))
        screen.draw.filled_rect(rect, self.color)
    
rectangle1 = Rectangle(color1, width1, height1, 150, 100, 100)
rectangle2 = Rectangle(color2, width2, height2, 300, 200, 200)
rectangle3 = Rectangle(color3, width3, height3, 450, 300, 300)
rectangle4 = Rectangle(color4, width4, height4, 600, 400, 400)

rectangles = [rectangle1, rectangle2, rectangle3, rectangle4]

def draw():
    screen.clear()
    for rectangle in rectangles:
        rectangle.draw_rectangle()

def update(c):
    for rectangle in rectangles:
        rectangley = rectangle.yvel
        rectangle.yvel += gravity * c
        rectangle.y += (rectangley + rectangle.yvel) * 0.5 * c

    for rectangle in rectangles: 
        if rectangle.y > HEIGHT - rectangle.height:
            rectangle.y = HEIGHT - rectangle.height
            rectangle.yvel = -rectangle.yvel * 0.9
    
    for rectangle in rectangles:
        rectangle.x += rectangle.xvel * c
        if rectangle.x > WIDTH - rectangle.width or rectangle.x < rectangle.width:
            rectangle.xvel = -rectangle.xvel


def on_mouse_down():
        rectangle1.yvel = -2000
        rectangle2.yvel = -1000
        rectangle3.yvel = -1500
        rectangle4.yvel = -2500
pgzrun.go()
