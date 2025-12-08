from collections import defaultdict

with open("input.txt", "r", encoding = "utf-8") as file:
    data = file.read().splitlines()

for i in range(len(data) -1, -1, -1):
    data[i] = data[i].split(",")
    for j in range(3):
        data[i][j] = int(data[i][j])

print(data)

result = 0
circuts = defaultdict(int)
lastCircut = 0
connections = []

for a in range(1000):
    closestRange = None
    closestPoint1 = None
    closestPoint2 = None
    for point in range(len(data)):
        for point2 in range(point + 1, len(data)):
            distance = (data[point][0] - data[point2][0]) ** 2 + (data[point][1] - data[point2][1]) ** 2 + (data[point][2] - data[point2][2]) ** 2
            if (closestRange is None or distance < closestRange) and (point, point2) not in connections:
                closestRange = distance
                closestPoint1 = point
                closestPoint2 = point2


    print((data[closestPoint1], data[closestPoint2], closestRange))

    lastCircut += 1
    if circuts[closestPoint1] != 0:
        for i in range(len(data)):
            if circuts[closestPoint1] == circuts[i] and i != closestPoint1:
                circuts[i] = lastCircut
    if circuts[closestPoint2] != 0:
        for i in range(len(data)):
            if circuts[closestPoint2] == circuts[i] and i != closestPoint2:
                circuts[i] = lastCircut

    circuts[closestPoint1] = lastCircut
    circuts[closestPoint2] = lastCircut
    connections.append((closestPoint1, closestPoint2))

for i in range(len(data)):
    print((i, circuts[i]))

longestCircuts = []

for i in range(1, lastCircut + 1):
    TempCircuts = 0
    for j in range(len(data)):
        if circuts[j] == i:
            TempCircuts += 1
    if len(longestCircuts) < 3 or TempCircuts > min(longestCircuts):
        longestCircuts.append(TempCircuts)
        if len(longestCircuts) > 3:
            longestCircuts.remove(min(longestCircuts))


result = 1
for i in longestCircuts:
    result *= i

print(result)