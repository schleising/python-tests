from datetime import date

date1 = date(2021, 7, 9)
date2 = date.today()

print(f'It has been {(date2 - date1).days} days')
