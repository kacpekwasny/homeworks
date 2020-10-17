# Proszę napisać program rozwiązujący równanie x x = 2020 metodą bisekcji.

import sys

def bisekcja(num, percentDifference):
    # alias
    prcd = percentDifference
    minn = 0
    maxx = num

    # when maxx is 2 big then we get overflow error
    # on x**x, thats why we try to reduce it to size that doesnt
    # raise an error
    while True:
        try:
            x = (maxx - minn)/2+minn
            pw = x**x
            break
        except OverflowError:
            maxx = maxx/1.1
    x = 1
    prevx = x
    while not (num*(100-prcd)/100 < x**x < num*(100+prcd)/100):
        x = (maxx - minn)/2+minn
        pw = x**x
        if pw==num:
            return x
        elif pw > num:
            maxx = x
        else: # num < pw
            minn = x
        if prevx == x:
            return x
        prevx = x
    return x

if __name__ == "__main__":
    print("python3 zad6.py <nr> <accurity in percent>\n  using 0 as accuracy will work :)")
    x = bisekcja(float(sys.argv[1]), float(sys.argv[2]))
    print(f"{x}**{x} = {x**x}")