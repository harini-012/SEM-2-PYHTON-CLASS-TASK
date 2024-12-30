'''1.Given a string in run-length encoded format, decode it.
Input : encoded = "3a2b1c"
Output: “aaabbc'''

input_string=input("Enter the string")
for i in range(len(input_string)):
    if input_string[i].isdigit():   
        print(int(input_string[i])*input_string[i+1],end="")
      
