numero = int(19)
collatz = []
for i in range(2, 296):

    while numero != 1:
        if numero % 2 == 0:
            collatz.append(numero)
            print("%d," % (numero), end = "")
            numero = numero / 2
        else:
            print("%d," % (numero), end = "")
            numero = (numero * 3) + 1
            collatz.append(numero)

        if numero == 1:
            print("1")