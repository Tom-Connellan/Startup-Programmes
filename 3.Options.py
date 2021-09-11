#Task 3

valid = False
#Loop Function
while (valid == False):
    number = int(input("Input a number between 1 and 3: "))
    #Selection Function
    if number > 3 or number < 1:
        valid = False
    else:
        valid = True
number = str(number)
print("You chose option " + number)