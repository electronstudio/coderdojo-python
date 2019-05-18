"""
draw red cirlces using a loop
draw green circles using a loop within another loop
"""
WIDTH = 500
HEIGHT = 500

def draw():
    screen.clear()
    for x in range(0, WIDTH, 40):
        screen.draw.filled_circle((x, 20), 20, "red")

    for x in range(0, WIDTH, 40):
        for y in range(60, HEIGHT, 40):
            screen.draw.filled_circle((x, y), 10, "green")

"""TODO:
import random and make the positions random, e.g.
     random.randint(0, 100)
learn about RGB colour and make random colours (see colours.py)
create a timer variable and change colours based on time (see timer.py)
"""