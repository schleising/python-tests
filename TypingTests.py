from typing import List, Optional


stringList: List[Optional[str]] = [
    'abc',
    'def',
    'ghi',
    None,
    'jkl',
]

testString: Optional[str] = 'None'

if testString not in stringList:
    print('Not in list')
else:
    print('In list')

newString = ', '.join([item for item in stringList if item is not None and item not in 'def'])

print(newString)

splitString = newString.split(',')

for item in splitString: print(item)
