# pyright: strict
class TestClass:
    def __init__(self, one, two, three):
        self.one = one[1]
        self.two = two

    def foo(self):
        print("It's just a function")


test_class = TestClass(1, 2, 3)
test_class.foo()


def greeting(name):
    return 'Hello ' + name
