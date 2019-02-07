#!/usr/bin/python3

import random
import adventurelib
from adventurelib import *
import _dream

def when(*args, **kwargs):
    return adventurelib.when(*args, **{'context': 'awake', **kwargs})



TETRIS = "TETRIS™"

Room.has_tetris = False
bedroom = Room("""Your bedroom is a mess, just as you left it. A SNES running TETRIS™ sits in the corner""")
bedroom.name = "bedroom"
bedroom.has_tetris = True
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


skill = 0
MAX_SKILL = 3

def improve():
    global skill
    skill = min(MAX_SKILL, skill + 1)


@when("play tetris")
def play_tetris():
    if not current_room.has_tetris:
        say(f'There is no {TETRIS} here.')
        return
    score = random.randint(1000, 10000 * 10 ** skill)
    time = (
        'a few minutes',
        'some time',
        'half an hour',
        'the best part of an hour',
    )[skill]
    adjective = (
        'terrible',
        'mediocre',
        'solid',
        'seriously good',
    )[skill]

    say(
        f'You spend {time} playing {TETRIS}. You get a {adjective} score '
        f'of {score} points.'
    )


set_context('dream')
start()

