x1=[]
k=int(input())
for i in range(0,k):
    x=([str(i) for i in input().split()])
    x1.extend(x)
x1.sort()
s=' '.join(x1)
print(s)
