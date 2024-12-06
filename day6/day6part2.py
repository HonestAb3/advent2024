import numpy as np

f = open("testinput.txt", "r")

lines = []
for line in f.readlines():
    line = line.strip("\n")
    lineList = []
    for c in line:
        lineList.append(c)
    lines.append(lineList)
map = np.asarray(lines)

print(map)
print(np.where(map == "^"))
print(map[6][4])

guardOnMap = True
# dir: 0 = up, 1 = right, 2 = down, 3 = left
direction = 0
currentPos = np.where(map == "^")
currentPos = (currentPos[0][0], currentPos[1][0])
touchedObjectLocations = []
while guardOnMap:
    if direction == 0:
        if currentPos[0] <= 0:
            guardOnMap = False
        elif currentPos[0] > 0 and map[currentPos[0] - 1][currentPos[1]] != "#":
            currentPos = (currentPos[0] - 1, currentPos[1])
            map[currentPos[0]][currentPos[1]] = "^"
        elif map[currentPos[0] - 1][currentPos[1]] == "#":
            touchedObjectLocations.append(
                ((currentPos[0] - 1, currentPos[1]), direction)
            )
            direction = 1
    if direction == 1:
        if currentPos[1] >= len(map[0]) - 1:
            guardOnMap = False
        elif map[currentPos[0]][currentPos[1] + 1] != "#":
            currentPos = (currentPos[0], currentPos[1] + 1)
            map[currentPos[0]][currentPos[1]] = "^"
        elif map[currentPos[0]][currentPos[1] + 1] == "#":
            touchedObjectLocations.append(
                ((currentPos[0], currentPos[1] + 1), direction)
            )
            direction = 2
    if direction == 2:
        if currentPos[0] >= len(map) - 1:
            guardOnMap = False
        elif map[currentPos[0] + 1][currentPos[1]] != "#":
            currentPos = (currentPos[0] + 1, currentPos[1])
            map[currentPos[0]][currentPos[1]] = "^"
        elif map[currentPos[0] + 1][currentPos[1]] == "#":
            touchedObjectLocations.append(
                ((currentPos[0] + 1, currentPos[1]), direction)
            )
            direction = 3
    if direction == 3:
        if currentPos[1] <= 0:
            guardOnMap = False
        if map[currentPos[0]][currentPos[1] - 1] != "#":
            currentPos = (currentPos[0], currentPos[1] - 1)
            map[currentPos[0]][currentPos[1]] = "^"
        elif map[currentPos[0]][currentPos[1] - 1] == "#":
            touchedObjectLocations.append(
                ((currentPos[0], currentPos[1] - 1), direction)
            )
            direction = 0

    print(map)
    print("-----------")
print("final map")
print(map)
print(np.count_nonzero(map == "^"))
print(touchedObjectLocations)
obstacleToCreateLoop = 0
for touchedObj in touchedObjectLocations:
    if touchedObj[1] == 0:
        rowToExamine = map[touchedObj[0][0] + 1]
        objsFound = np.where(rowToExamine[touchedObj[0][1] :] == "#")[0]
        if objsFound.size > 0:
            firstObjFound = objsFound[0]
            firstObjFound += len(rowToExamine[: touchedObj[0][1]])
            columnToExamine = map.T[firstObjFound - 1]
            secondObjFound = np.where(columnToExamine[touchedObj[0][0] + 1 :] == "#")[0]
            if secondObjFound.size > 0:
                finalRowToCheck = map[touchedObj[0][0] + secondObjFound[0]]
                finalObjsFound = np.where(finalRowToCheck == "#")[0]
                for o in touchedObjectLocations:
                    idx = finalObjsFound[-1]
                    if o[1] == 0 and idx < touchedObj[0][1]:
                        obstacleToCreateLoop += 1
                        print("found loop!", touchedObj)
    elif touchedObj[1] == 1:
        columnToExamine = map.T[touchedObj[0][1] - 1]
        objsFound = np.where(columnToExamine[touchedObj[0][0] :] == "#")[0]
        if objsFound.size > 0:
            firstObjFound = objsFound[0]
            firstObjFound += len(columnToExamine[: touchedObj[0][0]])
            rowToExamine = map[firstObjFound - 1]
            secondObjFound = np.where(rowToExamine[: firstObjFound + 1] == "#")[0]
            if secondObjFound.size > 0:
                finalColumnToCheck = map.T[secondObjFound[-1] + 1]
                finalObjsFound = np.where(finalColumnToCheck == "#")[0]
                for o in touchedObjectLocations:
                    idx = finalObjsFound[-1]
                    if o[1] == [1] and idx < touchedObj[0][0]:
                        obstacleToCreateLoop += 1
                        print("found loop!", touchedObj)
    elif touchedObj[1] == 2:
        rowToExamine = map[touchedObj[0][0] - 1]
        objsFound = np.where(rowToExamine[: touchedObj[0][1]] == "#")[0]
        if objsFound.size > 0:
            firstObjFound = objsFound[0]
            columnToExamine = map.T[firstObjFound + 1]
            secondObjFound = np.where(columnToExamine[: touchedObj[0][1]] == "#")[0]
            if secondObjFound.size > 0:
                finalRowToCheck = map[touchedObj[0][0] - secondObjFound[0]]
                finalObjsFound = np.where(finalRowToCheck == "#")[0]
                for o in touchedObjectLocations:
                    idx = finalObjsFound[0]
                    if o[1] == 2 and idx > o[0][1]:
                        obstacleToCreateLoop += 1
                        print("found loop!", touchedObj)
    elif touchedObj[1] == 3:
        columnToExamine = map.T[touchedObj[0][1] + 1]
        objsFound = np.where(columnToExamine[: touchedObj[0][0]] == "#")[0]
        if objsFound.size > 0:
            firstObjFound = objsFound[0]
            rowToExamine = map[firstObjFound + 1]
            secondObjFound = np.where(rowToExamine[firstObjFound:] == "#")[0]
            if secondObjFound.size > 0:
                finalColToCheck = map.T[
                    len(rowToExamine[:firstObjFound]) + secondObjFound[0] - 1
                ]
                finalObjsFound = np.where(finalColToCheck[secondObjFound[0] :] == "#")[
                    0
                ]
                for o in touchedObjectLocations:
                    idx = finalObjsFound[0] + len(finalColToCheck[: secondObjFound[0]])
                    if o[1] == 3 and idx > o[0][0]:
                        obstacleToCreateLoop += 1
                        print("found loop!", touchedObj)

print(obstacleToCreateLoop)
