def fun(n):
    e = n//3
    q = n%3
    if n == 0:
        return '0'
    elif e == 0:
        return str(q)
    else:
        return fun(e) + str(q)
a=int(input())
print(fun(a))
