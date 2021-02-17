import retailitem_class as retail


item1 = retail.RetailItem("jacket", 12, 59.95)

item2 = retail.RetailItem("Designer Jeans", 40, 34.95)
item3 = retail.RetailItem("Shirt", 20, 24.95)


print(item1.__str__())
print(item2.__str__())
print(item3.__str__())
