def f(a,L = []):
    L = []
    L.append(a)
    return L

def call():
    print f(1)
    print f(2)

print f(0)
call()
