global count
count=0  
n1,n2=input().split()
n1=int(n1)
n2=int(n2)
while(n1!=n2):
    for i in range(2,12):
        if(n1%i==0 and n1!=i):
            break
    else:
        count+=1
    n1+=1
print(count)
