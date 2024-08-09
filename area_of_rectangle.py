length = eval(input("Enter the length of the rectangle:"))
breadth = eval(input("Enter the breadth of the rectangle:"))
if length > breadth:
    area = length * breadth
    print(f"The area of the rectangle is: {area}")
else:
    print(f"The length should be greater than the breadth.")
