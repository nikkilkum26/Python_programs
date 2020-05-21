
num = int(input("Enter a number: "))
a = len(str(num))
sum = 0

temp = num
while temp > 0:
   n = temp % 10
   sum += n ** a
   temp = temp//10

if num == sum:
   print(" Armstrong number")
else:
   print("Not an Armstrong number")