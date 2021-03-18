import datetime
import pytz



dt_mtn = datetime.datetime.now(tz=pytz.timezone('US/Mountain'))
print(dt_mtn.strftime('%B %d, %Y'))

dt_str = 'March 18, 2021'
dt = datetime.datetime.strptime(dt_str,'%B %d, %Y')
print(dt)
#strftime - Datetime to String
# srtptime - String to Datetime