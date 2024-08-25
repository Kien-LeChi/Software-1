print("This program will convert medieval units into kilograms and grams.")
print("Enter your talents, pounds and lots.")
talent = float(input("Enter talents: "))
pound = float(input("Enter pounds: ")) #1 talent = 20 pounds
lot = float(input("Enter lots: ")) #1 pound = 32 lots
#1 lot = 13.3g
LotToGrams = 13.3
PoundToLot = 32
TalentToPound = 20

#Converting
TotalGrams = (talent * TalentToPound * PoundToLot * LotToGrams)
TotalGrams += pound * PoundToLot * LotToGrams
TotalGrams += lot * LotToGrams

print("The weight in modern units:")
print(f"{int(TotalGrams / 1000)} kilograms and {TotalGrams % 1000 :.2f} grams.")



