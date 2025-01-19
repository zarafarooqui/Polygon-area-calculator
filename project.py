#area of triangle

a=int(input("Enter First side"))
b=int(input("Enter Second side"))
c=int(input("Enter Third side"))

s=(a+b+c)/2

area=(s*(s-a)*(s-b)*(s-c))** 0.5

print("The area of triangle is %.2f" %area)