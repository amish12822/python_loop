"Search for a number x in this tuple using loop:"

list4 = (1, 4, 9, 16, 25, 36, 49, 64, 81,100)

ser = int(input("Enter value: "))

count = 0
for num1 in list4:
    if (num1 == ser):
        print("Match with index:",count)
    count += 1
