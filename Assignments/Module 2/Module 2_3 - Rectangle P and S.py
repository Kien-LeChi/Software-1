print("This program will calculate the area and perimeter of a rectangle")

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

print(
    f"The perimeter of the rectangle is {2 * (length + width):.5f}\n"
    f"The area of the rectangle is {width * length:.5f}"
    )
