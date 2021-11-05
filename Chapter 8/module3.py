def getMaxTemps():
    maxTemp = 0
    day = 0
    for i in range(7):
        temp = int(input("Please enter a temperature"))
        if temp > maxTemp:
            maxTemp = temp
            day = i

    return maxTemp, day

maxTemps, day = getMaxTemps()
print(str(maxTemps), "on day " + str(day + 1))