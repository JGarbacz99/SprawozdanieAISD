n = int(input("Podaj n jako długość ciągu: "))
if n>0:
    ile_u = 0
    for i in range(n):

        if i<n:
            i += 1
            a = int(input(f'Podaj {i} liczbę: '))
            if a<0:
                ile_u += 1
            print(f'Wystąpiło {ile_u} liczb ujemnych')
else:
    print("Podaj n większe od 0")
