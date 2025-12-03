with open("input.txt" , "r" , encoding="utf-8") as f:
    banks = f.read().splitlines()


wynik = 0

for bank in banks:
    bank = list(bank)
    bank2 = bank[0 : len(bank)-1]
    L1 = max(bank2)
    bank = bank[bank.index(L1) + 1 : ]
    L2 = max(bank)
    L = 10*int(L1) + int(L2)
    wynik += L

print(wynik)