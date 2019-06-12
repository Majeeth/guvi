x1,y1=map(int,input().split())
a=0
l=[]
for i in range(1,x1+1):
    print(i,end=' ')
    l.append(i)
for j in range(len(l)):
    if(j<y1):
        a+=l[j]
print('')        
print(a)
