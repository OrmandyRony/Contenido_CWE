def efectivo():
    v = float((input("Cambio debido: ")))
    if (v < 0): 
        print("Porfavor ingrese un cambio positivo")
        efectivo()
    else:
        print(round(v))  

efectivo()