#!/usr/bin/python3

import curses
import time

from .common import *

pin_map = {
    'w': fwd_pin,
    'a': left_pin,
    's': back_pin,
    'd': right_pin
}

all_pins = list(pin_map.values())
all_pins.append(hard_pin)

def main(stdscr):
    current_milli_time = lambda: int(round(time.time() * 1000))

    stdscr.nodelay(1)

    lastcommand = current_milli_time()
    while True:
        # get keyboard input, returns -1 if none available
        c = stdscr.getch()
        if c != -1:
            # print numeric value
            stdscr.addstr(str(c) + ' ')
            stdscr.refresh()
            # return curser to start position
            stdscr.move(0, 0)
            char = chr(c)
            if char.lower() in pin_map:
                GPIO.output(pin_map[char.lower()], GPIO.HIGH)
            if char.isupper():
                GPIO.output(hard_pin, GPIO.HIGH)
            elif c == ord('q'):
                return
            lastcommand = current_milli_time()
        elif current_milli_time() - lastcommand > 100:
            GPIO.output(all_pins, GPIO.LOW)

    GPIO.cleanup()

if __name__ == '__main__':
    curses.wrapper(main)
