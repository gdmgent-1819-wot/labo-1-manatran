from sense_hat import SenseHat
import time
from random import randint

sense = SenseHat()

letters = input("enter a string") or "NMD"
interval = input("enter an interval") if type(input("enter an interval")) == int else 1

while True:
    for letter in letters:
        sense.show_letter(letter, text_colour=[randint(0,255), randint(0,255), randint(0,255)])
        time.sleep(int(interval))
