
class Parent():

    def __init__(self):
        self.value = 5+6

    def show(self):
        print(self.value)

class Child(Parent):

    def __init__(self):
        self.value = 4+6

    def show(self):
        print(self.value)


obj = Parent()
obj1 = Child()

obj.show()
obj1.show()
