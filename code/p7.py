global s1
s2=input()
s=list(s2)
n=len(s)
for i in range(0,n-1,2):
    s1=s[i]
    s[i]=s[i+1]
    s[i+1]=s1
s3=''.join(s)
print(s3)

