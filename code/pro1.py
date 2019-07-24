def string(str1, str2): 
    n1 = len(str1) 
    n2 = len(str2) 
    result = ""  
    j = 0
    i = 0
    while(i <= n1 - 1 and j <= n2 - 1): 
        if (str1[i] != str2[j]): 
            break
        result += (str1[i])           
        i += 1
        j += 1  
    return (result)   
def func(arr, n):
    arr.sort(reverse = False)  
    print(string(arr[0], arr[n - 1]))  
global s
s=[]
l=[]
n=int(input())
for i in range(n):
    a=input()
    s.append(a)
n = len(s)   
func(s, n) 
      
