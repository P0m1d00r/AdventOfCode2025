with open("input.txt", "r", encoding = "utf-8") as file:
    data = file.read().splitlines()


result = 0

initialNumber1 = list(data[0])
initialNumber2 = list(data[1])
initialNumber3 = list(data[2])
initialNumber4 = list(data[3])
initialOperators = list(data[4])

for i in range(len(initialNumber1) - 1, -1, -1):
    if initialNumber1[i] == " ":
        initialNumber1[i] = ""
    if initialNumber2[i] == " ":
        initialNumber2[i] = ""
    if initialNumber3[i] == " ":
        initialNumber3[i] = ""
    if initialNumber4[i] == " ":
        initialNumber4[i] = ""


starts = []

for i in range(len(initialOperators)):
    if initialOperators[i] != " ":
        starts.append(i)

for i in range(len(starts)):
    if i < len(starts) - 1:
        numbersCount = starts[i + 1] - starts[i] - 1
    else:
        numbersCount = len(initialOperators) - starts[i]
    
    numbersFinal = []
    for j in range(numbersCount):
        numbersFinal.append(initialNumber1[starts[i] + j] + initialNumber2[starts[i] + j] + initialNumber3[starts[i] + j] + initialNumber4[starts[i] + j])
        numbersFinal[j] = int(numbersFinal[j])

    match initialOperators[starts[i]]:
        case "+":
            resultTemp = 0
            for j in range(len(numbersFinal)):
                resultTemp += numbersFinal[j]
        case "*":
            resultTemp = 1
            for j in range(len(numbersFinal)):
                resultTemp *= numbersFinal[j]

    result += resultTemp
    

print(result)










