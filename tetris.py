#!/usr/bin/python3

from adventurelib import *
import _dream

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

