x1=[]
x2=[]
k=int(input())
for i in range(0,k):
    x=([int(i) for i in input().split()])
    x1.extend(x)
x1.sort()
x1
for i in x1:
    c=str(i)
    x2.append(c)
x2
s=' '.join(x2)
print(s)
