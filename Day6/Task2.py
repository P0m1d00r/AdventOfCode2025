with open("input.txt", "r", encoding = "utf-8") as file:
    data = file.read().splitlines()


result = 0

initialNumber1 = data[0].split(" ")
number1 = initialNumber1[:]

for i in range(len(initialNumber1) - 1, -1 ,-1):
    if number1[i] == "":
        number1.pop(i)
    else:
        number1[i] = int(number1[i])

initialNumber2 = data[1].split(" ")
number2 = initialNumber2[:]

for i in range(len(initialNumber2) - 1, -1 ,-1):
    if number2[i] == "":
        number2.pop(i)
    else:
        number2[i] = int(number2[i])

initialNumber3 = data[2].split(" ")
number3 = initialNumber3[:]

for i in range(len(initialNumber3) - 1, -1 ,-1):
    if number3[i] == "":
        number3.pop(i)
    else:
        number3[i] = int(number3[i])

initialNumber4 = data[3].split(" ")
number4 = initialNumber4[:]

for i in range(len(initialNumber4) - 1, -1 ,-1):
    if number4[i] == "":
        number4.pop(i)
    else:
        number4[i] = int(number4[i])

initialOperators = data[4].split(" ")
operators = initialOperators[:]
for i in range(len(initialOperators) - 1, -1 ,-1):
    if operators[i] == "":
        operators.pop(i)

for i in range(len(number1)):
    match operators[i]:
        case "+":
            result += number1[i] + number2[i] + number3[i] + number4[i]
        case "*":
            result += number1[i] * number2[i] * number3[i] * number4[i]

print(result)
