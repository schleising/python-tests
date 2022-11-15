from datetime import date
import re

dateString = '2022-12-20'

dateRegex = re.compile('(202[0-9])-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])')

output = dateRegex.fullmatch(dateString)

if output is not None:
    year, month, day = (int(group) for group in output.groups())
    realdate = date(year, month, day)
    print(type(realdate))
    print(realdate)
else:
    print('No match')
