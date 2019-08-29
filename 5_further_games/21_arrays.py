"""
Create an empty array, use a loop to fill it with aliens
Draw the aliens, move the aliens
Add a new alien when the mouse is clicked
"""

WIDTH = 500
HEIGHT = 500

aliens = []
for i in range(0,10):
    aliens.append(Actor('alien', (i*30, i*30)))

def draw():
    screen.clear()
    for alien in aliens:
        alien.draw()

def update():
    for alien in aliens:
        alien.x += 2
        if alien.x > WIDTH:
            alien.x = 0

def on_mouse_down(pos, button):
    aliens.append(Actor('alien', pos))

"""TODO:
Go back to your previous game (e.g. program 16)
make an array of bullets that shoot when you
press the space bar
"""