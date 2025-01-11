colors = [] 
color1 = input("Please enter your first color: ")
color2 = input("Please enter your second color: ")
color3 = input("Please enter your third color: ")


colors.append(color1)
colors.append(color2)
colors.append(color3)

size = len(colors)
count = 0

while count < size:
    print("Your " + str(count+1) + " color is: " + colors[count])
    count += 1

