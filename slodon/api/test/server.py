
class Parent:
    def __init__(self, test):
        self.name = 'parent'
        print("coming from here", test)

    def test2(self):
        pass

class Child(Parent):
    def test1(self):
        print(self.name)


child1 = Child('test')
child1.test2()