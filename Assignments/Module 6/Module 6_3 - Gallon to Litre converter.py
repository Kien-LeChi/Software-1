print("This program will convert gallons to litres.")

def GallonToLitre(gallon) :
    GallonInLitre = 3.78541
    return gallon * GallonInLitre #--> Liter

while True :
    try :
        UserGallon = float(input("Enter a gallon value (Or a negative value to exit): "))
        if(UserGallon < 0) : break;
        print(f"{UserGallon} gallon(s) is {GallonToLitre(UserGallon) :.2f} litre(s).")
    except :
        print(f"Please enter a float value")
