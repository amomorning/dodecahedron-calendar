import datetime
import math
from ics import Calendar, Event

def is_prime(x):
    if x == 1: return False
    if x == 2: return True
    for i in range(2, int(math.sqrt(x))+2):
        if x % i == 0: return False
    return True

year = 2024



filename = f'primedays-{year}.ics'
c = Calendar()

start_date = datetime.date(year, 1, 1)
end_date = datetime.date(year, 12, 31)

delta = datetime.timedelta(days=1)
while start_date <= end_date:
    s = start_date.strftime('%Y%m%d')
    if is_prime(int(s)):
        e = Event()
        e.name = f'Prime day {s}'
        e.begin = start_date.strftime('%Y-%m-%d')
        e.make_all_day()
        c.events.add(e)
        print(s)
    start_date += delta

with open(filename, 'w') as f:
    f.writelines(c.serialize_iter())
