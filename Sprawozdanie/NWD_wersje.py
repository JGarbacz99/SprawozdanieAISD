# wersja I
# rozwiązanie iteracyjne
def NWD_iter(a,b):
    while a!=b:
        if a>b: a = a-b;
        else: b = b-a;
    return a

#rekurencja
def NWD(a,b):
    if a!=b:
        if a>b: return NWD(a-b,b)
        else: return NWD(a,b-a)
    return a

# wersja II
def nwd(a,b):
    while b!=0:
        temp = b;
        b = a % b
        a = temp
    return a
#wersja rek
def nwdrek(a,b):
    while b!=0:
        return nwdrek(b, a % b)
    return a