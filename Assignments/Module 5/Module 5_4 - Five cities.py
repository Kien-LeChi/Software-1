print("This program will ask you to enter 5 cities name, "
      "and will output them one by one, one per line.")

CityList = []
for i in range(1, 6) :
    city = input(f"Enter city {i} name: ")
    CityList.append(city)
for i in CityList :
    print(i)