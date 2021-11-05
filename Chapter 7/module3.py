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

##[
##['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
##[6, 7, 10, 13, 17, 20, 22, 21, 19, 14, 10, 7]
##[3, 3, 4, 6, 9, 12, 14, 14, 12, 9, 6, 3]
##]

maxTemps = sorted(monthsMaxMin, key=lambda x:x[1], reverse = True)
minTemps = sorted(monthsMaxMin, key=lambda x:x[1])

for i in range(6):
    print(maxTemps[i])

print('''
---------------
''')
for i in range(6):
    print(minTemps[i])

