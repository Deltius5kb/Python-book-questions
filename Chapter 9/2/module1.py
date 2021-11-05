f = open("students.txt", "r")


for line in f:
    field = line.split(", ")
    if field[3] == "f" and field[4] == "10":
        print(field[2] + " " + field[1])

f.close()