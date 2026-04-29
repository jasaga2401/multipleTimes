
def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    nlist = [x]
    total = x
    
    for times in range(n-1):

        total = total + x
        nlist.append(total)

    return nlist

x = 2
n = 5
print(count_by(x, n))
