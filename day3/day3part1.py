import re

f = open("input.txt", "r")

matches = re.findall("mul\(\d{1,3},\d{1,3}\)", f.read())

print(matches)

total = 0

for m in matches:
    (num1, num2) = map(int, re.findall("(\d{1,3})", m))
    total += num1 * num2

print(total)
