#Task 12
num = int(input("Please enter your integer: "))
counter = 2
numbs = "1"
while counter <= num:
    if num%counter == 0:
        numbs = numbs + ", " + str(counter)
    #endif
    counter = counter + 1
#endwhile
print(numbs)