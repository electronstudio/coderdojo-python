import random

n = random.randint(0, 10)

print("What is", n, "plus 7?")
g = int(input())  # why do we use int() here?
if g == n + 7:
    print("correct")
else:
    print("wrong")

# TODO:
# add some more questions, e.g.
#    instead of 7, use another random number
#    use a bigger random number
#    multiply or divide or subtract numbers
# print how many questions the player
# got correct at the end.
