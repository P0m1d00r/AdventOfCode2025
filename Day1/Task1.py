position = 50
zerosAmount = 0

with open("input.txt" , "r" , encoding="utf-8") as f:
    password = f.read().splitlines()

for i in range(len(password)):
    dir = password[i][0]
    steps = int(password[i][1:])
    if dir == "R":
        position += steps
    elif dir == "L":
        position -= steps
    
    if position%100 == 0:
        zerosAmount += 1
    
print(zerosAmount)
