a = int(input("Podaj liczbe do zmiany na binarne: "))
def dec2bin(a):
    if a == 0:
        return '0'
    elif a < 0:
        return '-' + dec2bin(-a)
    else:
        return dec2bin(a // 2) + str(a % 2)
print(f'Liczba {a} po zmianie z systemu dziesiętnego na binarne ma postać {dec2bin(a)}')