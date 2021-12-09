class Room:
    def __init__(self, description, north, south, west, east):
        self.description = description
        self.north = north
        self.south = south
        self.west = west
        self.east = east


def create_rooms():
    room_list = []
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
    return room_list
