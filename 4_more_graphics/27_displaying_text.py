"""
Simple game that displays text on screen
"""
WIDTH = 500
HEIGHT = 500

score = 0

def draw():
    screen.clear()
    screen.draw.text(f"Player 1 score: {score}", (0, 0))
    screen.draw.textbox("Hello mum", Rect(50, 50, 200, 200))

# This is another special function that is called by Pygame automatically
# each time a key is pressed. That way player cannot just hold down key!

def on_key_down(key):
    global score
    if key == keys.SPACE:
        score += 1

"""
TODO
Make the score text larger
Add a second player who presses a different key and show their score too
Add text to one of your other games
"""