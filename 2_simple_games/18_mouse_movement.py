# wiggle your mouse around the screen!

alien = Actor("alien")

def draw():
    screen.clear()
    alien.draw()

def on_mouse_move(pos):
    alien.pos = pos

#TODO:
# what happens if you delete line 8 and replace it with this:
#
#   animate(alien, pos=pos, duration=1, tween='bounce_end')
#
# what happens if you change on_mouse_move to on_mouse_down?
# can you make a game with one alien controlled by mouse
#    and another controlled by keyboard?


