n1=input()
n2=input()
len1=len(n2)
c=n2[len1-1]
count=0
for i in n1:
    if c==i:
        count+=1
print(count)
