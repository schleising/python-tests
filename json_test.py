import json

class TestClass:
    def __init__(self) -> None:
        self.x = 1
    test = 1
    class TestSubclass1:
        def __init__(self) -> None:
            self.y = 10
        sc1_var1 = 'Hello'
        sc1_var2 = 5

    class TestSubclass2:
        sc2_var1 = 'Bottom'
        sc2_var2 = 5.5

        class TestSubclass21:
            sc21_var1 = '10'
            sc21_var2 = 'Down in the details'

tc = TestClass()

json_string = json.dumps(tc, default=lambda x: vars(x))

print(vars(tc))
print('-----------')
print(json_string)
