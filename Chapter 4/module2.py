#Q2

import random

count = 0
total = 0

for count in range(1000):
    x = random.randint(1,10)
    total = total + x

total /= 1000
print("average =", total)


'''This is what you would expect as it is an average and not a total.
The average in the end is usually around 5 as there are many more numbers and
this means it is more likely for it to be more consistent'''
