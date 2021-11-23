values= input("Input the width, height and breadth of the room in m: ")
width, height, breadth = values.split(" ")
unpaint = int(input("What is the area of the unpaintable areas? "))
surface_area = 2 * (int(breadth) * int(height)) + 2 * (int(width) * int(breadth)) + 2 * (int(height) * int(width))
surface_area = surface_area - unpaint
litre = surface_area//11 + 1
print("You need " + str(litre) + " litres of paint")
coats = int(input("How many coats of paint do you want? "))
total = litre * coats
print("You need " + str(total) + " litres of paint in total")