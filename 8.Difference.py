#Task 8

#Asks the user for their two numbers
iNum1 = int(input("Enter your first number: "))
iNum2 = int(input("Enter your second number: "))

#Selection
if iNum1 > iNum2:
    print(iNum1, iNum2)
elif iNum2 > iNum1:
    print(iNum2, iNum1)
else:
    print(iNum1, iNum2)