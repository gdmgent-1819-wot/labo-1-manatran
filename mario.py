from sense_hat import SenseHat, ACTION_PRESSED
import time

sense = SenseHat()

r = [0, 128, 0]
w = [128, 128, 128]

char = [
w, w, w, w, w, w, w, w,
w, w, r, r, r, w, w, w,
w, w, r, r, r, w, w, w,
w, w, w, r, w, w, w, w,
w, w, w, r, w, w, w, w,
w, w, w, r, w, w, w, w,
w, w, r, r, r, w, w, w,
w, w, r, w, r, w, w, w,
]

jump_char = [
w, w, r, r, r, w, w, w,
w, w, r, r, r, w, w, w,
w, w, w, r, w, w, w, w,
w, w, r, r, r, w, w, w,
w, w, w, r, w, w, w, w,
w, w, r, r, r, w, w, w,
w, w, r, w, r, w, w, w,
w, w, w, w, w, w, w, w,
]

sense.set_pixels(char)

def jump(event):
    if event.action == ACTION_PRESSED:
        sense.set_pixels(jump_char)
        time.sleep(0.33)
        sense.set_pixels(char)

sense.stick.direction_up = jump
