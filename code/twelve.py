n1=int(input())
dp=n1
r1=0
while(n1>0 and n<=1000):
    digt=n1%10
    r1=r1*10+digt
    n1=n1//10
if(dp==r1):
    print('yes')
else:
    print('no')
