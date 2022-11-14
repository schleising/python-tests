import json
from typing import TypedDict

class TestClass(TypedDict):
    name: str
    age: int

person1: TestClass = {'name': 'Bob', 'age': 28}
print(type(person1))

with open('people.json', 'r', encoding='utf8') as inputFile:
    people: list[TestClass] = json.load(inputFile)

peopleList: list[TestClass] = []

for person in people:
    print(type(person))
    peopleList.append(person)

for person in peopleList:
    print(type(person))
