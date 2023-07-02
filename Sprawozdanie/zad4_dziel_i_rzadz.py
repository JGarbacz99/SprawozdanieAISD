def suma(l,r,A):
    w = r - l + 1
    if w == 1:
        return A[l]
    else:
        return (suma(l,r-w//2,A)+suma((r-(w//2)+1),r,A))

tab = [10,23,17,45,92,44,28,73,61,55]

print(suma(0,9,tab))
