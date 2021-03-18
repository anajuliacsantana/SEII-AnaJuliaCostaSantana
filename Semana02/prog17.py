import datetime
import pytz



dt_mtn = datetime.datetime.now(tz=pytz.timezone('US/Mountain'))
print(dt_mtn.strftime('%B %d, %Y'))
