#re module of verification of password

import re
def verify_password(password):
    ex=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?!.[@#$%^&*()]).{8,}$'

    if re.match(ex,password):
        print("Password is strong")
    else:
        print("Password is not strong")
password=input("Enter the password")
verify_password(password)
