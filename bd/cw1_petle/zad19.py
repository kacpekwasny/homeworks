# Napisać program wyznaczający wartość liczby e korzystając z zależności: e = 1/0! + 1/1! +
# 1/2! + 1/3! + ...


import sys

def comp_e(x):
    reps = 0
    fac = 1
    facCont = 1
    elim = 2
    while reps<x:
        facCont += 1
        fac = facCont*fac
        elim = elim + 1/fac
        print(elim)
        reps += 1

if __name__ == "__main__":
    lim = sys.argv[1]
    comp_e(int(lim))