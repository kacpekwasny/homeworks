# Proszę napisać program sprawdzający czy istnieje spójny podciąg ciągu Fibonacciego o zadanej
# sumie.



import sys

def genFib():
    i, j, nxt = 1, 1, 2
    yield i
    yield j
    yield nxt
    while True:
        i, j = j, nxt
        nxt = i+j
        yield nxt
 
def hasSumFib(sum_):
    sequence = []
    for i in genFib():
        print("action append", sequence)
        sequence.append(i)
        suma = sum(sequence)
        if suma == sum_:
            return True, sequence
        if suma < sum_:
            # skip rest of code in this iteration and proceed
            # to next iteration
            continue
        while sum(sequence) >= sum_:
            if sum(sequence) == sum_:
                return True, sequence
            print("action del:", sequence)
            # pop deletes element of specified index
            # in this example it will be element under index 0
            # so it will be the oldest one
            if len(sequence)>1:
                sequence.pop(0)
            else:
                return False, []

if __name__ == "__main__":
    # in your commandline
    # python3 zad3.py 242786
    try:
        suma = sys.argv[1]
    except IndexError:
        raise IndexError("Please specify sum of sequence!")

    # Lets see what is this sys.argv
    print("sys.argv =", sys.argv)

    # if this part raises error it wont be showed but except
    # will be triggered
    try:
        suma = int(suma)
        if suma<1:
            raise ValueError
    except:
        # This will raise ValueError with set message
        raise ValueError("Wrong input! Positive Integers only")
    found, seq = hasSumFib(suma)
    if found:
        print("Found sequence!")
        print(seq)
    else:
        print("Not found!")


