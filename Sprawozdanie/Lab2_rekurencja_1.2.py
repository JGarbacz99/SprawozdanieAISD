tab = [1,2,3,4,5]

def odwr_tab(tab):
    dlugosc = len(tab)
    if dlugosc <= 1:
        return tab
    else:
        a_element = tab[0]
        b_elementy = tab[1:]
        odwr_b_element = odwr_tab(b_elementy)
        odwr_b_element.append(a_element)
        return odwr_b_element

print(f'Odwrócona tablica: {odwr_tab(tab)}')
