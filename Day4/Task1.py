with open("input.txt" , "r" , encoding="utf-8") as f:
    lines = f.read().splitlines()

wynik = 0

for x in range(len(lines)):
    for y in range(len(lines[0])):
        rolls = 0
        
        if lines[x][y] == "@":
            if x != 0:
                if y != 0:
                    if lines[x-1][y-1] == "@":
                        rolls += 1
                if lines[x-1][y] == "@":
                    rolls += 1 
                if y < len(lines[0]) - 1:
                        if lines[x-1][y+1] == "@":
                            rolls += 1 
            
            if y != 0:
                if lines[x][y-1] == "@":
                    rolls += 1
            if y < len(lines[0]) - 1:
                if lines[x][y+1] == "@":
                        rolls += 1

            if x < len(lines) - 1:
                if y != 0:
                    if lines[x+1][y-1] == "@":
                        rolls += 1
                if lines[x+1][y] == "@":
                    rolls += 1 
                if y < len(lines[0]) - 1:
                        if lines[x+1][y+1] == "@":
                            rolls += 1
            
            if rolls < 4:
                wynik += 1

print(wynik)


