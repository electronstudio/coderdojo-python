"""
    Program 15 but the box chases the alien and game exits if it catches him
"""
WIDTH = 500
HEIGHT = 500

alien = Actor("alien")
alien.pos = (400, 50)
box = Rect((20, 20), (100, 100))

def draw():
    screen.clear()
    screen.draw.filled_rect(box, "red")
    alien.draw()

def update():
    if keyboard.right:
        alien.x = alien.x + 2
    elif keyboard.left:
        alien.x = alien.x - 2
    if box.x < alien.x:
        box.x = box.x + 1
    if box.x > alien.x:
        box.x = box.x - 1
    if alien.colliderect(box):
        exit()


""" TODO
    joystick input (again), vertical movement (again)
    instead of a box use another Actor that you have drawn
"""
