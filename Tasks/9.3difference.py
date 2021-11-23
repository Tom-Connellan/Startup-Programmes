#Task 9

#Defining the 4 variables
counter = 1
#0 as it has to be a posotive integer and every number will be larger
biggest = 0
#Unless the numbers are larger than this, the smallest number will always be reasigned
smallest = 999999999999
middle = 0


while counter < 4:
    num = int(input("Please enter number #" + str(counter) +": "))
    if num > biggest:
        biggest = num
    else:
        middle = num
    #endif
    if num < smallest:
        smallest = num
    #endif
    counter = counter + 1
#endwhile
print(biggest, middle, smallest)