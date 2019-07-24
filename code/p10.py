s1,s2=input().split()
count=0
for i in range(len(s1)):
    if(s1[i]==s2[i]):
        count+=1
w=len(s1)-count
if(w==1):
    print('yes')
else:
    print('no')
