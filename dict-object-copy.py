from dataclasses import dataclass


@dataclass
class TestClass:
    number: int
    letter: str

testList = [
    TestClass(1, 'A'),
    TestClass(2, 'B'),
    TestClass(3, 'C'),
    TestClass(4, 'D'),
    TestClass(5, 'E'),
    TestClass(6, 'F'),
]

testDictNums = {test_obj.number: test_obj for test_obj in testList}
testDictLets = {test_obj.letter: test_obj for test_obj in testList}

print(testDictNums)
print(testDictLets)

print(testDictNums[3] is testDictLets['C'])

print(id(testDictNums[3]))
print(id(testDictLets['C']))

newList = [
    1,
    2,
    3,
]

print(id(newList))

anotherNewList = newList

print(id(anotherNewList))

anotherNewList.pop(1)

print(id(newList))
print(id(anotherNewList))

anotherNewList = [num for num in anotherNewList]

print(id(anotherNewList))
