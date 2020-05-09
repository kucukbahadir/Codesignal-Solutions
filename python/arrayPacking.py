def arrayPacking(a):
    output = ["{0:b}".format(i).rjust(8,"0") for i in a]
    return int("".join(output[::-1]),2)