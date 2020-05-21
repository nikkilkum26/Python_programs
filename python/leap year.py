num = int(input("Enter Year: "))

if num % 4 == 0 and num % 100 != 0:
    print(num, "is a Leap Year")
elif num % 100 == 0:
    print(num, "is not a Leap Year")
elif num % 400 ==0:
    print(num, "is a Leap Year")
else:
    print(num, "is not a Leap Year")