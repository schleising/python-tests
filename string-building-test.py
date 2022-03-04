testString2 = 'Lots of empty seats at {ground}'

teamDict = {
    'team': 'Liverpool',
    'ground': 'Anfield',
}

print(testString2.format(**teamDict))
