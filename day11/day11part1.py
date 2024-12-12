
# f = open('testinput.txt', 'r')
f = open('input.txt', 'r')
l = f.read()
stones = list(map(int, l.split()))

def blink(stones):
    updatedStones = []
    for i in range(0, len(stones)):
        stoneString = str(stones[i])
        if stones[i] == 0:
            updatedStones.append(1)
        elif len(stoneString) % 2 == 0:
            newLeftStone = stoneString[:int(len(stoneString)/2)]
            newRightStone = stoneString[int(len(stoneString)/2):]
            updatedStones.append(int(newLeftStone))
            updatedStones.append(int(newRightStone))
        else:
            updatedStones.append(stones[i] * 2024)
    return updatedStones
    
print('original', stones)

for i in range(0, 25):
    # print(i)
    stones = blink(stones)
    

print(len(stones))
