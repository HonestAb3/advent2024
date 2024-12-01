f = open("input.txt", "r")
lines = f.readlines()

first = []
second = []
for line in lines:
    (x, y) = map(int, line.replace("\n", "").split("   "))
    first.append(x)
    second.append(y)

first = sorted(first)
second = sorted(second)

distance = 0
for i in range(0, len(first)):
    distance += abs(first[i] - second[i])
print(distance)
