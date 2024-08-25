print("This program will determine which pizza is cheaper based on "
      "its unit price per square meter")

import math

def PizzaUnitPrice(diameter, price) :
    radius = diameter / 2 / 100 #radius = diameter / 2 and / 100 for unit conversion
    area = radius ** 2 * math.pi
    return price / area

PizzaDiameter1 = float(input("Enter the diameter of the first pizza (in cm): "))
PizzaPrice1 = float(input("Enter the price of the first pizza: "))

PizzaDiameter2 = float(input("Enter the diameter of the second pizza (in cm): "))
PizzaPrice2 = float(input("Enter the price of the second pizza: "))

UnitPrice1 = PizzaUnitPrice(PizzaDiameter1, PizzaPrice1)
UnitPrice2 = PizzaUnitPrice(PizzaDiameter2, PizzaPrice2)

if UnitPrice1 < UnitPrice2 :
    print("The first pizza has lower unit price.")
else :
    print("The second pizza has lower unit price.")