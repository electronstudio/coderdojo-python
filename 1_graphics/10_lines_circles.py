"""
IMPORTANT: switch Mu mode to "Pygame Zero" or
nothing will appear!
"""
WIDTH = 500  # What are these units? What if we change them?
HEIGHT = 500  # What if we delete this line?


def draw():
    screen.clear()
    screen.draw.circle((250, 250), 50, "white")
    screen.draw.filled_circle((250, 100), 50, "red")
    screen.draw.line((150, 20), (150, 450), "purple")
    screen.draw.line((150, 20), (350, 20), "purple")


""" TODO:
    Finishing drawing this picture, or your own picture.
    Make sure you understand (x,y) co-ordinates
    (In maths this called a 'Cartesian coordinate system'
    and everything we do in Pygame Zero will use it)
"""
