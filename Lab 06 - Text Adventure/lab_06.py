class Room:
    def __init__(self, description, north, south, west, east):
        self.description = description
        self.north = north
        self.south = south
        self.west = west
        self.east = east


class Item:
    def __init__(self, description, room_number, name):
        self.description = description
        self.room_number = room_number
        self.name = name


def main():
    room_list = []
    item_list = []
    room = Room("You are in a small entrance room with a little bench and doors in the west, north,"
                " and east sides.", 2, None, 3, 1)
    room_list.append(room)
    room = Room("You are in a messy mudroom with a dirty floor but surprisingly clean walls,"
                "\nwith doors to your west and east.", None, None, 0, 9)
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
    item = Item("There is a old dirty piece of paper on the book shelf with the"
                " numbers 2387 on the back of it.", 3, "code")
    item_list.append(item)
    item = Item("There is a dirty plunger sitting in the corner"
                " with a broken handle.", 11, "plunger")
    item_list.append(item)
    item = Item("You found a rusty old key, that seems to have been sitting in "
                "water for a long time.", 8, "key")
    item_list.append(item)
    item = Item("There is a shiny new axe leaning against a log that seems to "
                "have never been used.", 15, "axe")
    item_list.append(item)
    item = Item("There is a book on the shelf called Understanding Analysis", 3, "book")
    item_list.append(item)
    item = Item("There is a wet dirty mop hanging on a hook that looks like a pain "
                "to carry around", 11, "mop")
    item_list.append(item)
    item = Item("There is a sharp shovel with a broken handle leaning against "
                "the wall.", 15, "shovel")
    item_list.append(item)

    current_room = 0
    current_item = 0

    done = False
    while not done:
        print()
        print(room_list[current_room].description)
        for item in item_list:
            if item.room_number == current_room:
                if item.name != "key":
                    print(item.description)

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
