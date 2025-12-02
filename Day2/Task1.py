answer = 0



with open("input.txt" , "r", encoding="utf-8") as f:
    ranges = f.read()
ranges = ranges.split(",")


for j in ranges:
    j = j.split("-")
    rangeStart = int(j[0])
    rangeEnd = int(j[1])
    for i in range(rangeStart, rangeEnd + 1):
        i = str(i)
        if len(i) > 1:
            half = len(i)//2
            firstHalf = i[:half]
            secondHalf = i[half:]
            if firstHalf == secondHalf:
                answer += int(i)

print(answer)
