print("This program diagnose your hemoglobin level")
gen = str(input("Enter your gender (F / M): "))
if gen != 'F' and gen != 'M' : print("Invalid gender.")
val = float(input("Enter your hemoglobin value: "))
print("Your hemoglobin level is: ", end = "")
if gen == 'F' :
    if val < 117 : print("LOW")
    elif val > 155 : print("HIGH")
    else : print("NORMAL")
elif gen == 'M' :
    if val < 134 : print("LOW")
    elif val > 167 : print("HIGH")
    else : print("NORMAL")
