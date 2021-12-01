lines = []
with open('input.txt') as input:
    lines = input.readlines()

increases = 0
for line in range(0, (len(lines))):
    if line != 0:
        if lines[line] > lines[line-1]:
            print(lines[line] + 'increased')
            increases = increases+1
        else:
            print(lines[line] + 'decreased')
    else:
        print(lines[line] + 'n/a')
print(increases+1)
