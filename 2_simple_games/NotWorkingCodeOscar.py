WIDTH=500

meteor = Actor("alien")
meteor.pos= (250, 0)

meteors = []
for i in range(0,10):
    meteors.append(Actor('a', (i*30, i*30)))


def draw():
    screen.clear()
    for meteor in meteors:
        meteor.draw()

def update():
    for meteor in meteors:
        meteor.y += 3.5
        if meteor.y > WIDTH:
            meteor.y = 0

def on_mouse_down(pos, button):
    meteors.append(Actor('meteor', pos))
