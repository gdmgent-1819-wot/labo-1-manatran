from sense_hat import SenseHat
from random import randint
import time

sense = SenseHat()

pixel = 0

while pixel < 8:
    i=0
    while i < 8:
        if i < 8: 
            sense.set_pixel(i, pixel, [randint(0,255), randint(0,255), randint(0,255)])
            time.sleep(0.2)
            sense.clear()
            i+=1
    pixel+=1
    if pixel > 7 : pixel = 0
