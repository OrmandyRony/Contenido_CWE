Text = input("Ingrese su texto: ")

letras = 0
for i in Text:
    if (i >= "a" and i <= 'z') or (i >= "A" and i <= "Z"):
        letras += 1

palabras = 1
for i in Text:
    if (i == " "):
        palabras += 1

oraciones = 0
for i in Text:
    if i == "." or i == "¡" or i == "!" or i == "¿" or i == "?":
        oraciones += 1

L = (letras * (100/palabras))
s = (oraciones * (100/palabras))

indice = round(((0.0588 * L) - (0.296 * s) - 15.8))

if indice < 1:
    print("Antes del Grado 1")
elif indice > 16:
    print("Grado 16+")
else:
    print(f"Grado {indice}")