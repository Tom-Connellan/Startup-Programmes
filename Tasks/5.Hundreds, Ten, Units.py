#Task 5

#Input the number
number = int(input("Please input an integer between 100 and 999: "))

#Calculating each digit
hund = number//100
ten = number //10
ten1 = ten%10
dig = number%ten

#showing the results
print(hund, ten1, dig)

##ACS VEry good. Perghaps a better print at the end e.g. 3 hundreds, 2 tens ...