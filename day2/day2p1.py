lines = []
with open('input.txt') as input:
    lines = input.readlines()

instructions = []
for line in lines:
    instructions.append(line.split())

horizontal = 0
depth = 0
for instruction in instructions:
    if instruction[0] == "forward":
        horizontal = horizontal + int(instruction[1])
    elif instruction[0] == "down":
        depth = depth + int(instruction[1])
    elif instruction[0] == "up":
        depth = depth - int(instruction[1])

print(depth * horizontal)
