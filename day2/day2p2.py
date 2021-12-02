lines = []
with open('input.txt') as input:
    lines = input.readlines()

instructions = []
for line in lines:
    instructions.append(line.split())

horizontal = 0
depth = 0
aim = 0
for instruction in instructions:
    if instruction[0] == "forward":
        horizontal = horizontal + int(instruction[1])
        depth = depth + (aim * int(instruction[1]))
    elif instruction[0] == "down":
        aim = aim + int(instruction[1])
    elif instruction[0] == "up":
        aim = aim - int(instruction[1])

print(depth * horizontal)
