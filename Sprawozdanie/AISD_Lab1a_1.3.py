tab = [4,8,7,4,9,3,5,8]
x = int(input("Podaj wartość, której szukasz: "))

i = 0
while i < len(tab):
    if tab[i] == x:
        print("Podana wartość jest w tablicy.")
        break
    i += 1
else:
    print("Podana wartość nie występuje w tablicy.")
    # print(len(tab))