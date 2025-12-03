with open("input.txt" , "r" , encoding="utf-8") as f:
    banks = f.read().splitlines()


wynik = 0

for bank in banks:
    
    L = []
    bank =  list(bank)
    for i in range(len(bank)):
        bank[i] = int(bank[i])
    for i in range(11,-1,-1):
        L.append(max(bank[: len(bank) - i]))
        bank = bank[bank.index(L[11 - i]) + 1 : ]
        
    num = 0
    for i in range(12):
        num = num*10 + int(L[i])
    wynik += num
print(wynik)