class RetailItem:
    def __init__(self, descrip, inv, price):
        self.__item_description = descrip
        self.__units_in_inventory = inv
        self.__price = price

    def __str__(self):
        return (
            "ITEM DESCRIPTION: "
            + str(self.__item_description)
            + "\n"
            + "UNITS IN INVENTORY: "
            + str(self.__units_in_inventory)
            + "\n"
            + "PRICE: "
            + "$"
            + str(self.__price)
            + "\n"
        )