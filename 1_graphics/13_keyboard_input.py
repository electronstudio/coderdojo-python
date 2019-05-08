alien = Actor('alien')
alien.pos = (0,50)

def draw():
    screen.clear()
    alien.draw()

def update():
    if(keyboard.right):
        alien.x = alien.x + 2
    elif(keyboard.left):
        alien.x = alien.x - 2

#TODO
# make the alien move up and down as well as left and right
# use the += operator to change the alien.x more concisely
# use the 'or' operator to allow WASD keys to move the alien
#   in addition to the cursor keys
# make alien wrap around when he moves off edge of screen
