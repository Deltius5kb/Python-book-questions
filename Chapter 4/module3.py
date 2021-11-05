#Q3

while (True):
    count = 0
    code = input("Enter the 5 digit product code: ")
    letters = code[0:2]
    numbers = code[2:5]

    while letters == 'AB' and numbers[1] == 0 and numbers[2]:
        count += 1

    print(count)

