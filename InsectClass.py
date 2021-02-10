# Create a class for an insect object. It should have 2 attributes – wings and legs. For now, the insect object has 2 wings and 4 legs. It should also have 1 method – to determine the length of flight. Length of flight should be a method that randomly assigns a number between 1 and 10 miles. Create a python program that will create an instance of the insect class and print out how many miles the insect can fly#
import random

##2/10/2021##


class Insects:
    def __init__(self):
        # This is where you define all your attributes.
        self.__wings = 2
        self.__legs = 4
        self.__flight_length = 0

    # Even though flight length was initialized at 0, you can change it in this
    # function!
    def __flight_length(self):
        self.__flight_length = random.randrange(1, 10)
        return self.__flight_length

    def __str__(self):
        return (
            "wings: "
            + str(self.__wings)
            + "\n"
            + "legs: "
            + str(self.__legs)
            + "\n"
            + "flight length: "
            + str(self.__flight_length)
        )
