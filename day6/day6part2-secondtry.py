import numpy as np

def getMapWithPath(mapToWork, startingPos):
    inWorkMap = mapToWork.copy()
    isLooping = False
    guardOnMap = True
    # dir: 0 = up, 1 = right, 2 = down, 3 = left
    direction = 0
    currentPos = startingPos
    touchedObjectLocations = []
    while guardOnMap:
        if direction == 0:
            if currentPos[0] <= 0:
                guardOnMap = False
            elif currentPos[0] > 0 and inWorkMap[currentPos[0] - 1][currentPos[1]] != "#":
                currentPos = (currentPos[0] - 1, currentPos[1])
                inWorkMap[currentPos[0]][currentPos[1]] = "^"
            elif inWorkMap[currentPos[0] - 1][currentPos[1]] == "#":
                touchedObjectLocations.append(
                    ((currentPos[0] - 1, currentPos[1]), direction)
                )
                direction = 1
        if direction == 1:
            if currentPos[1] >= len(inWorkMap[0]) - 1:
                guardOnMap = False
            elif inWorkMap[currentPos[0]][currentPos[1] + 1] != "#":
                currentPos = (currentPos[0], currentPos[1] + 1)
                inWorkMap[currentPos[0]][currentPos[1]] = "^"
            elif inWorkMap[currentPos[0]][currentPos[1] + 1] == "#":
                touchedObjectLocations.append(
                    ((currentPos[0], currentPos[1] + 1), direction)
                )
                direction = 2
        if direction == 2:
            if currentPos[0] >= len(inWorkMap) - 1:
                guardOnMap = False
            elif inWorkMap[currentPos[0] + 1][currentPos[1]] != "#":
                currentPos = (currentPos[0] + 1, currentPos[1])
                inWorkMap[currentPos[0]][currentPos[1]] = "^"
            elif inWorkMap[currentPos[0] + 1][currentPos[1]] == "#":
                touchedObjectLocations.append(
                    ((currentPos[0] + 1, currentPos[1]), direction)
                )
                direction = 3
        if direction == 3:
            if currentPos[1] <= 0:
                guardOnMap = False
            if inWorkMap[currentPos[0]][currentPos[1] - 1] != "#":
                currentPos = (currentPos[0], currentPos[1] - 1)
                inWorkMap[currentPos[0]][currentPos[1]] = "^"
            elif inWorkMap[currentPos[0]][currentPos[1] - 1] == "#":
                touchedObjectLocations.append(
                    ((currentPos[0], currentPos[1] - 1), direction)
                )
                direction = 0
        if len(touchedObjectLocations) >= 8:
            lastone = touchedObjectLocations[-1]
            isLooping = lastone in touchedObjectLocations[:len(touchedObjectLocations)-1]  
            if isLooping: break

    return (inWorkMap, isLooping)

f = open("input.txt", "r")

lines = []
for line in f.readlines():
    line = line.strip("\n")
    lineList = []
    for c in line:
        lineList.append(c)
    lines.append(lineList)
map = np.asarray(lines)

startingPos = np.where(map == "^")
startingPos = (startingPos[0][0], startingPos[1][0])
mapWithPath, isLooping = getMapWithPath(map, startingPos)

loopsThatCanBeMade = 0
for i in range(0, len(map)):
    for j in range(0, len(map[0])):
        if (i,j) != startingPos and mapWithPath[i][j] == '^':
            mapToTest = map.copy()
            mapToTest[i][j] = '#'
            resultMap, resultIsLooping = getMapWithPath(mapToTest, startingPos)
            if resultIsLooping:
                loopsThatCanBeMade += 1

print(loopsThatCanBeMade)