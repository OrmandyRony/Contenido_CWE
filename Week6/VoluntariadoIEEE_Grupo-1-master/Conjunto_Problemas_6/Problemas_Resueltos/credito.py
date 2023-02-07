import sys

def main():
    tarj_cred = obtenernum()

    validar(tarj_cred)

def obtenernum():
    while True:
        card_num = input("Número de tarjeta: ")
        try:
            if len(card_num) > 0 and int(card_num):
                break
        except ValueError:
            continue

    return card_num

def validar(tarj_cred):
    if len(tarj_cred) < 13 or 16 < len(tarj_cred):
        print("Invalido")
        sys.exit(0)
    par, impar = 0, 0
    largo = len(tarj_cred)

    if largo % 2 == 0:
        for i in range(largo):
            num = int(tarj_cred[i])
            if i % 2 == 0:
                multiple = num * 2
                if multiple >= 10:
                    par += multiple // 10
                    par += multiple % 10
                else:
                    par += multiple
            else:
                impar += num
    else:
        for i in range(largo):
            num = int(tarj_cred[i])
            if i % 2 != 0:
                multiple = num * 2
                if multiple >= 10:
                    par += multiple // 10
                    par += multiple % 10
                else:
                    par += multiple
            else:
                impar += num

    verificacion = (par + impar) % 10

    if verificacion == 0:
        prim_digito = int(tarj_cred[0])
        seg_digito = int(tarj_cred[1])
        if prim_digito == 3 and seg_digito == 4 or seg_digito == 7:
            print("AMEX")
        elif prim_digito == 5 and 1 <= seg_digito <= 5:
            print("MASTERCARD")
        elif prim_digito == 4:
            print("VISA")
        else:
            print("Invalido")

if __name__ == "__main__":
    main()