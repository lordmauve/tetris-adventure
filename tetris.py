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

convention_center = Room("""There are a large number of people milling here. They are all here for the TETRIS™ world championships""")
convention_center.name = "convention center"

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


@when("get in taxi")
def taxi():
    global current_room
    say("The taxi ride is long and uneventful. You arrive at the convention centre with time to spare before the competition beings.")
    current_room = convention_center
    look_around()


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
        look_around()
    else:
        say("You cannot move {}".format(exit))



set_context('tetris')
start()

