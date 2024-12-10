import numpy as np

# f = open('simpleinput.txt', 'r')
# f = open('anotherinput.txt', 'r')
f = open('input.txt', 'r')

lineList = []
for line in f.readlines():
    tl = []
    for c in line.strip():
        tl.append(int(c))
    lineList.append(tl)

topomap = np.array(lineList)

trailheads = list(zip(*np.where(topomap == 0)))

def pathfind(th, topomap, beenthere):
    op = 0

    if topomap[th[0]][th[1]] == 9 and th not in beenthere:
        op += 1
        beenthere.append(th)
    else:
        beenthere.append(th)
        #check north
        if th[0] - 1 >= 0 and topomap[th[0]-1][th[1]] == topomap[th[0]][th[1]] +1:
            op+= pathfind((th[0]-1, th[1]), topomap, beenthere)
        #check south
        if th[0] + 1 <= len(topomap)-1 and topomap[th[0]+1][th[1]] == topomap[th[0]][th[1]] +1:
             op+= pathfind((th[0]+1, th[1]), topomap, beenthere)
        #check east
        if th[1] + 1 <= len(topomap[0])-1 and topomap[th[0]][th[1]+1] == topomap[th[0]][th[1]] +1:
             op+= pathfind((th[0], th[1]+1), topomap, beenthere)
        #check west
        if th[1] - 1 >= 0 and topomap[th[0]][th[1]-1] == topomap[th[0]][th[1]] +1:
             op+= pathfind((th[0], th[1]-1), topomap, beenthere)
    return op

total = 0
for th in trailheads:
    beenthere = []
    total += pathfind(th, topomap, beenthere)

print(total)


