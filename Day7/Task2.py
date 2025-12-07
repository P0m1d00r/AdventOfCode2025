from collections import defaultdict

with open("input.txt", "r", encoding = "utf-8") as file:
    data = file.read().splitlines()

result = 0

beamsCount = defaultdict(int)
beamsCount[data[0].index('S')] = 1
linelength = len(data[0])

for lineIndex in range(1, len(data)):
    for letterIndex in range(linelength):
        if data[lineIndex][letterIndex] == "^" and beamsCount[letterIndex] > 0:
            beamsCount[letterIndex - 1] += beamsCount[letterIndex]
            beamsCount[letterIndex + 1] += beamsCount[letterIndex]
            beamsCount[letterIndex] = 0


for i in range(len(data[0])):
    result += beamsCount[i]
print(result)