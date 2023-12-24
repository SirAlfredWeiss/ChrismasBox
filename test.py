import random

matrix = []

used_star_positions = set()  # Set zum Speichern der bereits verwendeten Sternpositionen

for i in range(100):
    sublist = []

    while True:
        star_position = random.randint(0, 99)  # Zufällige Position für den Stern in der Zeile

        if star_position not in used_star_positions:
            used_star_positions.add(star_position)
            break
    print(star_position)
    for j in range(100):
        if j == star_position:
            sublist.append("*" + str(random.randint(1, 10)) + "*")  # Zahl mit "*" am Anfang und Ende
        else:
            number = str(random.randint(1, 1000))
            if random.choice([True, False]):  # Zufällig entscheiden, ob der Stern davor oder danach platziert wird
                sublist.append(number + "*")
            else:
                sublist.append("*" + number)

    matrix.append(sublist)

# Schreiben der Matrix in eine Textdatei
with open("matrix.txt", "w") as file:
    for sublist in matrix:
        file.write(" ".join(sublist) + "\n")

# Drucken der Positionen der Zahlen mit "*" am Anfang und Ende in jeder Zeile
for i, sublist in enumerate(matrix):
    star_position = sublist.index("*")
    print("In Zeile", i, "an Position", star_position)

print("Matrix in matrix.txt geschrieben")