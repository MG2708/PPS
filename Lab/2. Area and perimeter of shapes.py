#Area and perimeters of Circle, Square, Triangle, Rectangle
#Date 17/11/21

print("Calculating the Area and Perimeter of selected Shape!")
a=input("Select shape from Circle / Rectangle / Square / Triangle: ")
if a == "Circle" or a == "circle":
    r = eval(input("Enter Radius of the circle: "))
    area = 3.14*r*r
    p = 2*3.14*r
elif a == "Square" or a == "square":
    s = eval(input("Enter side of the square: "))
    area = s*s
    p = 4*s
elif a == "Rectangle" or a == "rectangle":
    l = eval(input("Enter length of the rectangle: "))
    b = eval(input("Enter breadth of the rectangle: "))
    area = l*b
    p = 2*(l+b)
else :
    print("Invalid Inputs, Recheck !!")

print(f' The area of the entered shape {a} based on inputs is {area}')
print(f' The perimemter of the entered shape {a} based on inputs is {p}')
    
