# 1.Rozpocznij z pustym stosem.
# 2. Wczytaj ciąg znaków z nawiasami.
# 3. Przetwarzaj ciąg idąc od lewej do prawej.
# 4. Jeśli aktualny znak jest nawiasem otwierającym, wstaw go na stos.
# 5. Jeśli aktualny znak jest nawiasem zamykającym, ściągnij nawias otwierający z wierzchołka stosu.
# 6. Jeśli po dojściu do końca ciągu stos jest pusty i nie wystąpiły żadne błędy, nawiasy są poprawne.
from STOSY2 import Stack


def parChecker(symbolString):
    s = Stack()
    index = 0
    error = True
    while index < len(symbolString) and error:
        symbol = symbolString[index]
        symbol2 = symbolString[index]
        symbol3 = symbolString[index]
        if symbol == "(": s.push(symbol)
        elif symbol2 == "[": s.push(symbol2)
        elif symbol3 == "{": s.push(symbol3)
        else:
            if s.isEmpty(): error=False
            else: s.pop()
        index = index+1
    if error and s.isEmpty(): return True
    else: return False


print(parChecker('((()))'))
print(parChecker('((())))))'))
print(parChecker('(((()()()())))'))
print(parChecker('[[[]]]'))
print(parChecker('{{{}}}'))
print(parChecker('{}()[[][]]'))
print(parChecker('{}()[[][]])))'))

