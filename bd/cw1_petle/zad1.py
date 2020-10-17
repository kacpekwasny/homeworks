
i, j, nxt = 1, 1, 2

# default sep is " " (a space)
# but now args passed to print will be separated by
# a newline, this allows us to write single line
# insted of three
print(i, j, nxt, sep="\n")

while nxt<1000000-j:
    # i = j
    # j = nxt
    # same as above
    i, j = j, nxt
    nxt = i+j
    print(nxt)