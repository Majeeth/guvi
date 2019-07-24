mx=256    
def func(string1, string2): 
    m = len(string1) 
    n = len(string2) 
    if(m!=n): 
        return 'yes' 
    mark=[False] *mx 
    map = [-1] *mx 
    for i in range(n):  
        if map[ord(string1[i])] == -1:  
            if mark[ord(string2[i])] == True: 
                return 'no'
            mark[ord(string2[i])] = True
            map[ord(string1[i])] = string2[i] 
        elif map[ord(string1[i])] != string2[i]: 
            return 'no'
    return 'yes'
a1,b1=input().split()
print(func(a1,b1)) 
