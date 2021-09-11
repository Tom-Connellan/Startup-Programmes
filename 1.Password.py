#Task 2

#Inputting their password
password = input("Please enter your password: ")

#Finding how many characters are in the password
Length = len(password)

#Determining if it's < or > than 6
if Length > 6:
    print("Password is valid")
else:
    print("Password is invalid")