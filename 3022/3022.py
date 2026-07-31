"""chancetemperature"""
tem = float(input())
UNIT1 = str(input()).upper()
UNIT2 = str(input()).upper()
if UNIT1 == "C" and UNIT2 == "K":
    print(f'{tem + 273.15:.2f}')
elif UNIT1 == "K" and UNIT2 == "C":
    print(f'{tem - 273.15:.2f}')
elif UNIT1 == "K" and UNIT2 == "F":
    print(f'{((tem - 273.15)*9/5)+32:.2f}')
elif UNIT1 == "K" and UNIT2 == "R":
    print(f'{((tem - 273.15)+273.15)*9/5:.2f}')
elif UNIT1 == "F" and UNIT2 == "C":
    print(f'{(tem-32)*5/9:.2f}')
elif UNIT1 == "C" and UNIT2 == "F":
    print(f'{(tem*9/5)+32:.2f}')
elif UNIT1 == "F" and UNIT2 == "K":
    print(f'{((tem-32)*5/9) + 273.15:.2f}')
elif UNIT1 == "F" and UNIT2 == "R":
    print(f'{(((tem-32)*5/9)+273.15)*9/5:.2f}')
elif UNIT1 == "C" and UNIT2 == "R":
    print(f'{(tem + 273.15)*9/5:.2f}')
elif UNIT1 == "R" and UNIT2 == "C":
    print(f'{(tem*5/9)-273.15:.2f}')
elif UNIT1 == "R" and UNIT2 == "F":
    print(f'{(((tem*5/9)-273.15)*9/5)+32:.2f}')
elif UNIT1 == "R" and UNIT2 == "K":
    print(f'{((tem*5/9)-273.15) + 273.15:.2f}')
elif UNIT1 == UNIT2:
    print(f"{tem:.2f}")
