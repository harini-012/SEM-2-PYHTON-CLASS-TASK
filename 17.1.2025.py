
#reversing a string using recursion
string=input("Enter the string")
def reverse_string(string):
    if len(string)<=1:#rev
        return string
    return reverse_string(string[1:])+string[0]
res=reverse_string(string)
print(res)

#palindrome or not
string=input("Enter to check whether palindrome or not")
def palindrome(string):
    if len(string)<=1:
        return True
    
    if string[0]!=string[-1]:
            return False
    return palindrome(string[1:-1])
if palindrome(string):
    print("yes")
else:
    print("No")

#recursive function to print x^n
    
x=int(input("Enter the base"))
n=int(input("Enter the power"))
def power(x,n):
    if n==0:
        return 1
    else:
        return x*power(x,   n-1)
res=power(x,n)
print(res)

#recursive function to calculate sum
n=int(input("Enter the number to find the sum of its digits"))
def calculate(n):
    if n==0:
        return 0
    return n%10+ calculate(n//10)
ans=calculate(n)
print(ans)

#to calculate the sum of array
n=int(input("Enter the number of elements in the array"))
arr=[]
tot=0
for i in range(n):
    e=list(map(int,input().split()))
    arr.append(e)
for i in range(n):
    for j in range(n):
        print(arr[i][j],end=" ")
    print()
for i in range(n):
    for j in range(n):
        tot+=arr[i][j]
print(tot)

#to transpose

n=int(input("Enter the number of elements in the array:"))
arr=[]
for i in range(n):
    e=list(map(int,input().split()))
    arr.append(e)
print("Original matrix")
for i in range(n):
    for j in range(n):
        print(arr[i][j],end=" ")
    print()
print("Transpose")
for i in range(n):
    for j in range(n):
        print(arr[j][i],end=" ")
    print()


