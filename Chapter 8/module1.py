def getSA(cubeSide):
    SA = cubeSide * cubeSide * 6
    return SA

def getVolume(cubeSide):
    volume = cubeSide ** 3
    return volume

print("Please enter a side of the cube")
cubeSide = int(input())
SA = getSA(cubeSide)
volume = getVolume(cubeSide)
print("Surface area: " + str(SA) + "[unit]²")
print("Volume: " + str(volume) + "[unit]³")