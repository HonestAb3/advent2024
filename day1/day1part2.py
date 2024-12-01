f = open("input.txt", "r")
rawLines = f.readlines()

firstSide = []
secondSideDict = {}
for line in rawLines:
    (x, y) = map(int, line.replace("\n", "").split("   "))
    firstSide.append(x)
    if y not in secondSideDict:
        secondSideDict[y] = 1
    else:
        secondSideDict[y] += 1

total = 0

for i in firstSide:
    if i in secondSideDict:
        total += i * secondSideDict[i]

print(total)
