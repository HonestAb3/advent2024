f = open("input.txt", "r")

inputLines = f.readlines()
numSafe = 0
for line in inputLines:
    op = list(map(int, line.split()))

    if (
        all(op[j] < op[j + 1] for j in range(len(op) - 1))
        or all(op[j] > op[j + 1] for j in range(len(op) - 1))
    ) and all(abs(op[j] - op[j + 1]) <= 3 for j in range(len(op) - 1)):
        # print(op)
        numSafe += 1
print(numSafe)
