class Parent:
    def func1(self):
        print("Inheriting from Parent class")


class Child1(Parent):
    def func2(self):
        print("Inheriting from child 1")


class Child2(Child1):
    def func3(self):
        print("child 2")


ob = Child2()
ob.func1()
ob.func2()
ob.func3()