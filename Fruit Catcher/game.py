import pgzrun
import random

WIDTH = 1000
HEIGHT = 600

background = Actor("background")  
bowl = Actor("bowl")  
apple = Actor("apple")
banana = Actor("banana")    

bowl.pos = WIDTH / 2, HEIGHT - 50
apple.pos = random.randint(50, WIDTH - 50), 100
banana.pos = random.randint(50, WIDTH - 50), 100

score = 0
lives = 3
game_over = False

def draw():
    screen.clear()
    if game_over:
        screen.draw.text('Game Over', (300, 250), color=(255,255,255), fontsize=60)
        screen.draw.text('Your final score was: ' + str(score), (300, 350), color=(255,255,255), fontsize=60)
    else: 
        background.draw()
        bowl.draw()
        apple.draw()
        banana.draw()
        screen.draw.text("Score: " + str(score), color="white", fontsize=50, topleft=(100, 10))
        screen.draw.text("Lives: " + str(lives), color="white", fontsize=50, topleft=(600, 10))

def update():
    global score
    global lives
    global game_over

    apple.y += 5  

    if apple.colliderect(bowl):
        score += 1
        reset_apple()

    if apple.y > HEIGHT:
        reset_apple()
        lives -= 1
    
    banana.y += 5  

    if banana.colliderect(bowl):
        score += 1
        reset_banana()

    if banana.y > HEIGHT:
        reset_banana()
        lives -= 1
    
    if lives == 0:
        game_over = True

def reset_apple():
    global score
    apple.x = random.randint(50, WIDTH - 50)
    apple.y = 50 

def reset_banana():
    global score
    banana.x = random.randint(50, WIDTH - 50)
    banana.y = 50 

def on_mouse_move(pos):
    bowl.x = pos[0]
    if bowl.left < 0:
        bowl.left = 0
    elif bowl.right > WIDTH:
        bowl.right = WIDTH

pgzrun.go()