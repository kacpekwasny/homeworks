# Napisać program wyznaczający wartość do której zmierza iloraz dwóch kolejnych wyrazów
# ciągu Fibonacciego. Wyznaczyć ten iloraz dla różnych wartości początkowych wyrazów ciągu.


class Point:
    x = 0
    y = 0


def genFib():
    i, j, nxt = 1, 1, 2
    yield j
    yield nxt
    while True:
        i, j = j, nxt
        nxt = i+j
        yield nxt


def derivative(p1: Point, p2: Point):
    return (p2.y-p1.y)/(p2.x-p1.x)


def dirFib(steps):
    i = 1
    j = 1
    for nxt in genFib():
        pass







