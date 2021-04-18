from typing import NamedTuple


class TestClass(NamedTuple):
    name: str = 'Steve'
    age: int = 45

    def __str__(self) -> str:
        return(f'Name: {self.name}\nAge : {self.age}')

    def __repr__(self) -> str:
        return(f'Age : {self.age}\nName: {self.name}')

test = TestClass()

print(test)
