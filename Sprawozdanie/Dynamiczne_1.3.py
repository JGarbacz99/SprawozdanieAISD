# def S(n):
#     if n == 0 or n == 1:
#         return 1
#     if n > 1:
#         return 2 * S(n-1) - S(n-2)
#
# wynik = S(5)
# print(f'N-ty wyraz ciągu: {wynik}')

# def S(n):
#     if n == 0 or n == 1:
#         return 1
#     if n > 1:
#         return 2 * S(n-1) - S(n-2)
#
# wynik = S(5)
# print(f'N-ty wyraz ciągu: {wynik}')

def nty(n):
    if n == 0: return 1
    elif n == 1: return 1
    elif n>1:
        nty = [0, 1]
        i = 2
        while (i<=n):
            nty.append(nty[i-1]-nty[i-2])
            i+=1
    return nty[i-1]

n = int(input("Podaj n: "))
if (n>=0): print(nty(n))
else: print("Podano zly argument")