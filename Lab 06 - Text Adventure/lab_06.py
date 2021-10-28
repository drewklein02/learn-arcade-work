class Room:
    def __init__(self, description, north, south, west, east):
        self.description = description
        self.north = north
        self.south = south
        self.west = west
        self.east = east


def main():
    room_list = []
    room = Room("You are in a small entrance room with a little bench and doors in the west, north,"
                " and east sides.", 2, None, 3, 1)
    room_list.append(room)
    room = Room("You are in a messy mudroom with a dirty floor but surprisingly clean walls,"
                "\nwith only one door to your west.", None, None, 0, None)
    room_list.append(room)
    room = Room('You are in a long hallway with good conditioning and old pictures on the walls,'
                '\nwith doors on every side but east.', 6, 0, 8, None)
    room_list.append(room)
    room = Room("You are in a huge living room with green leather furniture, colored carpet,"
                " and abstract art.\nThere are doors on the north and east side.", 4, None, None, 0)
    room_list.append(room)
    room = Room(
        "You are in a dining room with impressively well made wood table and chairs with wide windows that look "
        "out to the back yard.\n You have doors on the south and east side.", None, 3, None, 5)
    room_list.append(room)
    room = Room("You are in a kitchen with white cabinets and new appliances,"
                "stone floors and granite counter tops.\nYou only have two doors on the east and west side.", None,
                None, 4, 6)
    room_list.append(room)
    room = Room("You are in a fire place room with red furniture and a wide glass door"
                " overlooking the deck.\nYou can go north to the deck or west to the kitchen.", 7, 2, 5, None)
    room_list.append(room)
    room = Room("You are on a well made red wood deck that overlooks the pool and backyard, you can see the trees"
                " in the distance.\nYou can only go back south to the fire place room.", None, 6, None, None)
    room_list.append(room)
    room = Room("You are in a small bathroom with clean utilities.\n"
                " You can only exit to the east to the hallway.", None, None, None, 2)
    room_list.append(room)

    current_room = 0

    done = False
    while not done:
        print()
        print(room_list[current_room].description)
        my_result = input("What do you want to do? ")

        if my_result.lower() == "north" or my_result.lower() == "n":
            next_room = room_list[current_room].north
            if next_room is None:
                print("No door")
            else:
                current_room = next_room

        if my_result.lower() == "south" or my_result.lower() == "s":
            next_room = room_list[current_room].south
            if next_room is None:
                print("No door")
            else:
                current_room = next_room

        if my_result.lower() == "west" or my_result.lower() == "w":
            next_room = room_list[current_room].west
            if next_room is None:
                print("No door")
            else:
                current_room = next_room

        if my_result.lower() == "east" or my_result.lower() == "e":
            next_room = room_list[current_room].east
            if next_room is None:
                print("No door")
            else:
                current_room = next_room
        if my_result.lower() == "quit" or my_result.lower() == "q":
            done = True


main()
