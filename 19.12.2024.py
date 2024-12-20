#regular expression

import re
word="Simple regular expression example regular"
result=re.findall("gula",word) #how many times the word  gula is in word
print(result)


space=re.search("\s",word)
print("\nThe first spalce is at:",space.start()) #position of the first space 
