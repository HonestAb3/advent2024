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
    score = 0
    rating = 0
    if topomap[th[0]][th[1]] == 9 and th not in beenthere:
        score += 1
        beenthere.append(th)
        rating+=1
    elif topomap[th[0]][th[1]] == 9 and th in beenthere:
        rating += 1
    else:
        beenthere.append(th)
        #check north
        if th[0] - 1 >= 0 and topomap[th[0]-1][th[1]] == topomap[th[0]][th[1]] +1:
            d = pathfind((th[0]-1, th[1]), topomap, beenthere)
            score += d[0]
            rating += d[1]
        #check south
        if th[0] + 1 <= len(topomap)-1 and topomap[th[0]+1][th[1]] == topomap[th[0]][th[1]] +1:
            d = pathfind((th[0]+1, th[1]), topomap, beenthere)
            score += d[0]
            rating += d[1]
        #check east
        if th[1] + 1 <= len(topomap[0])-1 and topomap[th[0]][th[1]+1] == topomap[th[0]][th[1]] +1:
            d = pathfind((th[0], th[1]+1), topomap, beenthere)
            score += d[0]
            rating += d[1]
        #check west
        if th[1] - 1 >= 0 and topomap[th[0]][th[1]-1] == topomap[th[0]][th[1]] +1:
            d = pathfind((th[0], th[1]-1), topomap, beenthere)
            score += d[0]
            rating += d[1]
    return (score, rating)

trailTotal = 0
ratingTotal = 0
for th in trailheads:
    beenthere = []
    op, score = pathfind(th, topomap, beenthere)
    trailTotal += op
    ratingTotal += score

print('Trail Score Total:', trailTotal)
print('Trail Rating Total:', ratingTotal)


