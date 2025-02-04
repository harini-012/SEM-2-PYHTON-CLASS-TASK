#CONVERTING UPPER CASE AND LOWER CASE OUTSIDE THE LOOP

'''character=input()
if 'A'<=character<='Z':
    c=ord(character)+32
    converted=chr(c)
print(converted)'''

#CONVERTING INTO UPPER CASE TO LOWER CASE

def lower():
    l=""
    if i==" ":
            l+=" "
    
    else:    
        c=ord(i)+32
        converted=chr(c)
        l+=converted
        
    print(l,end="")
def upper():
    new=""
    
    if i==" ":
            new+=" "
    else:
            c=ord(i)-32
            converted=chr(c)
            new+=converted
    print(new,end="")
            

        
        

sentence=input("Enter the string")
for i in sentence:
        if 'A'<=i<='Z':
            lower()
        else:
            upper()

