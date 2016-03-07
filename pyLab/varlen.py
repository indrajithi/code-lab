def sumall(*args):
    r_sum, i = 0,0
    n = len(args)
    while(n):
       r_sum = r_sum + args[i]
       print i
       i += 1
       n -= 1
    print r_sum

if __name__ == '__main__':
    sumall(1,2,3,4,5)
