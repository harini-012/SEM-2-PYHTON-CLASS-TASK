'''1. Find the Missing Number
Given an array of n-1 numbers in the range 1 to n, find the missing number.
Example:
arr = [1, 2, 4, 5]
# Missing number is 3'''



missing=True
value=0

arr=list(map(int,input().split()))
for i in range(len(arr)-1):
    if arr[i+1]-arr[i]==1:
        missing=False
    else:
        missing=True
        value=arr[i]
        break
        
if missing:
    print(value+1)
else:
    print("no missing values")

'''2. Find the Duplicates
Given an array where each number appears twice except one number, find the number that appears once.
arr = [4, 3, 2, 7, 8, 2, 3]
# 4 and 7 are the numbers that appear once'''



arr=list(map(int,input().split()))
app={}
for i in arr:
    if i in app:
        app[i]+=1
    else:
        app[i]=1

result=[]
for i ,j in app.items():
    if j==1:
        result.append(i)
print(result)

'''3. Check if Array is Sorted
Check whether a given array is sorted in ascending order.

Example:
arr = [1, 2, 3, 4]'''
# Output: True

arr=list(map(int,input().split()))
asc=True
for i in range(len(arr)-1):
    if arr[i+1]-arr[i]>0:
        asc=True
    else:
        asc=False
        break
print(asc)

'''4. Find the Majority Element
Given an array, find the majority element (the element that appears more than n//2 times).

Example:
arr = [3, 3, 4, 2, 4, 4, 2, 4, 4]
# Output: 4'''

arr=list(map(int,input().split()))
count={}
for i in arr:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
major=len(arr)//2
e=None
for i,j in count.items():
    if j>major:
        e=i
        break
print(e)

'''5. Check for Balanced Array
Given an array, check whether the sum of elements on the left is equal to the sum of elements on the right at any index.

Example:
arr = [1, 2, 3, 4, 10, 1, 2, 3]
# Output: True'''

def check_balanced_array(arr):
    total_sum = sum(arr)
    left_sum = 0
    equ=True

    for num in arr:
        
        if left_sum == total_sum - left_sum - num:
            equ=True
            return equ
        
        
        left_sum += num

        

    

arr = [1, 2, 3, 4, 10, 1, 2, 3]
print(check_balanced_array(arr))


'''6. Find All Pairs in an Array that Sum to a Specific Target
Given an array of integers and a target sum, find all pairs of numbers that sum up to the target.

Example:
arr = [2, 4, 3, 5, 7, 8]
target = 10
# Output: [(2, 8), (3, 7)]'''

arr=list(map(int,input().split()))
target=10
pairs=[]
for i in range(len(arr)-1):#5
    for j in range(i+1,len(arr)):#1,6
        if arr[i]+arr[j]==target:#0,1#0,2#0,3#0,4#0,5
            pairs.append((arr[i],arr[j]))

print(pairs)

        
    
    
    
