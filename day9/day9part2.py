# f = open('simpleinput.txt', 'r')
# f = open('testinput.txt', 'r')
f = open('input.txt', 'r')

rawLine = f.read()
data = []
for c in rawLine:
    data.append(int(c))

mappedData = []
idxCounter = 0
for i in range(0, len(data)):
    if i % 2 == 0:
        for i in range(0, data[i]):
            mappedData.append(idxCounter)
        idxCounter += 1
    else:
        for i in range(0, data[i]):
            mappedData.append('.')

fixedMappedData = mappedData.copy()

i = len(mappedData)-1
while i > 0:
    if mappedData[i] != '.':
        y = 0
        while mappedData[i-y] == mappedData[i]:
            y += 1
        for j in range(0, len(fixedMappedData)):
            if j > i:
                break
            if fixedMappedData[j] == '.':
                z = 0
                while fixedMappedData[z+j] == '.':
                    z+=1
                if y <= z:
                    for w in range(0, y):
                        fixedMappedData[j+w] = mappedData[i]
                        fixedMappedData[i-w] = '.'

                    break

        i -= y
    else:
        i -= 1

sum = 0
for i in range(0, len(fixedMappedData)):
    if isinstance(fixedMappedData[i], int):
        sum += fixedMappedData[i] * i

print(sum)