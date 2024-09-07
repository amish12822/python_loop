"WAP to find the sum of first n numbers. (using while)"

num1 = int(input("Enter value: "))

count = 1
sum1 = 0
while count<=num1:
    sum1 = sum1 + count

    count += 1
print(sum1)