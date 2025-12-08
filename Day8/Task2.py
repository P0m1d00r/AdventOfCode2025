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
done = False
test = 0
while done == False:
    closestRange = None
    closestPoint1 = None
    closestPoint2 = None
    for point in range(len(data)):
        for point2 in range(point + 1, len(data)):
            distance = (data[point][0] - data[point2][0]) ** 2 + (data[point][1] - data[point2][1]) ** 2 + (data[point][2] - data[point2][2]) ** 2
            if (closestRange is None or distance < closestRange) and (circuts[point] != circuts[point2] or circuts[point] == 0):
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

    done = True
    firstCircut = circuts[0]
    for i in range(len(data)):
        if circuts[i] != firstCircut:
            done = False

    test += 1
    print(len(data) - test)

for i in range(len(data)):
    print((i, circuts[i]))

print(data[closestPoint1][0] * data[closestPoint2][0])