global s
n=int(input())
for i in range(2,12):
    if(n%i==0):
        s='yes'
        break
    else:
        s='no'
        continue
if(s=='yes'):
    print('yes')
else:
    print('no')
