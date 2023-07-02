def znajdz_najwiekszy(wektor):
    if len(wektor) == 1:
        return wektor[0]

    polowa = len(wektor) // 2
    lewa = wektor[:polowa]
    prawa = wektor[polowa:]

    max1 = znajdz_najwiekszy(lewa)
    max2 = znajdz_najwiekszy(prawa)

    if max1 > max2:
        return max1
    else:
        return max2

wektor = [5, 8, 2, 9, 1, 6, 10, 3]
najwiekszy_element = znajdz_najwiekszy(wektor)
print("Największy element w wektorze to:", najwiekszy_element)