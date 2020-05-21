

class Parent:
    def func1(self):
        print(1)


class Child(Parent):
    def func2(self):
        print(2)


ob = Child()
ob.func1()
ob.func2()


