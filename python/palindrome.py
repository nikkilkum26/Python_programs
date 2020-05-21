num=int(input("Enter a number:"))
temp=num
rev=0
while(num>0):
    a=num%10
    r=r*10+a
    num=num//10
if(temp==r):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")