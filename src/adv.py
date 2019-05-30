from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

if __name__ == "__main__":
    p = Player(room['outside'])
    end = False
    while True:
        print(p.location.name)
        print(p.location.description)
        print()
        while True:
            direc = input("Input direction:    ")
            print()
            if direc == 'n':
                if hasattr(p.location, 'n_to'):
                    p.location = p.location.n_to
                    break
                else:
                    print("Incorrect direction")
                    print()
            elif direc == 'e':
                if hasattr(p.location, 'e_to'):
                    p.location = p.location.e_to
                    break
                else:
                    print("Incorrect direction")
                    print()
            elif direc == 's':
                if hasattr(p.location, 's_to'):
                    p.location = p.location.s_to
                    break
                else:
                    print("Incorrect direction")
                    print()
            elif direc == 'w':
                if hasattr(p.location, 'w_to'):
                    p.location = p.location.w_to
                    break
                else:
                    print("Incorrect direction")
                    print()
            elif direc == 'q':
                print("Thanks for playing!")
                end = True
                break
        if end:
            break