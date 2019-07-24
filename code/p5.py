ch=input()
l=['I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII','XIII','XIV','XV','XVI','XVII','XVIII','XIX','XX']
for i in range(0,20):
    if(ch==l[i]):
        print(l.index(l[i+1]))
