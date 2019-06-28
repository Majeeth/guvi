global s
numn=int(input())
for i in range(2,12):
    if(n==11):
        s='no'
        break
    if(numn%i==0):
        s='no'
        break
    else:
        s='yes'
        continue
if(s=='no'):
    print('no')
else:
    print('yes')
