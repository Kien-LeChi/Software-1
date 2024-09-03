print("This program is mainly designed for fetching and storing "
      "airports' data.")

AirportDatabase = dict({})

while True:
    #User choice
    print("Do you want to:\n"
          "1. Fetch an airport data\n"
          "2. Store a new airport data\n"
          "3. Exit\n")

    UserOption = input("Enter your choice: ")
    #End user choice

    try : #User input is an integer
        UserOption = int(UserOption)
        if UserOption == 1: #Fetching data---------------------------------------------

            AirportICAOCode = input("Please enter the airport ICAO code: ")
            print(f"Here is the corresponding airport: {AirportDatabase[AirportICAOCode]}")

        elif UserOption == 2: #Store new data------------------------------------------

            print("Please enter the airport name and ICAO code.")

            newAirportName = input("Airport name: ")
            newAirportICAOCode = input("ICAO code: ")

            AirportDatabase[newAirportICAOCode] = newAirportName

        elif UserOption == 3: #Quit----------------------------------------------------

            print("Successfully exited the program. See you next time!")
            break

    except : #User input is an integer
        print("Invalid choice.")
