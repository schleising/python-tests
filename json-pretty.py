import json

testDict: dict[int, dict[str, str]] = {
    4: {'inner4A': 'value4A', 'inner4B': 'value4B'},
    2: {'inner2A': 'value2A', 'inner2B': 'value2B'},
    3: {'inner3A': 'value3A', 'inner3B': 'value3B'},
    1: {'inner1A': 'value1A', 'inner1B': 'value1B'},
    6: {'inner6A': 'value6A', 'inner6B': 'value6B'},
    5: {'inner5A': 'value5A', 'inner5B': 'value5B'},
}

with open('test.json', 'w', encoding='utf8') as outputFile:
    json.dump(testDict, outputFile, indent=2)
