def fib():
    limit = 4000000
    fst , lst, total = 0, 1, 0

    while(True):

        nxt = fst + lst
        fst = lst
        lst = nxt

        if nxt >= limit:
            break
       # print nxt
        if nxt % 2 == 0:
        #    print "          ", nxt
            total += nxt

    print "total = ",total

fib()
