n=int(input("Enter the number of elements in the array"))
arr=[]#[1 0 2 1]#[1 2 0 1]#[1 2 1 0]
for i in range(n):
    e=int(input("Enter the elements"))
    arr.append(e)
print(arr)
for i in range(len(arr)-1):#3
    if arr[i]==0:#arr[0] #arr[1]#arr 2
        arr[i],arr[i+1]=arr[i+1],arr[i]#arr[1],arr[2]=arr[2],arr[1] #arr[2],arr[3]=arr[3],arr[2]
    else:
        i+=1
print(arr)

n=int(input("Enter the number of elements in the array"))
arr=[]
for i in range(n):
    e=int(input("Enter the elements"))
    arr.append(e)
for i in range(len(arr)-1):
    if arr[i]==0:
        arr[i],arr[i-1]=arr[i-1],arr[i]
    else:
        i+=1
print(arr)




arr=[]
p=0
n=int(input("Enter the number of days"))
for i in range(n):
    e=int(input("Enter the buy and sell prizes"))
    arr.append(e)
print(arr)
length=len(arr)
for i in range(1,length):
    if arr[i]>arr[i-1]:
        p+=arr[i]-arr[i-1]
print(p)
    
