vd=[0,1,2,5,6,8,9]
def fun(k):
    k=str(k)
    for i in k:
        if int(i) not in vd:
            return False
    return True

n = int(input())
if n < len(vd):
    print(vd[n-1])
else:
    count=len(vd)
    k=vd[-1]
    while(count<=n):
        k+=1
        if fun(k):
            count+=1
    print(k)
