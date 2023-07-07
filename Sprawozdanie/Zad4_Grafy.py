def dijkstry(G, s):
    odleglosc = {v: float('inf') for v in G}
    odleglosc[s] = 0

    nieodwiedzone = set(G)

    while nieodwiedzone:
        min_odleglosc = float('inf')
        wierzch_min_odleglosc = None

        for v in nieodwiedzone:
            if odleglosc[v] < min_odleglosc:
                min_odleglosc = odleglosc[v]
                wierzch_min_odleglosc = v

        nieodwiedzone.remove(wierzch_min_odleglosc)

        for sasiad, waga in G[wierzch_min_odleglosc]:
            nowa_odleglosc = odleglosc[wierzch_min_odleglosc] + waga
            if nowa_odleglosc < odleglosc[sasiad]:
                odleglosc[sasiad] = nowa_odleglosc

    return odleglosc

G = {
    'A': [('B', 5), ('C', 3)],
    'B': [('A', 5), ('C', 2), ('D', 1)],
    'C': [('A', 3), ('B', 2), ('D', 4), ('E', 6)],
    'D': [('B', 1), ('C', 4), ('E', 8)],
    'E': [('C', 6), ('D', 8)]
}

start = 'A'

odleglosc = dijkstry(G, start)
print("Odległości od wierzchołka", start, "do pozostałych wierzchołków:")
for wierzcholek, odleglosc in odleglosc.items():
    print("Wierzchołek", wierzcholek, ":", odleglosc)