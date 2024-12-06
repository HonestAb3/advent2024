def checkIfUpdateIsGood(update, rules):
    good = True
    for i in range(len(update) - 1, 0, -1):
        for el in update[:i]:
            if update[i] not in rules:
                continue
            if el in rules[update[i]]:
                good = False
                break
    return good


def checkIfRulesBroken(subject, restOfBadUpdate, rules):
    if subject in rules:
        return any(i in restOfBadUpdate for i in rules[subject])
    else:
        return False


def checkAndFixUpdate(badElement, badUpdate, rules):
    fixedUpdate = []
    for i in range(0, len(badUpdate)):
        if badUpdate[i] in rules[badElement]:
            fixedUpdate.append(badElement)
            fixedUpdate.extend(badUpdate[i:])
            return fixedUpdate
        else:
            fixedUpdate.append(badUpdate[i])
    return fixedUpdate


# f = open("testinput.txt", "r")
f = open("actualinput.txt", "r")
rules = {}
updates = []
for line in f.readlines():
    if "|" in line:
        k, v = map(int, line.split("|"))

        if k in rules:
            rules[k].append(v)
        else:
            rules[k] = [v]
    elif line == "\n":
        continue
    else:
        inputUpdate = list(map(int, line.split(",")))
        updates.append(inputUpdate)

badUpdates = []
for u in updates:
    if not checkIfUpdateIsGood(u, rules):
        badUpdates.append(u)

fixedUpdates = []
inWorkBadUpdate = []
for badUpdate in badUpdates:
    inWorkBadUpdate = badUpdate.copy()
    while not checkIfUpdateIsGood(inWorkBadUpdate, rules):
        for i in range(len(badUpdate) - 1, 0, -1):
            isBad = checkIfRulesBroken(inWorkBadUpdate[i], inWorkBadUpdate[:i], rules)
            if isBad:
                badElement = inWorkBadUpdate[i]
                inWorkBadUpdate.pop(i)
                inWorkBadUpdate = checkAndFixUpdate(badElement, inWorkBadUpdate, rules)
                break
    fixedUpdates.append(inWorkBadUpdate)

sum = 0
for fixedUpdate in fixedUpdates:
    sum += fixedUpdate[len(fixedUpdate) // 2]

print(sum)
