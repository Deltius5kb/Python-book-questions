monthsMaxMin =[['January', 6, 3],
['February', 7, 3],
['March', 10, 4],
['April', 13, 6],
['May', 17, 19],
['June',20, 12],
['July', 22, 14],
['August', 21, 14],
['October', 19, 12],
['November', 10, 6],
['December', 7, 3]]

monthsUnder9 = [ ]
monthsOver19 = [ ]

for i in range(11):
    if monthsMaxMin[i-1][2] < 9:
        monthsUnder9.append(monthsMaxMin[i-1])

for i in range(11):
    if monthsMaxMin[i-1][1] >= 20:
        monthsOver19.append(monthsMaxMin[i-1])

print("Months under 9 degrees celsius:")
print(monthsUnder9)
print("\n Months over or 20 degrees celsius")
print(monthsOver19)