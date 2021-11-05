#Q2

nameList = []
currentName = "placeholer"
count = 0

while currentName != 'End':
    currentName = input("Please enter a name. Enter End when you are finished")
    nameList.append(currentName)
    count += 1

count /= 2
countTwo = 0
for countTwo in range(int(count)):
    print(nameList[countTwo])

nameList.pop()
print(nameList)