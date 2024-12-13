import re

# f = open('testinput.txt', 'r')
f = open('input.txt', 'r')

games = []
rawlines = f.readlines()
gameDict = {'A':(), 'B':(), 'Prize': (), 'Cheapest': 0}
for rl in rawlines:
    if 'Button A' in rl:
        matches = re.findall(r"X\+(\d+)|Y\+(\d+)", rl)
        x_value = int(matches[0][0]) 
        y_value = int(matches[1][1])
        gameDict['A'] = (x_value, y_value)
    elif 'Button B' in rl:
        matches = re.findall(r"X\+(\d+)|Y\+(\d+)", rl)
        x_value = int(matches[0][0]) 
        y_value = int(matches[1][1])
        gameDict['B'] = (x_value, y_value)
    elif 'Prize' in rl:
        matches = re.findall(r"X\=(\d+)|Y\=(\d+)", rl)
        x_value = int(matches[0][0]) 
        y_value = int(matches[1][1])
        gameDict['Prize'] = (x_value, y_value)
        games.append(gameDict)
        gameDict = {'A':(), 'B':(), 'Prize': (), 'Cheapest': 0}

for g in games:
    x_a, y_a = g['A']
    x_b, y_b = g['B']
    target_x, target_y = g['Prize']
    tokens = 0
    found = []
    for i in range(0, 100):
        for j in range(0, 100):
            if x_a*i + x_b*j == target_x and y_a*i + y_b*j == target_y:
                found.append((i,j, i*3+j))
   
    found = sorted(found, key=lambda x: x[2])
    if len(found) != 0:
        tokens = found[0][2]


    g['Cheapest'] = tokens

total_tokens = 0
for g in games:
    total_tokens += g['Cheapest']

print(total_tokens)

