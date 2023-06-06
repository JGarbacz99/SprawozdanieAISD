import math

a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
c = int(input("Podaj c: "))
if a != 0:
    delta = b * b - 4 * a * c
    if delta > 0:
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        print(x1, x2)
    elif delta == 0:
        x1 = -b / (2 * a)
        print(x1)
    else:
        print("Brak rozwiązań rzeczywistych")
else:
    print("To nie jest równanie kwadratowe")