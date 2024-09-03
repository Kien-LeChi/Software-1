print("This program will calculate the geographical distance between "
      "two airports.")

#<editor-fold desc="mySQL Connector">
import mysql.connector
connection = mysql.connector.connect(
    # host = '127.0.0.1',
    user = 'root',
    password = '1234',
    database = 'flight_game',
    collation = 'utf8mb3_general_ci',
    autocommit = True,
)
cursor = connection.cursor()
#</editor-fold>

#<editor-fold desc = "Inputs">
print("Please enter the two airports.")
ICAO = ['']*2
ICAO[0] = input("Enter the first airport: ")
ICAO[1] = input("Enter the second airport: ")
#</editor-fold>

#<editor-fold desc = "Specifying queries">
#Specifying two airports
AirportQuery = ['']*2
AirportQuery[0] = f"select name, latitude_deg, longitude_deg from airport where ident = '{ICAO[0]}'"
AirportQuery[1] = f"select name, latitude_deg, longitude_deg from airport where ident = '{ICAO[1]}'"
#</editor-fold>

#<editor-fold desc = "Executing queries">
#airport = [Name, Latitude, Longitude]
cursor.execute(AirportQuery[0])
airport_1 = cursor.fetchall()[0]

cursor.execute(AirportQuery[1])
airport_2 = cursor.fetchall()[0]
# </editor-fold>

print(f"Your two airports are '{airport_1[0]}' and '{airport_2[0]}'.", end = '\n')

#<editor-fold desc = "Calculating the distance">
from geopy.distance import geodesic

PortCoord_1 = (airport_1[1], airport_1[2])
PortCoord_2 = (airport_2[1], airport_2[2])
print(f"The distance between two airports is: {geodesic(PortCoord_1, PortCoord_2).km :.2f}km")
#</editor-fold>