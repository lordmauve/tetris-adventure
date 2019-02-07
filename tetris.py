#!/usr/bin/python3

from adventurelib import *
import _dream

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

person1 = Item("Gary")
person2 = Item("Steve")
person3 = Item("John")

convention_center.people = Bag()
convention_center.people.add(person1)
convention_center.people.add(person2)
convention_center.people.add(person3)

@when("look around")
@when("look")
@when("l")
def look_around():
    say("You are in the {}".format(current_room.name))
    say(current_room.description)
    for exit in current_room.exits():
        destination = current_room.exit(exit)
        say("The {} is to the {}".format(destination.name, exit))
    if hasattr(current_room, "people"):
        people_in_room = [p.name for p in current_room.people]
        say("There are {} people here. There is {}".format(len(people_in_room), ",".join(people_in_room)))



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

