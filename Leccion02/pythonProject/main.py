nota = int(input("Ingrese su nota de 0 a 10: "))

while nota >= 0 and nota <= 10:

    if 9 <= nota <= 10:
        print("A")
        break
    elif 8 <= nota <= 9:
        print("B")
        break
    elif 7 <= nota <= 8:
        print("C")
        break
    elif 6 <= nota <= 7:
        print("D")
        break
    elif 0 <= nota <= 6:
        print("F")
        break

print("Valor incorrecto")

