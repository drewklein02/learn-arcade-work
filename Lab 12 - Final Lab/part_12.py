import lab_12_items
import lab_12_rooms


def main():
    lab_12_rooms.create_rooms()
    lab_12_items.create_items()
    room_list = lab_12_rooms.create_rooms()
    item_list = lab_12_items.create_items()

    current_room = 0

    done = False
    print("Welcome to Escape room, move around the house, collect items, have fun\n"
          "and try to escape! Use the commands, east, west, north, and south to \n"
          "travel. Use the commands get and use to interact with items.")
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
            for item in item_list:
                if command_words[1] == item.name:
                    if item.room_number == current_room:
                        item.room_number = -1
                        print("You picked up the", item.name)
                    else:
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
            if command_words[1] == "paper":
                if current_room == 9:
                    if item_list[0].room_number == -1:
                        room_list[9].east = 10
                        print("You unlocked the stairs")
                    else:
                        print("You do not have the correct item.")
        if command_words[0] == "use" or command_words[0] == "u":
            if command_words[1] == "plunger":
                if current_room == 8:
                    if item_list[1].room_number == -1:
                        item_list[2].room_number = -1
                        print("You collected the key")
                    else:
                        print("Find the key.")
        if command_words[0] == "use" or command_words[0] == "u":
            if command_words[1] == "key":
                if current_room == 13:
                    if item_list[2].room_number == -1:
                        room_list[13].north = 15
                        print("You unlocked the shed")
                    else:
                        print("You do not have the key.")
        if command_words[0] == "use" or command_words[0] == "u":
            if command_words[1] == "axe":
                if current_room == 16:
                    if item_list[3].room_number == -1:
                        done = True
                        print("You escaped, congratulations!!")
                    else:
                        print("You do not have the axe.")
        if command_words[0] == "quit" or command_words[0] == "q":
            done = True


main()
