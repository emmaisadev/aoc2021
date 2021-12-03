lines = []
with open('input.txt') as input:
    lines = input.readlines()

gamma_rate = ""
epsilon_rate = ""
for bit in range(12):
    oneCount = 0
    zeroCount = 0
    for line in lines:
        if line[bit] == "0":
            zeroCount = zeroCount + 1
        if line[bit] == "1":
            oneCount = oneCount + 1
    if oneCount > zeroCount:
        gamma_rate += "1"
        epsilon_rate += "0"
    if zeroCount > oneCount:
        gamma_rate += "0"
        epsilon_rate += "1"

print((int(gamma_rate, 2) * int(epsilon_rate, 2)))

