from __future__ import annotations
from enum import Enum
from functools import total_ordering

import unittest

from pydantic import BaseModel, ValidationError


@total_ordering
class Status(str, Enum):
    STATE1 = "e"
    STATE2 = "d"
    STATE3 = "c"
    STATE4 = "b"
    STATE5 = "a"

    def __lt__(self: Status, other: Status) -> bool:
        ordered = {status: index for index, status in enumerate(list(Status))}
        return ordered[self] < ordered[other]

    def __eq__(self: Status, other: Status) -> bool:
        ordered = {status: index for index, status in enumerate(list(Status))}
        return ordered[self] == ordered[other]
    
    def __hash__(self) -> int:
        return hash(self.value)

    def __str__(self) -> str:
        return self.value


class Order(BaseModel):
    status: Status

    class Config:
        arbitrary_types_allowed = True


class TestStatus(unittest.TestCase):
    def test_order(self):
        order = Order(status=Status.STATE1)
        self.assertEqual(order.status, Status.STATE1)

    def test_ordering(self):
        self.assertLess(Status.STATE1, Status.STATE2)
        self.assertLess(Status.STATE2, Status.STATE3)
        self.assertLess(Status.STATE3, Status.STATE4)
        self.assertLess(Status.STATE4, Status.STATE5)

    def test_str(self):
        order1 = Order(status=Status.STATE1)
        self.assertEqual(str(order1.status), "e")
        order2 = Order(status=Status.STATE2)
        self.assertEqual(str(order2.status), "d")
        order3 = Order(status=Status.STATE3)
        self.assertEqual(str(order3.status), "c")
        order4 = Order(status=Status.STATE4)
        self.assertEqual(str(order4.status), "b")
        order5 = Order(status=Status.STATE5)
        self.assertEqual(str(order5.status), "a")

    def test_ordering_in_model(self):
        order1 = Order(status=Status.STATE1)
        order2 = Order(status=Status.STATE2)
        order3 = Order(status=Status.STATE3)
        order4 = Order(status=Status.STATE4)
        order5 = Order(status=Status.STATE5)

        self.assertLess(order1.status, order2.status)
        self.assertLess(order2.status, order3.status)
        self.assertLess(order3.status, order4.status)
        self.assertLess(order4.status, order5.status)

    def test_assignment(self):
        for status in list(Status):
            order = Order(status=status.value) # type: ignore
            self.assertEqual(order.status, status)

        self.assertRaises(ValidationError, Order, status="f")

if __name__ == "__main__":
    unittest.main()
