class TestClass(list):
    def __init__(self) -> None:
        self.x = 10

    def __str__(self):
        return('Poo')

x = TestClass()

x.append(1)
x.append(2)
x.append(3)

print(str(x))

print(x)
