from dataclasses import dataclass
from collections import Counter

@dataclass
class TestClass:
    key: str
    status: str

objList = [TestClass(str(count), 'Open' if count % 2 == 0 else 'Closed' if count % 3 == 0 else 'Other') for count in range(10)]

print(objList)

openList = [item for item in objList if item.status == 'Open']

print()
print(openList)

counter = Counter([item.status for item in objList])

print()
print(counter)

print(counter['Open'])