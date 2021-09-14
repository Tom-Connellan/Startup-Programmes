#Task 10
sent = str(input("Input your sentence: "))
length = len(sent)
counter = 0
space = 1
while counter < length:
    if " " == sent[counter]:
        space = space + 1
    counter = counter + 1
print(space)