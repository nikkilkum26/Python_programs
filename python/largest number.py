num1 = int(input("Enter number: "))
num2 = int(input("Enter number: "))
num3 = int(input("Enter number: "))

if (num1 >= num2) and (num1 >= num3):
   temp = num1
elif (num2 >= num1) and (num2 >= num3):
   temp = num2
else:
   temp = num3

print("largest number:", temp)