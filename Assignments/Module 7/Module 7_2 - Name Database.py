print("This program will save all the names you enter, each name once.")

NameSet = set()
while True:
    names = input("Enter a name (Or an empty string to stop): ")
    if names == '' : break

    if names in NameSet:
        print("Existing name.")
    else :
        print("New name.")
        NameSet.add(names)

for names in NameSet:
    print(names)