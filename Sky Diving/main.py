import pygame
import random
import time

pygame.init()

WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
orange = (255, 165, 0)

enemies = []
last_enemy_time = time.time()

running = True
clock = pygame.time.Clock()
score = 0

player = pygame.Rect(200, 300, 40, 40)
gravity = 2.0
gravity_increment = score/500

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= 5
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.x += 5

    gravity += 0.01

    if player.top > HEIGHT:
        player.x, player.y = 200, 300
        gravity = 2.0
        score = 0

    if time.time() - last_enemy_time > 1:  
        x = random.randint(0, WIDTH - 100)
        if random.randint(1,2) == 1:
            color = red
        else:
            color = orange
        enemies.append([pygame.Rect(x, HEIGHT + 20, 100, 20), color])
        last_enemy_time = time.time()

    for enemy in enemies[:]:
        enemy[0].y -= gravity
        if player.colliderect(enemy[0]):
            player.x, player.y = 200, 300
            gravity = 2.0
            score = 0
            enemies.clear()
        if enemy[0].y < -20:
            enemies.remove(enemy)

    screen.fill(white)
    pygame.draw.rect(screen, blue, player)
    for enemy in enemies:
        pygame.draw.rect(screen, enemy[1], enemy[0])

    score += 1
    font = pygame.font.SysFont(None, 36)
    text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(text, (10, 10))

    pygame.display.update()

pygame.quit()
