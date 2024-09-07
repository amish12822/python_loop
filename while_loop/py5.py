"Search for a number x in this tuple using loop:"

list2 = (1, 4, 9, 16, 25, 36, 49, 64, 81,100,9)

srch = int(input("Enter value: "))

count = 0
while count<len(list2):
    if (list2[count] == srch):
        print("Match with index:",count)
    count += 1
