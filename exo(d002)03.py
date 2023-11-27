import random

class HotBeverage:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

class EmptyCup(HotBeverage):
    def __init__(self):
        super().__init__("empty cup", 0.90, "An empty cup?! Gimme my money back!")

class BrokenMachineException(Exception):
    def __init__(self):
        super().__init__("This coffee machine has to be repaired.")

class CoffeeMachine:
    def __init__(self):
        self.drinks_served = 0
        self.broken = False

    def repair(self):
        print("Repairing the coffee machine...")
        self.drinks_served = 0
        self.broken = False

    def serve(self, beverage):
        if self.broken:
            raise BrokenMachineException()

        self.drinks_served += 1
        if self.drinks_served >= 10:
            print("The coffee machine is now broken!")
            self.broken = True
            raise BrokenMachineException()

        if random.choice([True, False]):
            print(f"Serving {beverage.name}...")
            return beverage
        else:
            print("Oops! The coffee machine served an empty cup.")
            return EmptyCup()

# Exemple d'utilisation
coffee_machine = CoffeeMachine()

try:
    while True:
        drink = coffee_machine.serve(HotBeverage("Coffee", 1.50, "Delicious coffee"))
        print(f"You got a {drink.name} for {drink.price}. Enjoy!\n")
except BrokenMachineException:
    print("The coffee machine is broken. Time to repair it!")
    coffee_machine.repair()
