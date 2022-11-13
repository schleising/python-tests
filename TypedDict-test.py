from typing import TypedDict

class MyDict(TypedDict):
    name: str
    age: int

person = MyDict(name='Bob', age=50)

print(person)

person['name'] = 'Jim'
person['age'] = 30

print(person)
