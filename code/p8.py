lst=[]    
s1=input()
s=list(s1)
for i in range(len(s)):
    if(i==0):
        lst.append(s[i].upper())
    if(i!=0 and s[i-1]!=' '):
        lst.append(s[i])
    if(s[i]==' '):
        lst.append(s[i+1].upper())
s2=''.join(lst)
print(s2)
