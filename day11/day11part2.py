import functools

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

@functools.cache
def dosomething(stones, blinks):
    count = 0
    for s in stones:
        if blinks == 0:       
            return len(stones)   
        else:
            growingS = []
            stoneString = str(s)
            if s == 0:
                growingS.append(1)
                count += dosomething(tuple(growingS), blinks-1)
            elif len(str(s)) % 2 == 0:
                newLeftStone = stoneString[:int(len(stoneString)/2)]
                newRightStone = stoneString[int(len(stoneString)/2):]
                growingS.append(int(newLeftStone))
                growingS.append(int(newRightStone))
                count += dosomething(tuple(growingS), blinks-1)
            else:
                growingS.append(s*2024)
                count += dosomething(tuple(growingS), blinks-1)
    return count

print(dosomething(tuple(stones), 75))