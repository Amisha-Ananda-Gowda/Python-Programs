n=int(input("Enter the number of elements:"))
num=[]
print("Enter ",n," Elements:")

for i in range(n):
    num.append(int(input()))
    
sum=0
product=1

for i in range(n):
    if(num[i]%2==0):
        sum+=num[i]
    else:
        product*=num[i]
print("Sum of even numbers= ",sum)
print("Product of odd numbers = ",product)