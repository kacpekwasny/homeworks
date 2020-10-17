# Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
# liczba ta jest iloczynem dowolnych dwóch kolejnych wyrazów ciągu Fibonacciego.



def genFib():
    i, j, nxt = 1, 1, 2
    yield nxt
    while True:
        i, j = j, nxt
        nxt = i+j
        yield nxt


def multiplicationIsInFib(num):
    seq = [1,1]
    for i in genFib():
        print(seq)
        if seq[0]*seq[1] == num:
            return True, seq
        if seq[0]*seq[1]>num:
            return False, seq
        seq[0] = seq[1]
        seq[1] = i

if __name__ == "__main__":
    while True:
        try:
            num = int(input("Please type in an positive integer: "))
            break
        except ValueError:
            print("Positive integer only please!")
    out = multiplicationIsInFib(num)
    if out[0]:
        print(f"Found {out[1]}: {out[1][0]}*{out[1][1]}={out[1][0]*out[1][1]}")
    else:
        print(f"Not found, sequence left was: {out[1]}")
