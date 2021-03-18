import datetime
import pytz



dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
# print(dt_utcnow)

dt_mtn = datetime.datetime.now()
mtn_tz = pytz.timezone('US/Mountain')

dt_mtn =mtn_tz.localize(dt_mtn)
# dt_east = dt_mtn.astimezone(pytz.timezone('US/Eastern'))

print(dt_mtn)

