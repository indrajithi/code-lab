def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        res = fib(n -1 ) + fib (n-2)
        stack.append(res)
        return res
#for i in range(int(raw_input("enter a range:"))):
stack = []
i = int(raw_input("enter a range: "))
fib(i)
for j in range(i):
    print stack[j]
