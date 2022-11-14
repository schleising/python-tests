from dataclasses import dataclass, asdict
import json

@dataclass
class Person:
    name: str
    age: int
    friends: list[str]

person1 = Person('Bob', 26, ['Jim', 'Stan', 'Tim'])

print(json.dumps(asdict(person1), indent=2))
