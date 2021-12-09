class Item:
    def __init__(self, description, room_number, name):
        self.description = description
        self.room_number = room_number
        self.name = name

def create_items():
    item_list = []
    item = Item("There is a old dirty piece of paper on the book shelf with the\n"
                " numbers 2387 on the back of it. In the corner it reads ascend.", 3, "paper")
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
    return item_list