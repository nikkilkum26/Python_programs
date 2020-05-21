a = float(input('Enter first side: '))
b = float(input('Enter second side: '))
c = float(input('Enter third side: '))
d = (a + b + c) / 2
area = (d*(d-a)*(d-b)*(d-c)) ** 0.5
print('The area of the triangle is %f' %area)