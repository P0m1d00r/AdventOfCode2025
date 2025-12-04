with open("input.txt" , "r" , encoding="utf-8") as f:
    lines = f.read().splitlines()

wynik = 0
added = 1

for i in range(len(lines)):
     lines[i] = list(lines[i])



while added > 0:
    added = 0
    for x in range(len(lines)):
        for y in range(len(lines[0])):
            rolls = 0
            
            if lines[x][y] == "@":
                if x != 0:
                    if y != 0:
                        if lines[x-1][y-1] in ("@" , "x"):
                            rolls += 1
                    if lines[x-1][y] in ("@" , "x"):
                        rolls += 1 
                    if y < len(lines[0]) - 1:
                            if lines[x-1][y+1] in ("@" , "x"):
                                rolls += 1 
                
                if y != 0:
                    if lines[x][y-1] in ("@" , "x"):
                        rolls += 1
                if y < len(lines[0]) - 1:
                    if lines[x][y+1] in ("@" , "x"):
                            rolls += 1

                if x < len(lines) - 1:
                    if y != 0:
                        if lines[x+1][y-1] in ("@" , "x"):
                            rolls += 1
                    if lines[x+1][y] in ("@" , "x"):
                        rolls += 1 
                    if y < len(lines[0]) - 1:
                            if lines[x+1][y+1] in ("@" , "x"):
                                rolls += 1
                
                if rolls < 4:
                    wynik += 1
                    lines[x][y] = "x"
                    added += 1

    for x in range(len(lines)):
        for y in range(len(lines[0])):
             if lines[x][y] == "x":
                  lines[x][y] = "."

print(wynik)


