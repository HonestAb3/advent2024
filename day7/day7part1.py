f = open('input.txt', 'r')

equations = []

for line in f.readlines():
    line = line.strip('\n')
    p1 = int(line.split(':')[0])
    rNums = list(map(int, line.split(':')[1].split(' ')[1:]))
    equations.append((p1, rNums))

def figureItOut(equation):
    target = equation[0]
    nums = equation[1]
   
    if len(nums) == 2:
        if nums[0] * nums[1] == target:
            return True
        elif nums[0] + nums[1] == target:
            return True
        elif int(str(nums[0]) + str(nums[1])) == target:
            return True
    else:
        newNumMulti = nums[0] * nums[1]
        newNumsMulti = [newNumMulti] + nums[2:]
    
        newNumAdd = nums[0] + nums[1]
        newNumsAdd = [newNumAdd] + nums[2:]

        newNumConcat = int(str(nums[0]) + str(nums[1]))
        newNumsConcat = [newNumConcat] + nums[2:]
        
        if figureItOut((target, newNumsMulti)):
            return True
        elif figureItOut((target, newNumsAdd)):
            return True
        elif figureItOut((target, newNumsConcat)):
            return True

sum = 0
for eq in equations:
    if figureItOut(eq):
        sum += eq[0]

print(sum)