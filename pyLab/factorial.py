def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n-1)

def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result


print fac(int(raw_input("enter a number: ")))
#n = int( raw_input("enter a number "))
#fac(n)

#print "factorial is : ", factorial(n)

