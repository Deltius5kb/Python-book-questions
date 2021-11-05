#Q1
#dont understand question all that well so this is the program i think it wants
#ask user to enter number 4 times
#if not between 0 and 120 then re enter
#add them up
#get an average
#print total and average

def isNumRight(x):
    num = int(input("Enter the number of tickets sold (" + str(x) + ")"))
    if num >= 0 or num <= 120:
        return num
    else:
        print("Sorry that cant be right youre nowhere near popular enough, try again.")
        isNumRight()

x = 4
total = 0
while x > 0:
    num = isNumRight(x)
    total += num
    x -= 1

avg = total / 4
print("Average:     " + str(avg))
print("Total:       " + str(total))
