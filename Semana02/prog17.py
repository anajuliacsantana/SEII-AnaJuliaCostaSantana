import datetime

tday = datetime.date.today()

tdelta = datetime.timedelta(days = 7)

# print(tday - tdelta)

#date2 = date1 + timedelta
#timedelta = date1 + date2

bday = datetime.date(2022,3,2)

till_bday = bday - tday
print(till_bday)