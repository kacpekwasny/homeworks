# Proszę znaleźć wyrazy początkowe zamiast 1,1 o najmniejszej sumie, aby w ciągu analogicznym
# do ciągu Fibonacciego wystąpił wyraz równy numerowi bieżącego roku.


# this is a generator
# it uses yield insted of a return
# u have to iterate through it
# id doesnt throw at you a massive list
# but instead element at a time
def genSmallestSums(stop):
    i = 1
    while i<=stop:
        part1 = 0
        part2 = i
        while part1<part2:
            part1 += 1
            part2 -= 1
            yield part1, part2
        i+=1

def hasNumber(start1, start2, number):
    i, j, nxt = start1, start2, start1 + start2
    if number in [i, j, nxt]:
        return True, [i, j, nxt]
    
    sequence = [i, j, nxt]
    # no else as it is unnecesary because of the return
    while True:
        i, j = j, nxt
        nxt = i+j
        sequence.append(nxt)
        if nxt == number:
            return True, sequence 
        if nxt > number:
            return False, []

def main():
    for i, j in genSmallestSums(2020):
        has, parts = hasNumber(i, j, 2020)
        if has:
            print(f"found for i={i}, j={j}")
            print(*parts, sep="\n")
            break
        else:
            print(f"tested for i={i}, j={j}")

if __name__ == "__main__":
    main()

