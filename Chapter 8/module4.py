#Q4

def getHours():
    saturHour = int(input("Please enter the employee's hours worked on saturday"))
    sunHour = int(input("Please enter the employee's hours worked on sunday"))

    weekHour = int(input("Please enter the employee's hours worked during the week [monday - friday] "))
    return weekHour, saturHour, sunHour

def getPay(weekHour, saturHour, sunHour, payRate):
    totalHours = weekHour + (saturHour * 1.5) + (sunHour * 2)
    totalPay = totalHours * payRate

    return totalPay, totalHours

name = input("What is the name of the worker?")

weekHour, saturHour, sunHour = getHours()

payRate = int(input("How much do they get paid per hour?"))
totalPay, totalHours = getPay(weekHour, saturHour, sunHour, payRate)

print("Employee name: " + name)
print("Hours worked: " + str(totalHours))
print("Total pay: " + str(totalPay))