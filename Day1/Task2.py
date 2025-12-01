position = 50
zerosAmount = 0
lastPosition = 50

with open("input.txt" , "r" , encoding="utf-8") as f:
    password = f.read().splitlines()

for i in range(len(password)):
    dir = password[i][0]
    steps = int(password[i][1:])
    if dir == "R":
        position += steps
    elif dir == "L":
        position -= steps
    
   
    zerosAmount += abs((lastPosition//100) - (position//100))    
    
    if dir == "L" and position%100 == 0:        #WYJĄTEK: Jak lastPostition będzie równe np 125 i zmniejszy się na 100 to mimo iż będzie na "0" nie doda bo 125//100 == 100//100 więc treba dodać manualnie
        zerosAmount += 1

    if dir == "L" and lastPosition%100 == 0:       #WYJĄTEK: Jak lastPostition będzie równe np 100 i zmniejszy się na 75 to program doda jedno "0" bo 100//100 != 75//100 więc trzeba to usunąć
        zerosAmount -= 1

    lastPosition = position

print(zerosAmount)
