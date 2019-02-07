from adventurelib import *

direction = 0
height = 8


def drop():
    """Reduce the distance to the blocks."""
    global height
    height -= 1
    if height == 1 and get_context() == 'stuck':
        say('You feel a pang of fear.')


@when('turn left', context='dream')
def turn_left():
    global direction
    drop()
    direction = (direction + 1) % 4
    say('You turn left.')
    look()


@when('turn right', context='dream')
def turn_right():
    global direction
    drop()
    direction = (direction - 1) % 4
    say('You turn right.')
    look()


@when('look', context='dream')
@when('look', context='stuck')
@when('l', context='tetris')
@when('l', context='stuck')
def look():
    global height
    drop()
    if direction % 2:
        say('You see a wall.')
    elif direction == 0:
        say(
            'You see a random assortment of blocks' +
            (
                ', stuck to you.',
                '. They are close now.',
                '. They are growing closer.',
                ', some distance away.',
            )[(height // 3 + 1) if height > 0 else 0]
        )
    else:
        say('You see the sky.')

    if height == 0:
        if get_context() == 'tetris':
            set_context('stuck')
            say(
                "You make contact with the blocks, awkwardly, just "
                "missing a convenient gap. You stick, suddenly and firmly, "
                "become trapped."
            )
            height = 3
        else:
            stuck()


@when('turn left', context='stuck')
@when('turn right', context='stuck')
@when('forward', context='stuck')
def stuck():
    global direction
    drop()
    if height <= 0:
        say(
            'You awake with a start, confused. After some seconds, your '
            'awareness drifts back to you. You are in your bedroom, your '
            'sheets moist with quickly cooling sweat.'
        )
        set_context('awake')
    else:
        say('You try, but you are stuck.')


@when('wake up', context='dream')
@when('wake', context='dream')
def wake_up():
    set_context('awake')

