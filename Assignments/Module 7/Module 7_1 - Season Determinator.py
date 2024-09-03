print("This program will determine which season your month is.")

seasons = ('winter', 'spring', 'summer', 'autumn')

month = int(input("Please enter a month: "))
if month == 12 : month = 0
print(f"Month {month} is equivalent to {seasons[int(month/3)]}.")