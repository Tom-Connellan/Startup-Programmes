#Task 13
sent = input("Enter a sentence: ")
sent = sent.lower()
length = len(sent)
final = ""
counter = 0

while counter < length:
    asci = ord(sent[counter])
    if asci == 122:
        asci = 98
    elif asci == 121:
        asci = 97
    elif asci == 32:
        asci=32
    else:
        asci = asci + 2
    #endif
    final = final + str(chr(asci))
    counter = counter + 1
print(final)

## ACS Need more comments so we know what is going on.
## ACS - hello seems to cuase an error?