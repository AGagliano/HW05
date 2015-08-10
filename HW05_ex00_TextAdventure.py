#!/usr/bin/env python
# HW05_ex00_TextAdventure.py
##############################################################################
# Imports
import sys

# Body


def infinite_stairway_room(name, count = 0):
    print "%s walks through the door to see a dimly lit hallway." % (name)
    print "At the end of the hallway is a", count * 'long ', 'staircase going towards some light'
    next = raw_input("> ")
    
    # infinite stairs option
    if next == "take stairs":
        print '%s takes the stairs' % (name)
        if (count > 0):
            print "but %s's not happy about it" % (name)
        infinite_stairway_room(name, count + 1)
    # option 2 == ?????
    if next == option_2:
        pass


def gold_room(name):
    print "This room is full of gold.  How much does %s take?" % (name)

    next = raw_input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, %s's not greedy, %s wins!" % (name, name)
        sys.exit(0)
    else:
        dead("%s greedy bastard!" % (name))


def bear_room(name):
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How is %s going to move the bear?" % (name)
    bear_moved = False

    while True:
        next = raw_input("> ")

        if next in ["take honey", "honey", "take"]:
            dead("The bear looks at %s then slaps %s's face off." % (name, name))
        elif next == "taunt" and not bear_moved:
            print "The bear has moved from the door. %s can go through it now." % (name)
            bear_moved = True
        elif next == "taunt" and bear_moved:
            dead("The bear gets pissed off and chews %s's leg off." % (name))
        elif next in ["open door", "open", "door"] and bear_moved:
            gold_room(name)
        elif next == "magic":
            infinite_stairway_room(name)
        else:
            print "I got no idea what that means."


def cthulhu_room(name):
    print "Here %s sees the great evil Cthulhu." % (name)
    print "He, it, whatever stares at %s and %s goes insane." % (name, name)
    print "Does %s flee for %s's life or eat %s's head?" % (name, name, name)

    next = raw_input("> ")

    if "flee" in next:
        main()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room(name)


def dead(why):
    print why, "Good job!"
    sys.exit(0)


##############################################################################
def main():
    # START the TextAdventure game
    name = sys.argv[1]

    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"

    next = raw_input("> ")

    if next == "left":  
        bear_room(name)
    elif next == "right":
        cthulhu_room(name)
    else:
        dead("You stumble around the room until you starve.")

if __name__ == '__main__':
    main()
