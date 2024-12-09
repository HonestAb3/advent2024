
f = open('simpleinput.txt', 'r')
# f = open('testinput.txt', 'r')
# f = open('input.txt', 'r')

rawLine = f.read()
data = []
for c in rawLine:
    data.append(int(c))

print(data)

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

print(mappedData)

fixedMappedData = mappedData.copy()

for i in range(len(mappedData)-1, 0, -1):
    if mappedData[i] != '.':
        for j in range(0, len(fixedMappedData)):
            if j > i:
                break
            if fixedMappedData[j] == '.':
                fixedMappedData[j] = mappedData[i]
                fixedMappedData[i] = '.'
                break

print(fixedMappedData)
stophere =fixedMappedData.index('.')
print(fixedMappedData[:stophere])
sum = 0
for i in range(0, len(fixedMappedData[:stophere])):
    sum += fixedMappedData[i] * i

print(sum)