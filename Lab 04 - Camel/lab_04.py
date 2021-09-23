import random


def main():
    print("Welcome to Camel!")
    print("You have stolen a camel to make your way across the Mobi desert")
    print("The natives want their camel back and are chasing you down! Survive you")
    print("desert trek and outrun the natives.")
    done = False
    miles_traveled = 0
    thirst = 0
    camel_tiredness = 0
    natives_traveled = -20
    drinks_in_canteen = 3
    while not done:
        print()
        print("A. Drink from your canteen.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop for the night.")
        print("E. Status check.")
        print("Q. Quit.")
        user_choice = input("What is your choice? ")
        if user_choice.upper() == "Q":
            done = True
            print("Thanks for playing")

        elif user_choice.upper() == "E":
            print("Miles Traveled:", miles_traveled)
            print("Drinks in Canteen:", drinks_in_canteen)
            print("The natives are", miles_traveled - natives_traveled, "behind you.")

        elif user_choice.upper() == "D":
            camel_tiredness = 0
            print("The camel is happy!")
            natives_traveled += random.randrange(7, 14)
            print("The natives got", miles_traveled - natives_traveled, "closer.")

        elif user_choice.upper() == "C":
            miles_traveled += random.randrange(10, 20)
            print("You have traveled", miles_traveled , "miles")
            camel_tiredness += random.randrange(1, 3)
            thirst += 1
            natives_traveled += random.randrange(7, 14)

        elif user_choice.upper() == "B":
            miles_traveled += random.randrange(5, 12)
            print("You have traveled", miles_traveled, "miles")
            thirst += 1
            camel_tiredness += 1
            natives_traveled += random.randrange(7, 14)

        elif user_choice.upper() == "A":
            if drinks_in_canteen > 0:
                drinks_in_canteen -= 1
                print("That was good")
            else:
                print("You don't have any drinks")

        if thirst > 6 and not done:
            done = True
            print("You died of thirst.")
        elif thirst > 4 and not done:
            print("You are thirsty")

        if camel_tiredness > 8 and not done:
            print("Your camel is dead.")
            done = True
        elif camel_tiredness > 5 and not done:
            print("Your camel is getting tired.")

        if miles_traveled - natives_traveled < 15 and not done:
            print("The natives are getting close!")
        elif miles_traveled - natives_traveled < 0 and not done:
            print("The natives caught up")
            done = True


        if miles_traveled > 200:
            print("You won the game")
            done = True


main()
