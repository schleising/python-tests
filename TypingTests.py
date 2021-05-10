from typing import List, Optional

class BaseClass():
    @classmethod
    def PrintHello(cls) -> None:
        print(f'Hello from {cls.__name__}')

class NewClass(BaseClass):
    def __init__(self) -> None:
        super().__init__()
        self.x = 1

class NewerClass(BaseClass):
    def __init__(self) -> None:
        super().__init__()
        self.y = 1.7

def PrintClass(cls: BaseClass) -> None:
    cls.PrintHello()

oldClass = BaseClass()
newClass = NewClass()
newerClass = NewerClass()

PrintClass(oldClass)
PrintClass(newClass)
PrintClass(newerClass)

stringList: List[Optional[str]] = [
    'abc',
    'def',
    'ghi',
    None,
    'jkl',
]

testString: Optional[str] = 'None'

if testString not in stringList:
    print('Not in list')
else:
    print('In list')

newString = ', '.join([item for item in stringList if item is not None and item not in 'def'])

print(newString)

splitString = newString.split(', ')

for item in splitString: print(item)
