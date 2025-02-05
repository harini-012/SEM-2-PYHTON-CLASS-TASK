#Using non inbuilt function
def reverse(k):
    '''k=input("Enter the string to be reversed:").strip()'''
    length=0
    rev=""
    for i in k:
        length+=1
    for i in range(length-1,-1,-1):
        rev+=k[i]
    ''' print("The reversed string is:",rev)'''
    return rev
k=input("Enter the string to be reversed:").strip()
s=reverse(k)
print(s)


#replace the letter in a gien string
input_string=input("Enter the String:")  
to_replace=input("Enter a character which wyou wnat to replace:")
replace_with=input("Enter the character what you want to replace to the character:") 
replaced_string=""
for c in input_string:
    if c==to_replace: 
        replaced_string+=replace_with 
    else:
        replaced_string+=c
print("The replaced String is:",replaced_string)
