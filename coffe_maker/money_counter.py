from coffee_data import coffee_info

class Money_counter:
    def __init__(self):
        """Constructor that accepts coffee type input so that the money counter class can work"""

    def input_money(self, type):
        """Method to input money into the machine, the money will then be processed in a private method in
        the same class."""
        dollar = float(input("Please input your 1 dollar Bill: "))*100
        quarter = (float(input("Please input your quarter [25 cents]: ")) * 25)
        dime = (float(input("Please input your dime [10 cents]: ")) * 10)
        nickel = (float(input("Please input your nickel [5 cents]: ")) * 5)
        penny = float(input("Please input your penny [1 cents]: "))

        totalmoney = dollar + quarter + dime + nickel + penny

        self.__process_money(totalmoney=totalmoney, type=type)

    def __cost_choice(self,type):
        """private Method to Determine what the coffee type is"""
        if type == 1:
            return coffee_info["latte"]["price"]
        elif type == 2:
            return coffee_info["espresso"]["price"]
        elif type == 3:
            return coffee_info["arabica"]["price"]

    def __process_money(self, totalmoney, type):
        """private method to check and calculate the return of remaining money
        it also calls private method coffee_cost to determine the cost of the
        coffee through the type"""
        coffee_cost = float(self.__cost_choice(type)*100)
        dollar = 0
        quarter = 0
        dime = 0
        nickel = 0
        penny = 0
        if coffee_cost > totalmoney:
            return
        left_over = totalmoney - coffee_cost
        if left_over == 0:
            return
        if left_over > 1:
            int(left_over)
            dollar = int(left_over/100)
            left_over = left_over - (dollar*100)
            quarter = int(left_over/25)
            left_over = left_over - (quarter*25)
            dime = int(left_over / 10)
            left_over = left_over - (dime * 10)
            nickel = int(left_over / 5)
            left_over = left_over - (nickel * 5)
            penny = int(left_over)

        print(f"Your change is:\n{dollar} dollar\n{quarter} quarter\n{dime} dime\n{nickel} nickel\n{penny} penny")

