def triangle(x):
    if x < 0:
        count = x*-1
        while count > 0:
            print("#"*count)
            count = count - 1
    else:
        count = 0
    while count <= x:
        print("#"*count)
        count = count + 1
    return


triangle(-3)


