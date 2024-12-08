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
                
                iToAdjust = i
                jToAdjust = j
                
                #look above
                while iToAdjust - abs(cr) >= 0:
                    if cc > 0 and jToAdjust - abs(cc) >= 0:
                        mapWithAntiNodes[iToAdjust-abs(cr), jToAdjust-cc] = '#'
                        jToAdjust = jToAdjust-cc
                    elif cc < 0 and jToAdjust + abs(cc) <= len(map[0])-1:
                        mapWithAntiNodes[iToAdjust-abs(cr), jToAdjust+abs(cc)] = '#'
                        jToAdjust = jToAdjust+abs(cc)
                    elif cc == 0: 
                        mapWithAntiNodes[iToAdjust-abs(cr), jToAdjust] = '#'

                    iToAdjust = iToAdjust - abs(cr)
                    
                #look below
                oiToAdjust = o[0]
                ojToAdjust = o[1]
                while oiToAdjust + abs(cr) <= len(map)-1:
                    #if positive column change and still in bounds
                    if cc > 0 and ojToAdjust + abs(cc) <= len(map[0])-1:
                        mapWithAntiNodes[oiToAdjust+abs(cr)][ojToAdjust+cc] = '#'
                        ojToAdjust = ojToAdjust+cc
                    #if negative column change and still in bounds
                    elif cc < 0 and ojToAdjust - abs(cc) >= 0:
                        mapWithAntiNodes[oiToAdjust+abs(cr)][ojToAdjust-abs(cc)] = '#'
                        ojToAdjust = ojToAdjust-abs(cc)
                    #if no column change
                    elif cc == 0:
                        mapWithAntiNodes[oiToAdjust+abs(cr)][ojToAdjust] = '#'
                    oiToAdjust = oiToAdjust + abs(cr)
                mapWithAntiNodes[i][j] = '#'
                mapWithAntiNodes[o[0]][o[1]] = '#'
            
            
print(mapWithAntiNodes)                               
print(np.count_nonzero(mapWithAntiNodes == '#'))