#print the following pattern
'''
    *
   * *
  *   *
 *     *
*********
'''
def hollow_pyramid(n):
    for i in range(1,n+1):
        space=" "*(n-i)#space calculation for the first row
        if i==1:
            print(space+"*")
        elif i==n:
            print("*"*(2*n-1))#2*5-1=10-1=9#first multiplication and then subtraction
        else:
            
            print(space+"*"+" "*(2*i-3)+"*")#middle rows=space+*+space+*
            
n=int(input("Enter the height of the pyramid"))
hollow_pyramid(n)

#print the following pattern

''' *
   ***
  *****
 *******
*********'''
def hollow_pyramid(n):
    for i in range(1,n+1):
        space=" "*(n-i)#space calculation for the first row
        if i==1:
            print(space+"*")
        elif i==n:
            print("*"*(2*n-1))#2*5-1=10-1=9#first multiplication and then subtraction
        else:
            
            print(space+"*"+"*"*(2*i-3)+"*")#middle rows=space+*+space+*
            
n=int(input("Enter the height of the pyramid"))
hollow_pyramid(n)
        
    
