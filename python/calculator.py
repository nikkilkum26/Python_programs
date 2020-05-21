
def add(x, y):
	return x + y

def sub(x, y):
	return x - y

def mul(x, y):
	return x * y

def div(x, y):
	return x / y

def power(x, y):
    return x ** y
def fact(num):

    f = 1
    while num > 0:
        f = f * num
        num = num - 1
    return f
def lam(x,y):
    return (lambda x, y: x + y)(x,y)

def lam1(x,y):
    return (lambda x, y: x * y)(x,y)
print("Please select operation -\n" 
      "1. Add\n" 
		"2. Subtract\n" 
		"3. Multiply\n" 
		"4. Divide\n"
       "5.Power\n"
      "6.Factorial\n"
      "7.Lambda_ADDITION\n"
      "8.Lambda_MULTIPLICATION")



select = input("Select operations form 1, 2, 3, 4 , 5, 6, 7, 8:")



if select == '1':
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))
    print(n1, "+", n2, "=", add(n1, n2))

elif select == '2':
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))
    print(n1, "-", n2, "=", sub(n1, n2))

elif select == '3':
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))
    print(n1, "*", n2, "=", mul(n1, n2))

elif select == '4':
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))
    print(n1, "/", n2, "=", div(n1, n2))

elif select == '5':
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))
    print(n1, "^", n2, "=", power(n1, n2))

elif select == '6':
    num = int(input("Enter a number :"))
    print(num,"!=",fact(num))
elif select == '7':
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))
    print(n1, "+", n2, "=", lam(n1, n2))
elif select == '8':
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))
    print(n1, "*", n2, "=", lam1(n1, n2))

else:
	print("Invalid input")
