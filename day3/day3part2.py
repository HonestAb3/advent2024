import re

f = open("input.txt", "r")

matches = re.findall("mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\)", f.read())

do = True
total = 0
for m in matches:
    if "don't" in m:
        do = False
    elif "do()" in m:
        do = True
    if do:
        if "mul" in m:
            (num1, num2) = map(int, re.findall("(\d{1,3})", m))
            total += num1 * num2
print(total)
