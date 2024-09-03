import mysql.connector

print("You need to provide a country code for this program, "
      "and it will provide you with all airports' info.")

connection = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "1234",
    database = "flight_game",
    collation = "utf8mb3_general_ci",
    autocommit = True,
)

cursor = connection.cursor()

CountryCode = input("Please enter your country code: ")
#All Airports and search country through Country Code query
AirportQuery = f"select name, type from airport where iso_country = '{CountryCode}' and type != 'closed' order by type desc"
CountryQuery = f"select name from country where iso_country = '{CountryCode}'"
#
cursor.execute(AirportQuery)
AllAirports = cursor.fetchall()

cursor.execute(CountryQuery)
CountryName = cursor.fetchone()

for i in range(len(AllAirports)) :
    print(f"{i+1:>3}. {AllAirports[i][0] :>50} : {AllAirports[i][1] : <}")
print(f"{CountryName[0]} has {len(AllAirports)} airports in total.  \n", end = '')
