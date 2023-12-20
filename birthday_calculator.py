from zhdate import ZhDate
from datetime import datetime
birth_year = 1996
birth_month = 12
birth_day = 18
birth_date = ZhDate.from_datetime(datetime(birth_year, birth_month, birth_day))
for year in range(birth_year, 2100):
    date = ZhDate.from_datetime(datetime(year, birth_month, birth_day))
    if(date.lunar_day == birth_date.lunar_day and date.lunar_month == birth_date.lunar_month):
        print(f'{year-birth_year}岁, {date}, 公历{year}年{birth_month}月{birth_day}日')
