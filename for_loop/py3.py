"WAP to find the factorial of first n numbers. (using for)"

num1 = int(input("Enter value: "))

fac = 1
for num2 in range(1, num1+1):
    fac = fac * num2

print(fac)
