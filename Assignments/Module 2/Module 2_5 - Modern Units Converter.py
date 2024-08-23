tal = float(input("Enter talents: "))
pnd = float(input("Enter pounds: ")) + 20 * tal
lot = float(input("Enter lots: ")) + 32 * pnd
lot = lot * 13.3
print(f"The weight in modern units:\n{int(lot / 1000)} kilograms and {lot % 1000 : <.5f} grams")
