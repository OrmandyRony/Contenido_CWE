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
        k = 2*n - 2

        for i in range(0, n):
            for j in range(0, k):
                    print(end=" ")
            k = k - 2
            for j in range(0, i+1):
                print("# ", end="")
            print("\r") 

piramide()