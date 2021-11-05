#Q2
#AANN AAA

import re

def isTrue():
    regNum = input("Enter the reg number")
    valid = re.match("[A-Z]{1,2}[0-9]{3,4}[A-Z]{6,8}", regNum)
    if valid:
        return regNum
    else:
        print("Sorry thats not quite right, please try again")
        isTrue()

regNum = isTrue()
print(regNum)