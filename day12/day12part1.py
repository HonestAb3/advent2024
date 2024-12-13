import numpy as np

# f = open('simpleinput.txt','r')
# f = open('anotherinput.txt','r')
# f = open('testagain.txt', 'r')
f = open('input.txt', 'r')


lineList = []
for l in f.readlines():
    line = []
    for c in l.strip():
        line.append(c)
    lineList.append(line)

farm = np.array(lineList)

print(farm)

def attemptToFindRegionsIDs(farm):
    regions = {}
    for i in range(0, len(farm)):
        for j in range(0, len(farm[0])):
            if farm[i][j] not in regions:
                regions[str(farm[i][j])] = []

    return regions

def findUniqueRegions(farm, r):
    matchedPlots = list(zip(*np.where(farm == r)))
    matchedPlots = [tuple(map(int, el)) for el in matchedPlots]
    startingPoint = (int(matchedPlots[0][0]), int((matchedPlots[0][1])))
    uniqueRegions = []
    uniqueRegions.append([startingPoint])
    accountedFor = 1
    while accountedFor != len(matchedPlots):
        for ur in uniqueRegions:
            for sr in ur:
                x = [(mpi, mpj) for mpi, mpj in matchedPlots if sr[0] == mpi and abs(sr[1]-mpj) == 1 or abs(sr[0]-mpi) == 1 and sr[1] == mpj]
                for el in x:
                    if  (sr[0] == el[0] and abs(sr[1]-el[1]) == 1) or (abs(sr[0]-el[0]) == 1 and sr[1] == el[1]):
                        if (el[0], el[1]) not in ur:
                            accountedFor+=1
                            ur.append((el[0], el[1]))
        for m in matchedPlots:
            if not any(m in ur for ur in uniqueRegions):
                uniqueRegions.append([m])
                accountedFor+=1
                break

    return uniqueRegions                           
                    
def figureOutPerim(region):
    walls = 0

    for i in range(0, len(region)):
        plot = region[i]
        #nothing left
        if (plot[0], plot[1]-1) not in region:
            walls += 1
        #nothing up
        if (plot[0]-1, plot[1]) not in region:
            walls += 1
        #nothing right
        if (plot[0], plot[1]+1) not in region:
            walls += 1
        #nothing down
        if (plot[0]+1, plot[1]) not in region:
            walls += 1
    return walls * len(region)

regions = attemptToFindRegionsIDs(farm)

for r in regions:
    regions[r] = findUniqueRegions(farm, r)
# print(regions)

total = 0
for r in regions:
    for ur in regions[r]:
        total += figureOutPerim(ur)
print(total)

