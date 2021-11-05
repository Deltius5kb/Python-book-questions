#Q3
import random

dieOne = random.randint(1,6)
dieTwo = random.randint(1,6)
#dieOne = 1
#dieTwo = 1
sum = dieOne + dieTwo

if dieOne == dieTwo:
    print("You threw a double, so:", sum * 2)

else:
    print(sum)