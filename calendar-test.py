from calendar import TextCalendar
from datetime import date

cal = TextCalendar()

cal.prmonth(date.today().year, date.today().month)

print('------------------------')

cal.pryear(date.today().year)
