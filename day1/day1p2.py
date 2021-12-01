lines = []
with open('input.txt') as input:
    lines = input.readlines()

sums = []
for line in (range(0, (len(lines)-3))):
    sums.append((int(lines[line]) + int(lines[line+1]) + int(lines[line+2])))
increases = 0
for total in range(0, (len(sums))):
    if total != 0:
        if sums[total] > sums[total-1]:
            print(str(sums[total]) + 'increased')
            increases = increases+1
        else:
            print(str(sums[total]) + 'decreased')
    else:
        print(str(sums[total]) + 'n/a')
print(increases+1)
