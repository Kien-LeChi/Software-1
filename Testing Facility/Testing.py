games = {"Monopoly", "Chess", "Cluedo"}
print(games)

games.add("Dominion")
print(games)

games.remove("Chess")
print(games)

games.add("Cluedo")
print(games)

for g in games:
    print(g)