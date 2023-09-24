import random
print("Enter two numbers:")
m=int(input())
n=int(input())
x=random.randint(m,n)
print("It's your turn to guess")
print("Choices left:6")
for i in range(1,7):
    a=int(input("Enter your guess:"))
    if(a>x):
        print("The number is too high")
        print("Choices left:",6-i)
    elif(a<x):
        print("The number is too low")
        print("Choices left:",6-i)
    else:
        print("Congratulations! You guessed it right")
        break
if(a!=x):
    print("You couldn't make it out!")
    print("Random number generated is ",x)