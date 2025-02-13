#write

with open("C:\\Users\\HARINI RAJESH\\OneDrive\\Desktop\\New folder\\f1.txt","w") as f:
    f.write("File is in write mode\n")
print("File written successfully .Check your desktop")

#read
with open("C:\\Users\\HARINI RAJESH\\OneDrive\\Desktop\\New folder\\f1.txt","r") as f:
    filecontent=f.read()
    print(filecontent)

#append
with open("C:\\Users\\HARINI RAJESH\\OneDrive\\Desktop\\New folder\\f1.txt","a") as f:
    f.write("File functions")
