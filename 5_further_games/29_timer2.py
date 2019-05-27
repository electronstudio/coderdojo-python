"""
Pygame has its own clock which we can use by asking it to call one of our
functions at a certain time, or regularly over and over at an interval.
"""

import random

aliens = []

def add_alien():
    aliens.append(
        Actor("alien", (random.randint(0,500), random.randint(0,500)))
    )

# call add_alien once, 0.5 seconds from now
clock.schedule(add_alien, 0.5)

# call add_alien over and over again, ever 2 seconds
clock.schedule_interval(add_alien, 2.0)

def draw():
    screen.clear()
    for alien in aliens:
        alien.draw()

"""TODO
Make the aliens appear much faster
Use len(aliens) to print how many aliens there are
When there are too many aliens, stop adding them using this code:
    clock.unschedule(add_alien)
"""
