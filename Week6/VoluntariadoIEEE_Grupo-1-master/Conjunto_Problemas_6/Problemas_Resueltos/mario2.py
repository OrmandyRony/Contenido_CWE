def piramide():
    print("A conituación ingrese la altura que desea de la piramide debe ser un numero entre 1 y 8")
    n = int(input("Altura: "))  

    if (n < 1):
        print("Porfavor ingrese un número valido entre 1 y 8")
        piramide()
    elif (n > 8):
        print("Porfavor ingrese un número valido entre 1 y 8")
        piramide()
    else:
        for i in range(0, n, 1):
            for j in range(1, (n - i), 1):
                print(" ", end="")
            for k in range(i+1):
                print("#", end="")
            print("  ", end="")
            for l in range(i+1):
                if l == i:
                    print("#")
                else:
                    print("#", end="") 

piramide()