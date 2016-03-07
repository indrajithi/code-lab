def rec(val,n):
    if n==1:
        return val
    rec(n*n-1,n-1)
print rec(0,4)
