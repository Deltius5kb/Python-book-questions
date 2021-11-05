#Q1

aList = []
aList.append('apple')
bList = [0] * 20

cList = aList + bList
lastC = cList.pop()

print(aList, bList, cList, lastC)