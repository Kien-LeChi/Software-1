print("This program will calculate the sum, product and average of 3 numbers.")

a = float(input("Enter your first number: "))
b = float(input("Enter your second number: "))
c = float(input("Enter your third number: "))

print(f"The sum of the numbers is: {a + b + c : <.5f}")
print(f"The product of the numbers is: {a * b * c : <.5f}")
print(f"The average of the numbers is: {(a + b + c)/3 : <.5f}")