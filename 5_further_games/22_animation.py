# Most of this code is copied from program 15

alien = Actor("alien")
alien.pos = (200, 200)

def draw():
    screen.clear()
    alien.draw()

def update():
    if keyboard.right:
        alien.x = alien.x + 2
    elif keyboard.left:
        alien.x = alien.x - 2

images = ["alien_hurt", "alien"]
image_counter = 0

def animateAlien():
    global image_counter
    alien.image = images[image_counter % len(images)]
    image_counter += 1

clock.schedule_interval(animateAlien, 0.2)

""" TODO
make the alien animate faster
add another image to list of images
draw your own animation, e.g. a man walking left
and make it play when the left key is pressed
"""