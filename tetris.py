#!/usr/bin/python3

from adventurelib import *


direction = 0


@when('turn left', context='tetris')
def turn_left():
    global direction
    direction = (direction + 1) % 4
    say('You turn left.')


@when('turn right', context='tetris')
def turn_right():
    global direction
    direction = (direction - 1) % 4
    say('You turn right.')



set_context('tetris')
start()
