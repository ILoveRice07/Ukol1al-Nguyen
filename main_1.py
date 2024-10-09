#vytvoření pole
array = [ 4, 54, 62, 8, 96, 20, 71, 39, 82]

#vypsání první, prostřední a poslední hodnoty
delka_pole = len(array)
prvni = array[0]
prostredni = array[int(delka_pole/2)]
posledni = array[-1]

print("První číslo:", prvni)
print("Prostřední číslo:", prostredni)
print("Poslední číslo:", posledni)

#výměna 5. indexové hodnoty za číslo 34
array[5] = 34

#vypsání 7 indexové hodnoty
print("7. indexová hodnota:", array[7])

#vypsání délky pole
print("Délka pole je", delka_pole ,"hodnot.")

#vypsání maximální a minimální hodnoty
print("Maximální hodnota:", max(array))
print("Minimální hodnot:", min(array))

#vytvoření druhého pole
array_dva = [ 7, 1, 92, 75, 81, 93, 56, 18,] 

#sečtení a vypsání pole
soucet = sum(array_dva)
print("Soucet pole:", soucet)

#sečtení indexových hodnot 1 a 5
soucethodnot = array_dva[1] + array_dva[5]
print("Součet indexových hodnot 1 a 5:", soucethodnot)