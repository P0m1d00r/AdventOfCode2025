result =  0

with open("input.txt", "r", encoding = "utf-8") as file:
    data = file.read().splitlines()

beams = []

beams.append(data[0].index('S'))

for lineIndex in range(1, len(data)):
    for letterIndex in range(len(data[lineIndex])):
        if data[lineIndex][letterIndex] == "^" and letterIndex in beams:
            beams.remove(letterIndex)
            beams.append(letterIndex + 1)
            beams.append(letterIndex - 1)
            result += 1

    beamsTemp = []

    for beam in beams:
        if beam not in beamsTemp:
            beamsTemp.append(beam)

    beams = beamsTemp[:]

print(result)