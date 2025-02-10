n=int(input())
s=0
n=str(n)
p=True
for i in n:
    if int(i)<2:
        p=False
    if int(i)==2:
        p=True
    elif int(i)>2:
        for j in range(2,int(i)):
            if int(i)%j==0:
                p=False
                break
            else:
                p=True
    if p:
       
        s+=int(i)
    
        
print(s)
                
            
