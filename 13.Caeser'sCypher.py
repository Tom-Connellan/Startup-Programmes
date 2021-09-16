#Task 13
sent = input("Enter a sentence: ")
sent = sent.lower()
length = len(sent)
final = ""
counter = 0

while counter < length:
    asci = ord(sent[counter])
    if asci == 122:
        asci = 97
    elif asci == 32:
        asci=32
    else:
        asci = asci + 1
    #endif
    final = final + str(chr(asci))
    counter = counter + 1
print(final)