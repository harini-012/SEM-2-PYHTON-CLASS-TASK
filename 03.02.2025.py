#lambda arguments:expression
add=lambda a,b:a+b
print("The sum of two numbers is:",add(1,2))

#according to the variables the expression will change accordingly
add=lambda a,b,c:a+b+c
print("The sum of three numbers is:",add(1,2,3))

#space separated value in input .This cannot be used in for 
L1=list(map(int,input().split()))
square=list(map(lambda x:x**2,L1))
print(square)


#filter even numbers in a list

l2=list(map(int,input().split()))
even=filter(lambda x:x%2==0,l2)
print(list(even))

#sorting particular index
t=[(1,2),(2,3),(4,1)]
t1=sorted(t,key=lambda x:x[1])
print(t1)


#interview question:

Name=input("Enter the employee name").split()
Name=list(Name)
Salary=list(map(int,input("Enter the employee salary").split()))
phone_no=list(map(int,input("Enter the phone number").split()))

S=zip(Name,Salary,phone_no)

sort=sorted(S,key=lambda k:k[2])
print(sort)
