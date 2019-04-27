import pygame

# IMPORTANT: switch Mu mode to "Pygame Zero" or
# nothing will appear!

WIDTH = 500
HEIGHT = 500  # what are these units?

#pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()


def draw():

    screen.clear()
    screen.draw.circle((250, 250), 50, "white")
    screen.draw.filled_circle((250, 100), 50, "red")
    screen.draw.line((0, 0), (100, 150), "purple")

def update():
    a = joystick.get_button(0)
    print(str(a))

# TODO: draw a picture
