import numpy as np

f = open("input.txt", "r")

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
guardSquareCount = 1
while guardOnMap:
    # guard try to move current direction
    if direction == 0:
        if currentPos[0] <= 0:
            guardOnMap = False
        elif currentPos[0] > 0 and map[currentPos[0] - 1][currentPos[1]] != "#":
            currentPos = (currentPos[0] - 1, currentPos[1])
            map[currentPos[0]][currentPos[1]] = "^"
        elif map[currentPos[0] - 1][currentPos[1]] == "#":
            direction = 1
    if direction == 1:
        if currentPos[1] >= len(map[0]) - 1:
            guardOnMap = False
        elif map[currentPos[0]][currentPos[1] + 1] != "#":
            currentPos = (currentPos[0], currentPos[1] + 1)
            map[currentPos[0]][currentPos[1]] = "^"
        elif map[currentPos[0]][currentPos[1] + 1] == "#":
            direction = 2
    if direction == 2:
        if currentPos[0] >= len(map) - 1:
            guardOnMap = False
        elif map[currentPos[0] + 1][currentPos[1]] != "#":
            currentPos = (currentPos[0] + 1, currentPos[1])
            map[currentPos[0]][currentPos[1]] = "^"
        elif map[currentPos[0] + 1][currentPos[1]] == "#":
            direction = 3
    if direction == 3:
        if currentPos[1] <= 0:
            guardOnMap = False
        if map[currentPos[0]][currentPos[1] - 1] != "#":
            currentPos = (currentPos[0], currentPos[1] - 1)
            map[currentPos[0]][currentPos[1]] = "^"
        elif map[currentPos[0]][currentPos[1] - 1] == "#":
            direction = 0

    print(map)
    print("-----------")
print("final map")
print(map)
print(np.count_nonzero(map == "^"))
