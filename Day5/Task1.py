def CheckIngredient(ingredient):
    
    ingredient = int(ingredient)
    for j in fresh:
        j = j.split("-")
        freshStart = int(j[0])
        freshEnd = int(j[1])
        if ingredient >= freshStart and ingredient <= freshEnd:
            return True
    return False


with open("input.txt" , "r" , encoding="utf-8") as f:
    input = f.read().split("\n\n")

wynik = 0
fresh = input[0].splitlines()
ingredients = input[1].splitlines()


for i in ingredients:
    if CheckIngredient(i) == True:
        wynik += 1

    
print(wynik)