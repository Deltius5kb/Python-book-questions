file = open("students.txt", "a")

x = True

while x:
    username = input("username")
    firstname = input("firstname")
    surname = input("surname")
    gender = input("gender")
    year = input("year")
    end = input("end?")
    if end == "end": x = False

    file.write(username)
    file.write(", ")
    file.write(firstname)
    file.write(", ")
    file.write(surname)
    file.write(", ")
    file.write(gender)
    file.write(", ")
    file.write(year)
    file.write("\n")

file.close()