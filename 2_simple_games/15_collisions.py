"""
    Most of this code is copied from programs 11 and 13
"""
WIDTH = 500

alien = Actor("alien")
alien.pos = (0, 50)
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
    box.x = box.x + 2
    if box.x > WIDTH:
        box.x = 0
    if alien.colliderect(box):
        print("hit")


""" TODO
    joystick input (again), vertical movement (again)
    make the box chase the alien
    print number of times hit (the score)
"""
