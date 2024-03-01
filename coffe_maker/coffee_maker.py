from coffee_data import coffee_info, resources


class Coffee_info:

    def __init__(self):
       pass


    def latteInfo(self):
        """Grabs Lattee Info from coffee_data.py"""
        print(coffee_info["latte"]["info"], end="\n")
        print(f"The price is: {coffee_info['latte']['price']}")

    def espressoInfo(self):
        """Grabs espresso Info from coffee_data.py"""
        print(coffee_info["espresso"]["info"], end="\n")
        print(f"The price is: {coffee_info['espresso']['price']}")

    def arabicaInfo(self):
        """Grabs arabica Info from coffee_data.py"""
        print(coffee_info["arabica"]["info"], end="\n")
        print(f"The price is: {coffee_info['arabica']['price']}")


class Coffee_maker:

    def __init__(self):
       pass

    def latteMaker(self):
        latte = coffee_info["latte"]["cost"]
        if (resources["milk"] < latte["milk"]) or (resources["water"] < latte["water"]) or (
                resources["sugar"] < latte["sugar"]) or (resources["coffee"] < latte["coffee"]):
            print("Sorry, we do not have enough resources")
            return
        resources["milk"] -= latte["milk"]
        resources["water"] -= latte["water"]
        resources["sugar"] -= latte["sugar"]
        resources["coffee"] -= latte["coffee"]

    def espressoMaker(self):
        espresso = coffee_info["espresso"]["cost"]
        if (resources["milk"] < espresso["milk"]) or (resources["water"] < espresso["water"]) or (
                resources["sugar"] < espresso["sugar"]) or (resources["coffee"] < espresso["coffee"]):
            print("Sorry, we do not have enough resources")
            return
        resources["milk"] -= espresso["milk"]
        resources["water"] -= espresso["water"]
        resources["sugar"] -= espresso["sugar"]
        resources["coffee"] -= espresso["coffee"]

    def arabicaMaker(self):
        arabica = coffee_info["arabica"]["cost"]
        if (resources["milk"] < arabica["milk"]) or (resources["water"] < arabica["water"]) or (
                resources["sugar"] < arabica["sugar"]) or (resources["coffee"] < arabica["coffee"]):
            print("Sorry, we do not have enough resources")
            return
        resources["milk"] -= arabica["milk"]
        resources["water"] -= arabica["water"]
        resources["sugar"] -= arabica["sugar"]
        resources["coffee"] -= arabica["coffee"]
