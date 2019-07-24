global a1
a1=int(input())
if(a1==0):
    print('1')
if(a1!=0):
    for i in range(1,a1):
        a1*=i
if(a1!=0):
    print(a1)
