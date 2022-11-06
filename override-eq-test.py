from __future__ import annotations

# When overriding __eq__ for a mutable Class accept that the resultant object is no longer hashable,
# there's no good way around this as,
# 1. An object's hash must not chnage during its lifetime
# 2. If objectA == objectB, hash(objectA) == hash(objectB) MUST also be true

class NewClass:
    def __init__(self, a: int, b: int) -> None:
        self.a = a
        self.b = b

    def __eq__(self, other: NewClass) -> bool:
        return self.a == other.a and self.b == other.b

object1 = NewClass(1,2)
object2 = NewClass(4,5)

# obj1hash = hash(object1)
# obj2hash = hash(object2)

object1.b = 9
object2.a = 6

# assert(hash(object1) == obj1hash)
# assert(hash(object2) == obj2hash)

print(object1 == object2)
print(object1 != object2)

object2.a = object1.a
object2.b = object1.b

print(object1 == object2)
print(object1 != object2)
