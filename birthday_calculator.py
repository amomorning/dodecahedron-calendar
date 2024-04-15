from zhdate import ZhDate
from datetime import datetime, timedelta


def same_solar_lunar_birthday(birth_year, birth_month, birth_day):
    birth_date = ZhDate.from_datetime(datetime(birth_year, birth_month, birth_day))

    ages = []
    dates = []
    for year in range(birth_year, 2100):
        zhdate = ZhDate.from_datetime(datetime(year, birth_month, birth_day))
        if(zhdate.lunar_day == birth_date.lunar_day and zhdate.lunar_month == birth_date.lunar_month):
            print(f'{year-birth_year}岁, {zhdate}, 公历{year}年{birth_month}月{birth_day}日')
            ages.append(year-birth_year)
            dates.append(datetime(year, birth_month, birth_day))
    return ages, dates

def datetime_to_ganzhi(date):
    gan = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛','壬', '癸']
    zhi = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未','申', '酉', '戌', '亥']

    zhdate = ZhDate.from_datetime(date)
    
    year_gan = (zhdate.lunar_year-4)%10
    year_zhi = (zhdate.lunar_year-4)%12

    #month
    month_gan = ((year_gan%5+1)*2+zhdate.lunar_month-1)%10
    month_zhi = (zhdate.lunar_month+1)%12
    
    #day 高氏日柱公式：格里历 -> 日柱
    if date.month <= 2:
        C = (date.year-1) // 100
        s = (date.year-1) % 100
        m = date.month + 12
    else:
        C = date.year // 100
        s = date.year % 100
        m = date.month
    x = (44*C+C//4+9)%60 # 世纪常数
    mb = 15*((-1)**(m)+1) + (3*m-7)//5 # 月基数
    day_zhu = s//4*6+5*(s//4*3+s%4) + mb + date.day + x - 1

    day_gan = day_zhu%10
    day_zhi = day_zhu%12

    #hour
    hour_zhi = (date.hour+1)//2%12
    hour_gan = ((day_gan%5)*2+hour_zhi)%10

    return gan[year_gan]+zhi[year_zhi]+gan[month_gan]+zhi[month_zhi]+gan[day_gan]+zhi[day_zhi]+gan[hour_gan]+zhi[hour_zhi]

def wuxing_of_ganzhi(ganzhi):
    gan = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛','壬', '癸']
    zhindex = {'子':4, '丑':2, '寅':0, '卯':0, '辰':2, '巳':1, '午':1, '未':2,'申':3, '酉':3, '戌':2, '亥':4}
    wuxing = ['木', '火', '土', '金', '水']


    ret = []
    for i in range(4):
        ret.append(wuxing[(gan.index(ganzhi[i*2]))//2])
        ret.append(wuxing[zhindex[ganzhi[i*2+1]]])

    return ''.join(ret)

def yinyang_of_ganzhi(ganzhi):
    gan = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛','壬', '癸']
    zhi = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未','申', '酉', '戌', '亥']
    ret = []
    for i in range(4):
        gan_idx = gan.index(ganzhi[i*2])
        ret.append('阴') if gan_idx%2 == 1 else ret.append('阳')
        zhi_idx = zhi.index(ganzhi[i*2+1])
        ret.append('阴') if zhi_idx%2 == 1 else ret.append('阳')
    return ''.join(ret)


def test_datetime(year, mon, day, hour):
    date = datetime(year, mon, day, hour)
    ganzhi = datetime_to_ganzhi(date)
    print(date.year, date.month, date.day)
    print(ganzhi)
    print(wuxing_of_ganzhi(ganzhi))
    print(yinyang_of_ganzhi(ganzhi))

    
if __name__ == '__main__':
    year = 2030
    start_date = datetime(year-10, 1, 1, 1)
    end_date = datetime(year+10, 12, 31, 1)
    delta = timedelta(hours=2)

    def allzhi(ganzhi):
        zhi = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未','申', '酉', '戌', '亥']
        # if ganzhi[0] == ganzhi[6] and ganzhi[2] == ganzhi[4] and ganzhi[1] == ganzhi[7] and ganzhi[3] == ganzhi[5]:
        #     return True
        for z in zhi:
            if ganzhi.count(z) == 4 and ganzhi.count(ganzhi[0]) == 4:
            # if ganzhi.count(z) == 4:
                return True
        return False

    while start_date <= end_date:
        try:
            ganzhi = datetime_to_ganzhi(start_date)
            if allzhi(ganzhi):
                print(start_date, "至", start_date+delta, ": " + ganzhi)
        except TypeError as e:
            pass
            # print(start_date, e)
        start_date += delta


