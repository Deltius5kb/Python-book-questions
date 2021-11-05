#Q4

cost = float(input("Enter cost"))

if cost <= 200:
    discount = 0.9

elif cost >= 100 and cost < 200:
    discount = 0.95

else:
    dicount = 1

print("The value of the cost is:", cost)
cost = cost * discount
print("The dicounted price is:", round(cost, 2))