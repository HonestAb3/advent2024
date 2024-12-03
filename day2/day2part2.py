def checkIfAllAsc(lineData):
    return all(lineData[j] < lineData[j + 1] for j in range(len(lineData) - 1))

def checkIfAllDesc(lineData):
    return all(lineData[j] > lineData[j + 1] for j in range(len(lineData) - 1))

def checkOrder(lineData):
    return checkIfAllAsc(lineData) or checkIfAllDesc(lineData)

def checkIfNearEnough(lineData):
    return all(
        abs(lineData[j] - lineData[j + 1]) <= 3 for j in range(len(lineData) - 1)
    )

def checkIfSafe(lineData):
    if (checkIfAllAsc(lineData) or checkIfAllDesc(lineData)) and checkIfNearEnough(
        lineData
    ):
        return True
    else:
        return False

def funtimes(lineData):
    for i in range(0, len(lineData)):
        if checkIfSafe(lineData[:i] + lineData[i + 1 :]):
            return True
    return False


f = open("input.txt", "r")
inputLines = f.readlines()

numSafe = 0
for line in inputLines:
    lineData = list(map(int, line.split()))

    if checkIfSafe(lineData):
        numSafe += 1
    else:
        if funtimes(lineData):
            numSafe += 1

print("Number of Safe: ", numSafe)
