import random



WIDTH = 600
HEIGHT = 600
import random

level = 1
lives = 3

MAX_BULLETS = 3

background = Actor("background")
player = Actor("player", pos=(200,580))


enemies = []


bullets = []
bombs = []


score = 0
time = 20

def create_enemies():
    global level
    level = level + 1

#Actor("alien", pos=(0,300)),
#Actor("alien", pos=(300,300)),
#Actor("alien", pos=(400,300))
#]

    for x in range(0,600, 60):
        for y in range(0,200, 60):
            enemy = Actor("alien", pos=(x, y))
            enemy.vx = level * 3
            enemies.append(enemy)


def on_key_down(key):
    if(key==keys.SPACE and len(bullets) < MAX_BULLETS):
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
    for bomb in bombs:
        bomb.draw()
    draw_text()

def update(delta):
    if len(enemies)==0:
        create_enemies()
    move_player()
    move_bullets()
    move_enemies()
    create_bombs()
    move_bombs()

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
        if bullet.y < 0:
            bullets.remove(bullet)

def create_bombs():
    if(random.randint(0,30)==0):
        print("foo")
        enemy = random.choice(enemies)
        bomb = Actor("player", pos=enemy.pos)
        bombs.append(bomb)

def move_bombs():
    global lives
    for bomb in bombs:
        bomb.y = bomb.y + 10
        if bomb.colliderect(player):
            bombs.remove(bomb)
            lives = lives - 1
            if lives == 0:
                exit()

def move_enemies():
    global score
    for enemy in enemies:
        enemy.x = enemy.x + enemy.vx
        if enemy.x > WIDTH or enemy.x < 0:
            enemy.vx = -enemy.vx
            animate(enemy, duration=0.1, y=enemy.y+60)
        for bullet in bullets:
            if bullet.colliderect(enemy):
                enemies.remove(enemy)
                bullets.remove(bullet)
                score = score + 1
        if enemy.colliderect(player):
            exit()
#        if enemy.collidelist(bullets) != -1:
#            dead_enemies.append(enemy)
#            enemies.remove(enemy)
#    for enemy in dead_enemies:
#        enemies.remove(enemy)


def draw_text():
    screen.draw.text("Level "+str(level), (0,0), color='red')
    screen.draw.text("Score "+str(score), (100,0), color='red')
    screen.draw.text("Lives "+str(lives), (200,0), color='red')



