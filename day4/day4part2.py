import numpy as np
import re


def convertArrToString(arrLine):
    line = ""
    for el in arrLine:
        line += el
    return line


def check3by3(box):
    d1 = re.search("MAS|SAM", convertArrToString(box.diagonal()))
    d2 = re.search("MAS|SAM", convertArrToString(np.fliplr(box).diagonal()))

    if d1 and d2:
        return True
    else:
        return False


f = open("actualInput.txt", "r")

rawInput = f.read()

listOfChars = []
temp = []
for c in rawInput:
    if c != "\n":
        temp.append(c)
    elif c == "\n":
        listOfChars.append(temp)
        temp = []

inputMatrix = np.asarray(listOfChars)
found = 0
for i in range(0, len(inputMatrix)):
    for j in range(0, len(inputMatrix[0])):
        temp = np.array(inputMatrix[i : i + 3, j : j + 3])
        if check3by3(temp):
            found += 1

print(found)
