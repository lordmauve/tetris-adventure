#!/usr/bin/python3

from adventurelib import *


direction = 0
height = 8


def drop():
    """Reduce the distance to the blocks."""
    global height
    height -= 1
    if height == 1 and get_context() == 'stuck':
        say('You feel a pang of fear.')


@when('turn left', context='tetris')
def turn_left():
    global direction
    drop()
    direction = (direction + 1) % 4
    say('You turn left.')
    look()


@when('turn right', context='tetris')
def turn_right():
    global direction
    drop()
    direction = (direction - 1) % 4
    say('You turn right.')
    look()


@when('look', context='tetris')
@when('look', context='stuck')
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
            'awareness drifts back to you. Youare in your bedroom, your sheets'
            'moist with quickly cooling sweat.'
        )
        set_context(None)
    else:
        say('You try, but you are stuck.')

@when('wake up', context='tetris')
@when('wake', context='tetris')
def wake_up():
    set_context(None)


bedroom = Room("""Your bedroom is a mess, just as you left it. A SNES running TETRIS™ sits in the corner""")
bedroom.name = "bedroom"
living_room = Room("""Austere swedish furniture fills this room. TETRIS™ posters and other merchendise decorates the walls.""")
living_room.name = "living room"
street = Room("""It is dark, a taxi is waiting""")
street.name = "outside"

bedroom.south = living_room
living_room.south = street

current_room = bedroom


@when("look around")
@when("look")
@when("l")
def look_around():
    say("You are in the {}".format(current_room.name))
    say(current_room.description)
    for exit in current_room.exits():
        destination = current_room.exit(exit)
        say("The {} is to the {}".format(destination.name, exit))


@when("n", exit="north")
@when("s", exit="south")
@when("w", exit="east")
@when("e", exit="west")
@when("north", exit="north")
@when("south", exit="south")
@when("east", exit="east")
@when("west", exit="west")
@when("go EXIT")
def move(exit):
    global current_room

    destination = current_room.exit(exit)

    if destination:
        say("You walk {} to the {}".format(exit, destination.name))
        current_room = destination
        say(current_room.description)
    else:
        say("You cannot move {}".format(exit))



set_context('tetris')
start()

