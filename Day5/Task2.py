def CheckIngredient(ingredient, index):
    freshStartCI = []
    freshStopCI = []
    for i in fresh:
        i = i.split("-")
        freshStartCI.append(int(i[0]))
        freshStopCI.append(int(i[1]))
    freshStopCI.pop(index)
    freshStartCI.pop(index)

    for i in range(len(freshStartCI)):
        if ingredient >= freshStartCI[i] and ingredient <= freshStopCI[i]:
            return True
    return False




with open("input.txt" , "r" , encoding="utf-8") as f:
    input = f.read().split("\n\n")

wynik = 0
fresh = input[0].splitlines()
freshStart = []
freshStop = []


d = {}

for i in fresh:
    i = i.split("-")
    freshStart.append(int(i[0]))
    freshStop.append(int(i[1]))

freshStartTemp = freshStart[:]
for i in freshStartTemp:
    if i in freshStop:
        freshStart.remove(i)
        freshStop.remove(i)
        

for i in freshStart:
    d[i] = "S"

for i in freshStop:
    d[i] = "F"

freshList = []

for i in freshStart:
    freshList.append(i)

for i in freshStop:
    freshList.append(i)

freshList.sort()
lastPosition = 0
position = 0
StartPoint = 0

for i in freshList:
    if d[i] == "S":
        position += 1
    else:
        position -= 1
    
    if lastPosition == 0 and position > 0:
        wynik += 1
        StartPoint = i
    elif lastPosition > 0 and position == 0:
        wynik += i - StartPoint
    

    lastPosition = position

freshStart = []
freshStop = []
for i in fresh:
    i = i.split("-")
    freshStart.append(int(i[0]))
    freshStop.append(int(i[1]))

freshStartTemp = freshStart[:]
for i in range(len(freshStartTemp)):
    if freshStart[i] == freshStop[i]:
        if CheckIngredient(freshStart[i], i) == False:
            wynik += 1
print(wynik)