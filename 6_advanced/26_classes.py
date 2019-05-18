"""
You've already been using class types, e.g. Rect and Actor
But these classes do not include vx and vy variables, so let's
create our own class, Sprite, that is the same as Actor but with
these variables included
"""
WIDTH = 500
HEIGHT = 500

class Sprite(Actor):
    vx = 1
    vy = 1

ball = Sprite('alien')

def draw():
    screen.clear()
    ball.draw()

def update():
    ball.x += ball.vx
    ball.y += ball.vy
    if ball.right > WIDTH or ball.left < 0:
        ball.vx = -ball.vx
    if ball.bottom > HEIGHT or ball.top < 0:
        ball.vy = -ball.vy

