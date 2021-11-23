#Task 11

time = str(input("Input the time (Hours, Minutes, Seconds): "))
    
hours, minutes, seconds = time.split(':')
hours = int(hours) * 60 * 60
minutes = int(minutes) * 60 * 60
seconds = int(seconds)
print(hours + minutes + seconds)

## ACS = Good work