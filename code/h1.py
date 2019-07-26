r=int(input())
l=[]   
x=[str(i) for i in input().split()]
s=''.join(x)
for i in s:
    a=s.count(i)    
    if(a>1):
        l.append(i)
b=set(l)
c=list(b)
for i in range(len(c)):
    c[i]=int(c[i])
c.sort()    
for j in range(len(c)):
    print(c[j],end=' ')
