"""
    Actor sprites are very similiar to boxes!
    Click 'Images' to see images available
    alien.png should already be there, but
    for other images you must add them yourself
"""
WIDTH = 500
HEIGHT = 500

alien = Actor('alien')
alien.x = 0
alien.y = 50


def draw():
    screen.clear()
    alien.draw()


def update():
    alien.x += 2
    if alien.x > WIDTH:
        alien.x = 0


"""TODO
    draw or download your own image to use instead of alien
"""
