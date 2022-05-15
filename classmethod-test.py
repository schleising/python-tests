class TestClass:
    classVariable = 4

    def __init__(self) -> None:
        print(self.classVariable)
        self.objectVariable = 5
    
    @classmethod
    def setClassVariable(cls, newVal: int) -> None:
        cls.classVariable = newVal

TestClass.setClassVariable(6)

testClass1 = TestClass()
testClass2 = TestClass()

print(f'TC1: {testClass1.classVariable}, {testClass1.objectVariable}')
print(f'TC2: {testClass2.classVariable}, {testClass2.objectVariable}')

print(testClass1.__dir__())

TestClass.setClassVariable(8)
testClass1.objectVariable = 9

print()
print(f'TC1: {testClass1.classVariable}, {testClass1.objectVariable}')
print(f'TC2: {testClass2.classVariable}, {testClass2.objectVariable}')
print(testClass1.__dir__())
