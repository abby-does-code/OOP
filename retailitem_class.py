class RetailItem:
    def __init__(self, descrip, inv, price):
        self.__item_description = descrip
        self.__units_in_inventory = inv
        self.__price = price

    def __str__(self):  #this method displays the object's state
        return (
            "ITEM DESCRIPTION: "
            + str(self.__item_description)
            + "\n"
            + "UNITS IN INVENTORY: "
            + str(self.__units_in_inventory)
            + "\n"
            + "PRICE: "
            + "$"
            + format(self.__price, '.2f')
            + "\n"
        )