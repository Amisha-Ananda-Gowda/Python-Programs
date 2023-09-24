def circle(r):
    return 3.142*r*r
def square(s):
    return s*s
def rectangle(l,b):
    return l*b
print("Choices\n1.Area of Circlr\n2.Area of Square\n3.Area of Rectangle\nEnter your choice")
choice=int(input())
match choice:
    case 1:
        r=int(input("Enter the radius of the circle:"))
        print("Area of circle = ",circle(r))
    case 2:
        s=int(input("Enter the side of the square:"))
        print("Area of square = ",square(s))
    case 3:
        l=int(input("Enter the length of the rectangle:"))
        b=int(input("Enter the breadth of the rectangle:"))
        print("Area of circle = ",rectangle(l,b))
    case default:
        print("Invalid Choice!")