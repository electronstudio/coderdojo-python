import random

WIDTH = 600
HEIGHT = 600

background = Actor("background")
player = Actor("player")
player.x = 200
player.y = 200

enemies = []
#Actor("alien", pos=(0,300)),
#Actor("alien", pos=(300,300)),
#Actor("alien", pos=(400,300))
#]

for x in range(0,600, 60):
    for y in range(0,300, 60):
        enemy = Actor("alien", pos=(x, y))
        enemy.vx = 1
        enemies.append(enemy)

bullets = []

player2 = Actor("player")
coin = Actor("alien", pos=(300,300))
score = 0
time = 20

def on_key_down(key):
    if(key==keys.SPACE):
        bullet = Actor("alien", pos=(player.x, player.y))
        bullets.append(bullet)

def draw():
    screen.clear()
    background.draw()
    player.draw()
    for enemy in enemies:
        enemy.draw()
    for bullet in bullets:
        bullet.draw()

def update(delta):
    move_player()
    move_bullets()
    move_enemies()

def move_player():
    if keyboard.right:
        player.x = player.x + 4
    if keyboard.left:
        player.x = player.x - 4

    if player.x > WIDTH:
        player.x = WIDTH
    if player.x < 0:
        player.x = 0

def move_bullets():
    for bullet in bullets:
        bullet.y = bullet.y - 5

def move_enemies():
    dead_enemies = []
    for enemy in enemies:
        enemy.x = enemy.x + enemy.vx
        if enemy.x > WIDTH or enemy.x < 0:
            enemy.vx = -enemy.vx
            animate(enemy, duration=0.1, y=enemy.y+60)
        collided_enemy_index = enemy.collidelist(bullets)
        if collided_enemy_index != -1:
            dead_enemies.append(enemies[collided_enemy_index])
    for enemy in dead_enemies:
        enemies.remove(dea)








