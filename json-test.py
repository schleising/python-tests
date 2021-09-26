from dataclasses import dataclass
import json

@dataclass
class Test:
    x: int
    y: float
    z: str

class TestEncoder(json.JSONEncoder):
    def default(self, object):
        if isinstance(object, Test):
            return object.__dict__
        else:
            # call base class implementation which takes care of
            # raising exceptions for unsupported types
            return json.JSONEncoder.default(self, object)

l1 = [Test(r, r*r, str(r)) for r in range(20)]

print(l1)

string = TestEncoder().encode(l1)

print(string)
