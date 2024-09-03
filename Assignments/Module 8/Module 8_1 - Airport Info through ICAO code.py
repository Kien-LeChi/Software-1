import mysql.connector

print("This program will give you every airport's information based on your"
      " entered ICAO codes.")

connection = mysql.connector.connect(
    user = 'root',
    password = '1234',
    database = 'flight_game',
    collation = 'utf8mb3_general_ci',
    autocommit = True
)
cursor = connection.cursor()

ICAO = input("Enter your ICAO code: ")
#select name, municipality from airport where ident = '{ICAO}';
query = f"select name, municipality from airport where ident = '{ICAO}'"
cursor.execute(query)
answer = cursor.fetchall()
print(f"The name of the airport is {answer[0][0]} and it is stationed in {answer[0][1]}")
