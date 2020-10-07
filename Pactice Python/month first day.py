import calendar
from datetime import datetime
date = datetime.today()
year = date.year
month = date.month

print(date)
print(month)
print(year)

last_month = month - 1
last = calendar.monthrange(year, last_month)[1]
print(last)