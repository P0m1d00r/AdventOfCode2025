def IsInside(point , polygon):
    n = len(polygon)
    x,y = point
    inside = False

    j = n - 1
    for i in range(n):
        xi, yi = polygon[i][0], polygon[i][1]
        xj, yj = polygon[j][0], polygon[j][1]
        if (xi == xj == x and min(yi,yj) <= y <= max(yi,yj)) or (yi == yj == y and min(xi,xj) <= x <= max(xi,xj)):
            return True
        j = i


    j = n - 1
    for i in range(n):
        xi, yi = polygon[i][0], polygon[i][1]
        xj, yj = polygon[j][0], polygon[j][1]
        if ((yi > y) != (yj > y)) and x < xi:
            inside = not inside
        j = i
    return inside

def CornersInside(point_1, point_2, polygon):
    xa, ya = point_1[0], point_1[1]
    xb, yb = point_2[0], point_2[1]
    xc, yc = point_1[0], point_2[1]
    xd, yd = point_2[0], point_1[1]
    square = [[xa, ya], [xb, yb], [xc, yc], [xd, yd]]
    for corner in square:
        if not IsInside((corner[0], corner[1]), polygon):
            return False
    return True

def polygonNotCrossingSquare(point_1, point_2, polygon):
    up = [[min(point_1[0], point_2[0]), max(point_1[1], point_2[1])], [max(point_1[0], point_2[0]), max(point_1[1], point_2[1])]]
    right = [[max(point_1[0], point_2[0]), min(point_1[1], point_2[1])], [max(point_1[0], point_2[0]), max(point_1[1], point_2[1])]]
    left = [[min(point_1[0], point_2[0]), min(point_1[1], point_2[1])], [min(point_1[0], point_2[0]), max(point_1[1], point_2[1])]]
    down = [[min(point_1[0], point_2[0]), min(point_1[1], point_2[1])], [max(point_1[0], point_2[0]), min(point_1[1], point_2[1])]]

    n = len(polygon)
    j = n - 1
    for i in range(n):
        xi, yi = polygon[i][0], polygon[i][1]
        xj, yj = polygon[j][0], polygon[j][1]

        if xi == xj:
            #pionowa
            if up[0][0] < xi < up[1][0]:
                if min(yi,yj) < up[0][1] <= max(yi, yj):
                    return False
            if down[0][0] < xi < down[1][0]:
                if min(yi, yj) <= down[0][1] < max(yi, yj):
                    return False
        if yi == yj:
            #pozioma
            if left[0][1] < yi < left[1][1]:
                if min(xi,xj) <= left[0][0] < max(xi,xj):
                    return False
            if right[0][1] < yi < right[1][1]:
                if min(xi,xj) < right[0][0] <= max(xi,xj):
                    return False
        j = i

    return True

with open("input.txt", "r", encoding="utf-8") as file:
    polygon = file.read().splitlines()

n = len(polygon)
for i in range(len(polygon)):
    polygon[i] = polygon[i].split(",")
    for j in range(len(polygon[i])):
        polygon[i][j] = int(polygon[i][j])



maxfield = 0
for point1 in range(n):
    for point2 in range(point1 + 1, n):
        field = (abs(polygon[point1][0] - polygon[point2][0]) + 1) * (abs(polygon[point1][1] - polygon[point2][1]) + 1)
        if field > maxfield:
            if CornersInside(polygon[point1], polygon[point2], polygon) and polygonNotCrossingSquare(polygon[point1], polygon[point2], polygon):
                maxfield = field



print(maxfield)