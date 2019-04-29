# Some game controllers may have different inputs
# and some may not be compatible so don't be
# surprised if this doesnt quite work properly!
# Use joystick_tester.py program to test yours.

import pygame

joystick = pygame.joystick.Joystick(0)
joystick.init()

WIDTH = 500
HEIGHT = 500

alien = Actor('alien')
alien.pos = (0,50)

def draw():
    screen.clear()
    alien.draw()

def update():
    if(keyboard.right or joystick.get_axis(0)>0.1):
        alien.x = alien.x + 2
    elif(keyboard.left or joystick.get_axis(0)<-0.1):
        alien.x = alien.x - 2

#TODO
# make the alien move up and down as well as left and right
