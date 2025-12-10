with open("input.txt", "r", encoding="utf-8") as file:
    data = file.read().splitlines()

for i in range(len(data)):
    data[i] = data[i].split(",")
    for j in range(len(data[i])):
        data[i][j] = int(data[i][j])

print(data)
maxfield = 0
for point1 in range(len(data)):
    for point2 in range(point1 + 1, len(data)):
        field = (abs(data[point1][0] - data[point2][0]) + 1) * (abs(data[point1][1] - data[point2][1]) + 1)
        if field > maxfield:
            maxfield = field

print(maxfield)