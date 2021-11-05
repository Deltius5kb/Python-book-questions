#Q1

import random

count = 0
total = 0

for count in range(10):
    x = random.randint(1,10)
    print(x)
    total = total + x

print("total:", total)