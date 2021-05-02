from dataclasses import dataclass

@dataclass
class DataClass:
    integer1: int
    float1: float
    string1: str

class NormalClass:
    def __init__(self, integer1: int, float1: float, string1: str):
        self.integer1 = integer1
        self.float1 = float1
        self.string1 = string1

    def testFunction(self):
        self.newVar: int = 7

def main() -> None:
    dataClass = DataClass(2, 5.8, 'Test Data Class')
    dataClassDict = dataClass.__dict__

    normalClass = NormalClass(3, 6.9, 'Test Normal Class')
    normalClassDict = normalClass.__dict__

    # normalClass.testFunction()
    normalClassDict['addedVar'] = 7.4

    print('Data Class')
    print(dataClass)
    print(dataClassDict)
    print()

    print('Normal Class')
    print(normalClass)
    print(normalClassDict)
    print()

if __name__ == '__main__':
    main()