import numpy as np
import re

f = open("actualInput.txt", "r")


def testForward(line):
    cLine = ""
    for el in line:
        cLine += el
    return len(re.findall("XMAS", cLine))

def testBackward(line):
    cLine = ""
    for el in line:
        cLine += el
    return len(re.findall("SAMX", cLine))

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
for i in inputMatrix:
    found += testForward(i) + testBackward(i)
for i in inputMatrix.T:
    found += testForward(i) + testBackward(i)
i = 0

while len(inputMatrix.diagonal(i)) > 0:
    found += testForward(inputMatrix.diagonal(i)) + testBackward(
        inputMatrix.diagonal(i)
    )
    i += 1

i = 1
while len(inputMatrix.diagonal(0 - i)) > 0:
    found += testForward(inputMatrix.diagonal(0 - i)) + testBackward(
        inputMatrix.diagonal(0 - i)
    )
    i += 1

flipped = np.fliplr(inputMatrix)

i = 0
while len(flipped.diagonal(i)) > 0:
    found += testForward(flipped.diagonal(i)) + testBackward(flipped.diagonal(i))
    i += 1

i = 1
while len(flipped.diagonal(0 - i)) > 0:
    found += testForward(flipped.diagonal(0 - i)) + testBackward(
        flipped.diagonal(0 - i)
    )
    i += 1

print(found)
