user_num = int(input("Input your number: "))
factorial = 1
if user_num == 0:
    print("1")
else:
    for count in range (user_num, 1, -1):
        factorial = factorial * count
    print(factorial)