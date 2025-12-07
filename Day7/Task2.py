from collections import defaultdict

with open("input.txt", "r", encoding = "utf-8") as file:
    data = file.read().splitlines()

result = 0
beams = [data[0].index('S')]
beamsCount = defaultdict(int)
beamsCount[beams[0]] = 1

for lineIndex in range(1, len(data)):
    for letterIndex in range(len(data[lineIndex])):
        if data[lineIndex][letterIndex] == "^" and letterIndex in beams:
            beams.append(letterIndex + 1)
            beams.append(letterIndex - 1)
            beams.remove(letterIndex)

            beamsCount[letterIndex - 1] += beamsCount[letterIndex]
            beamsCount[letterIndex + 1] += beamsCount[letterIndex]
            beamsCount[letterIndex] = 0


    beamsTemp = []

    for beam in beams:
        if beam not in beamsTemp:
            beamsTemp.append(beam)

    beams = beamsTemp[:]

for i in beams:
    result += beamsCount[i]
print(result)