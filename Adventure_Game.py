import time

user_name = input("What's your name? ")
user_age = int(input("How old are you? "))

if user_age >= 12:
    print("Getting ready...\n")
    time.sleep(1)  # Adding delays for extra effects
    print("Please wait!")
    time.sleep(1)
    count = 0
    while count != 5:
        print(".", end="")
        time.sleep(2 / 5)
        count += 1

    print("\nHello", user_name, "! Welcome to this journey! 🏕️🏝️🏖️🏕")

    user_choice = input("\nYou find yourself on a dirt road that leads to two paths: left or right. Which way do you want to go (left/right)?: ").lower()

    if user_choice == "left":
        count = 0
        while count != 5:
            print(".", end="")
            time.sleep(2 / 5)
            count += 1
        user_choice = input("\nYou stumble upon a river. Would you like to swim across or walk around it? Type 'S' to swim across and 'W' to walk around: ").upper()

        if user_choice == "S":
            count = 0
            while count != 5:
                print(".", end="")
                time.sleep(2 / 5)
                count += 1
            print("\nYou bravely swim across but unfortunately encounter an alligator.")
        elif user_choice == "W":
            count = 0
            while count != 5:
                print(".", end="")
                time.sleep(2 / 5)
                count += 1
            print("\nYou choose to walk around the river. After many miles, you run out of water and lose the game.")
        else:
            print('Invalid option. You lose.')

    elif user_choice == "right":
        count = 0
        while count != 5:
            print(".", end="")
            time.sleep(2 / 5)
            count += 1
        user_choice = input("\nYou come across a bridge. It looks unstable. Do you want to cross it or turn back (cross/back)? ").lower()

        if user_choice == "back":
            count = 0
            while count != 5:
                print(".", end="")
                time.sleep(2 / 5)
                count += 1
            print("\nYou decide to turn back and end up losing.")
        elif user_choice == "cross":
            count = 0
            while count != 5:
                print(".", end="")
                time.sleep(2 / 5)
                count += 1
            user_choice = input("\nYou successfully cross the bridge and encounter a stranger. Would you like to engage in conversation (yes/no)? ").lower()

            if user_choice == "yes":
                count = 0
                while count != 5:
                    print(".", end="")
                    time.sleep(2 / 5)
                    count += 1
                print("\nYou talk to the stranger who rewards you with gold. Congratulations! You WIN!")
            elif user_choice == "no":
                count = 0
                while count != 5:
                    print(".", end="")
                    time.sleep(2 / 5)
                    count += 1
                print("\nYou choose to ignore the stranger, who becomes offended. You LOSE!.")
            else:
                print('Invalid option. You lose.')
        else:
            print('Invalid option. You lose.')

    else:
        print('Invalid option. You lose.')

    print("Thank you for playing", user_name, ":)")
else:
    print("\nI'm sorry :( You are not old enough to play...")
    print("\nExiting...")
    count = 0
    while count != 5:
        print(".", end="")
        time.sleep(2/5)
        count += 1
    print()
if __name__ == "__main__":
    print()
