# Create a class for an insect object. It should have 2 attributes – wings and legs. For now, the insect object has 2 wings and 4 legs. It should also have 1 method – to determine the length of flight. Length of flight should be a method that randomly assigns a number between 1 and 10 miles. Create a python program that will create an instance of the insect class and print out how many miles the insect can fly#
import random

"""
class Insects:
    def __init__(self):
        self.wings = 2
        self.legs = 4

    def flight_length(self):
        self.flight_length = random.randrange(1, 10)
        return self.flight_length

    def wings(self):
        return self.wings

    def legs(self):
        return self.legs


my_bug = Insects()

print(str(my_bug.flight_length()) + str(my_bug.wings()) + str(my_bug.legs()))
"""

# Design a class that represents a cell phone. The data that should be kept as attributes in the class are as follows:The name of the phone’s manufacturer will be assigned to the __manufact attribute. The phone’s model number will be assigned to the __model attribute. The phone’s retail price will be assigned to the __retail_price attribute.
# The class will also have the following methods:An __init__ method that accepts arguments for the manufacturer, model number, and retail price.set_manufact, set_model and set_retail_price methods that accepts an argument for the manufacturer, model and retail_price respectively and can update it if neccessary. get_manufact, get_model, get_retail_price method that returns the phone’s manufacturer, model and price respectively.#


class Cellphone:
    def __init__(self):
        self.__manufact = int(input("Enter your manfacturer number: "))
        self.__model = int(input("Enter the model number: "))
        self.__retail_price = float(input("Enter the retail price: "))
