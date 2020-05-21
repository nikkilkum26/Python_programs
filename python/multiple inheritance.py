class Parent1:
    def fun(self):
        print(1)
class Parent2:
    def fun1(self):
        print(2)
class Child(Parent1 , Parent2):
    def fun2(self):
        print(3)

ob = Child()
ob.fun()
ob.fun1()
ob.fun2()