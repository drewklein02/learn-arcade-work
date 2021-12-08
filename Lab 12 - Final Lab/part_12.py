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
    room = Room("You are in a small entrance room with a little bench and doors in the west, north,\n"
                " and east sides.", 2, None, 3, 1)
    room_list.append(room)
    room = Room("You are in a messy mudroom with a dirty floor but surprisingly clean walls,"
                "\nwith doors to your west and east.", None, None, 0, 9)
    room_list.append(room)
    room = Room('You are in a long hallway with good conditioning and old pictures on the walls,\n'
                'with doors on every side but east.', 6, 0, 8, None)
    room_list.append(room)
    room = Room("You are in a huge living room with green leather furniture, colored carpet,\n"
                " and abstract art.There are doors on the north and east side.\n", 4, None, None, 0)
    room_list.append(room)
    room = Room(
        "You are in a dining room with impressively well made wood table and \n"
        "chairs with wide windows that look out to the back yard. You have \n"
        "doors on the south and east side.", None, 3, None, 5)
    room_list.append(room)
    room = Room("You are in a kitchen with white cabinets and new appliances,\n"
                "stone floors and granite counter tops.You only have two doors \n"
                "on the east and west side.", None,
                None, 4, 6)
    room_list.append(room)
    room = Room("You are in a fire place room with red furniture and a wide glass door\n"
                " overlooking the deck.You can go north to the deck or west to the kitchen.", 7, 2, 5, None)
    room_list.append(room)
    room = Room("You are on a well made red wood deck that overlooks the pool\n "
                "and backyard, you can see the trees in the distance.\nYou can "
                "go out into the yard or back in the house.", 13, 6, None, None)
    room_list.append(room)
    room = Room("You are in a small bathroom with a clean but clogged toilet.\n"
                " You can only exit to the east to the hallway.", None, None, None, 2)
    room_list.append(room)
    room = Room("You are at the bottom of a long narrow stairwell with a \n"
                "chandelier and pictures on the wall.", None, None, 1, None)
    room_list.append(room)
    room = Room("You have used the stairs and entered the study that \n"
                "displays a globe and a old desk.There is a door to the east \n"
                "and the north.", 11, None, 9, 12)
    room_list.append(room)
    room = Room("You are in a old musty maintenance room with a mop and a plunger.\n "
                "There are no other doors.", None, 10, None, None)
    room_list.append(room)
    room = Room("You have entered the Library with tons of books that cover the walls.\n "
                "There is a view of the back yard, it has a pool, shed and firm fence.", None, None, 10, None)
    room_list.append(room)
    room = Room("You have entered the backyard, perfectly cut grass, a beautiful\n"
                " blue water pool to the east,a huge shed to the north, and a \n"
                "fence to the west.", None, 7, 16, 14)
    room_list.append(room)
    room = Room("You are running jumping very high and splash, you jumped in the pool,\n"
                " the water is cool, but feels refreshing. You can exit on any side.", 13, 13, 13, 13)
    room_list.append(room)
    room = Room("You have entered the shed, there are many tools, such as a shovel\n "
                "and an axe. You only have one exit.", None, 13, None, None)
    room_list.append(room)
    room = Room("You have approached the sturdy wooden fence. This may be your way \n "
                "out but you need something to get through the fence.", 13, 13, None, 13)
    room_list.append(room)
    item = Item("There is a old dirty piece of paper on the book shelf with the\n"
                " numbers 2387 on the back of it.", 3, "paper")
    item_list.append(item)
    item = Item("The plunger is dirty and sitting in the corner\n"
                " with a broken handle.", 11, "plunger")
    item_list.append(item)
    item = Item("You found a rusty old key, that seems to have been sitting in\n "
                "water for a long time.", 8, "key")
    item_list.append(item)
    item = Item("The shiny new axe is leaning against a log that seems to\n "
                "have never been used.", 15, "axe")
    item_list.append(item)
    item = Item("There is a book on the shelf called Understanding Analysis", 3, "book")
    item_list.append(item)
    item = Item("The mop is wet and hanging on a hook that looks like a pain\n "
                "to carry around", 11, "mop")
    item_list.append(item)
    item = Item("There shovel with a broken handle is leaning against\n "
                "the wall.", 15, "shovel")
    item_list.append(item)

    current_room = 0
    current_item = 0

    done = False
    print("Welcome to Escape room, move around the house, collect items, have fun\n"
          "and try to escape!")
    while not done:
        print()
        print(room_list[current_room].description)
        print()
        for item in item_list:
            if item.room_number == current_room:
                if item.name != "key":
                    print(item.description)
                    print()
        my_result = input("What do you want to do? ")
        print()
        command_words = my_result.split(" ")

        if command_words[0] == "north" or command_words[0] == "n":
            next_room = room_list[current_room].north
            if next_room is None:
                print("No door")
            else:
                current_room = next_room

        if command_words[0] == "south" or command_words[0] == "s":
            next_room = room_list[current_room].south
            if next_room is None:
                print("No door")
            else:
                current_room = next_room

        if command_words[0] == "west" or command_words[0] == "w":
            next_room = room_list[current_room].west
            if next_room is None:
                print("No door")
            else:
                current_room = next_room

        if command_words[0] == "east" or command_words[0] == "e":
            next_room = room_list[current_room].east
            if next_room is None:
                print("No door")
            else:
                current_room = next_room
        if command_words[0] == "get":
            found = False
            for item in item_list:
                if command_words[1] == item.name:
                    if item.room_number == current_room:
                        item.room_number = -1
                        found = True
                        print("You picked up the", item.name)
                    else:
                        print("This item is not here.")
                if not found:
                    print("This item is not here.")
        if command_words[0] == "inventory" or command_words[0] == "i":
            has = False
            for item in item_list:
                if item.room_number == -1:
                    print("You are holding", item.name)
                    has = True
            if not has:
                print("You don't have anything")
        if command_words[0] == "drop" or command_words[0] == "d":
            drop = False
            for item in item_list:
                if command_words[1] == item.name:
                    item.room_number = 0
                    drop = True
                    print("You dropped the", item.name)
            if not drop:
                print("You do not have this item.")
        if command_words[0] == "use" or command_words[0] == "u":
            lock = False
            if command_words[1] == "paper":
                if current_room == 9:
                    if item_list[0].room_number == -1:
                        room_list[9].east = 10
                        lock = True
                        print("You unlocked the stairs")
                    else:
                        print("You do not have the paper.")
        if command_words[0] == "use" or command_words[0] == "u":
            lock = False
            if command_words[1] == "plunger":
                if current_room == 8:
                    if item_list[1].room_number == -1:
                        item_list[2].room_number = -1
                        lock = True
                        print("You collected the key")
                    else:
                        print("Find the key.")
        if command_words[0] == "use" or command_words[0] == "u":
            lock = False
            if command_words[1] == "key":
                if current_room == 13:
                    if item_list[2].room_number == -1:
                        room_list[13].north = 15
                        lock = True
                        print("You unlocked the shed")
                    else:
                        print("You do not have the key.")
        if command_words[0] == "use" or command_words[0] == "u":
            lock = False
            if command_words[1] == "axe":
                if current_room == 16:
                    if item_list[3].room_number == -1:
                        lock = True
                        done = True
                        print("You escaped, congratulations!!")
                    else:
                        print("You do not have the axe.")
        if command_words[0] == "quit" or command_words[0] == "q":
            done = True


main()
