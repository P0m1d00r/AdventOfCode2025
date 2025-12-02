answer = 0
done = False

with open("input.txt" , "r", encoding="utf-8") as f:
    ranges = f.read()
ranges = ranges.split(",")


for j in ranges:
    j = j.split("-")
    rangeStart = int(j[0])
    rangeEnd = int(j[1])
    for i in range(rangeStart, rangeEnd + 1):
        dividers = []
        done = False
        for k in range(1, len(str(i))):
            if len(str(i))%k == 0:
                dividers.append(k)
        for divider in dividers:
            cuts = []
            for l in range(len(str(i))//divider):
                startCut = divider*l
                endCut = divider*(l+1)
                cuts.append(str(i)[startCut:endCut])
            for m in range(1, len(cuts)):
                if cuts[0] != cuts[m]:
                    break
                elif cuts[0] == cuts[m] and m == len(cuts) - 1:
                    answer += i
                    done = True
            if done == True:
                done = False
                break
                    
print(answer)

