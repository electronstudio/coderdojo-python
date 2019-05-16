# Instead of using ready made colours like 'red', 'yellow', etc you can create your
# own color from three numbers. The numbers must be between 0-255 and represent
# how much red, green and blue to mix together, examples:
# my_colour = (0,0,0) # makes black
# my_colour = (255,255,255) # makes white

red_amount = 0
green_amount = 0
blue_amount = 0

def draw():
    my_colour = (red_amount, green_amount, blue_amount)
    screen.fill(my_colour)

def update():
    global red_amount
    red_amount += 1
    red_amount = red_amount % 255



# TODO
# Change the green and blue amounts to make different colours
# Can you make gray?
# Make random colours
