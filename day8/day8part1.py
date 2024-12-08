import numpy as np
# f = open('simpleinput.txt', 'r')
# f = open('simpleinputpart2.txt', 'r')
# f = open('anotherInput.txt', 'r')
f = open('input.txt', 'r')

lines = []
for l in f.readlines():
    line = []
    for c in l.strip():
        line.append(c)
    lines.append(line)

map = np.asarray(lines)

antinodes = 0
mapWithAntiNodes = map.copy()

for i in range(0, len(map)):
    for j in range(0, len(map[0])):
        if map[i][j] != '.':
            found = map[i][j]
            others = np.argwhere(map[i+1:] == found)
            for o in others:
                #adjust o
                o[0] += i+1
                cr = o[0] - i
                cc = o[1] - j
                #look above
                if i - abs(cr) >= 0:
                    if cc > 0 and j - abs(cc) >= 0:
                        mapWithAntiNodes[i-abs(cr), j-cc] = '#'
                    elif cc < 0 and j + abs(cc) <= len(map[0])-1:
                        mapWithAntiNodes[i-abs(cr), j+abs(cc)] = '#'
                    elif cc == 0: 
                        mapWithAntiNodes[i-abs(cr), j] = '#'
                #look below
                if o[0] + abs(cr) <= len(map)-1:
                    #if positive column change and still in bounds
                    if cc > 0 and o[1] + abs(cc) <= len(map[0])-1:
                        mapWithAntiNodes[o[0]+abs(cr)][o[1]+cc] = '#'
                    #if negative column change and still in bounds
                    elif cc < 0 and o[1] - abs(cc) >= 0:
                        mapWithAntiNodes[o[0]+abs(cr)][o[1]-abs(cc)] = '#'
                    #if no column change
                    elif cc == 0:
                        mapWithAntiNodes[o[0]+abs(cr)][o[1]] = '#'
            
            
                                
print(np.count_nonzero(mapWithAntiNodes == '#'))