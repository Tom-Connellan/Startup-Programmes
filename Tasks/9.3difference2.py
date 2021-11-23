#Create an array of 3 numbers
num = [0, 0, 0]

#Set counter to 0 - for both arrays and loop
counter = 0

#Start the loop to fill the array
while counter < 3:
    #Asks the user to input the 3 numbers
    num[counter] = int(input("Input number #" + str(counter + 1) + ": "))
    counter = counter + 1
#Sorts the array from largest - smallest
num = sorted(num)
print(num)

## ACS SUing sorted isn't really yourn algorithm!!