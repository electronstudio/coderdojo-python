# Classic bat and ball game

WIDTH = 500
HEIGHT = 500

ball = Rect((150, 400), (20, 20))
bat = Rect((200, 480), (60, 20))
vx = 4
vy = 4

def draw():
    screen.clear()
    screen.draw.filled_rect(ball, "red")
    screen.draw.filled_rect(bat, "white")

def update():
    global vx, vy
    ball.x += vx
    ball.y += vy
    if ball.right > WIDTH or ball.left < 0:
        vx = -vx
    if ball.colliderect(bat) or ball.top < 0:
        vy = -vy
    if ball.bottom > HEIGHT:
        exit()
    if(keyboard.right):
        bat.x += 2
    elif(keyboard.left):
        bat.x -= 2

#TODO
# Add another bat at the top of the screen for player 2
# Add bricks (Rects) that disappear when the ball hits them
