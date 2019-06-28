global s
numn=int(input())
for i in range(2,12):
    if(numn==11):
        s='yes'
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
