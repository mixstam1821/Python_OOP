from coffee_maker import Coffee_info, Coffee_maker
from money_counter import Money_counter


class main:



    def __init__(self):
        self.coffee_maker = Coffee_maker()
        self.coffee_payment = Money_counter()
        self.coffee_info = Coffee_info()
        self.coffeeChoice()

    def coffeeChoice(self):
        print("""       (  )   (   )  )
                          ) (   )  (  (
                          ( )  (    ) )
                          _____________
                         <_____________> ___
                        |             |/ _ \
                        |               | | |
                        |               |_| |
                     ___|             |\___/
                    /    \___________/    \
                    \_____________________/""")
        print("Welcome to the coffee shop we have\n 1.Latte \n 2.Espresso\n 3.Arabica \n")
        choice = int(input("which one will you choose?\n"))
        if choice == 1:
            self.latteChoice()
        elif choice == 2:
            self.espressoChoice()
        elif choice == 3:
            self.arabicaChoice()
        else:
            print("Sorry, we do not sell that type of coffee")
            self.coffeeChoice()

    def latteChoice(self):
        latte_choice = int(input("You have chosen Latte \n 1. Latte Info \n 2. Buy Latte \n 3. Back to Choice\n"))
        if latte_choice == 1:
            self.coffee_info.latteInfo()
            self.latteChoice()
        elif latte_choice == 2:
            self.coffee_maker.latteMaker()
            self.coffee_payment.input_money(1)
        elif latte_choice == 3:
            self.coffeeChoice()
        else:
            print("Command unknown")
            self.coffeeChoice()

    def espressoChoice(self):
        espresso_choice = int(input(
            "You have chosen Espresso \n 1. Espresso Info \n 2. Buy Espresso \n 3. Back to Choice\n"))
        if espresso_choice == 1:
            self.coffee_info.espressoInfo()
            self.espressoChoice()
        elif espresso_choice == 2:
            self.coffee_maker.espressoMaker()
            self.coffee_payment.input_money(2)
        elif espresso_choice == 3:
            self.coffeeChoice()
        else:
            print("Command unknown")
            self.coffeeChoice()

    def arabicaChoice(self):
        arabica_choice = int(input("You have chosen Arabica \n 1. Arabica Info \n 2. Buy Arabica \n 3. Back to Choice\n"))
        if arabica_choice == 1:
            self.coffee_info.arabicaInfo()
            self.arabicaChoice()
        elif arabica_choice == 2:
            self.coffee_maker.arabicaMaker()
            self.coffee_payment.input_money(3)
        elif arabica_choice == 3:
            self.coffeeChoice()
        else:
            print("Command unknown")
            self.coffeeChoice()


start = main()

