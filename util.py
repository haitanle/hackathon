from datetime import datetime
from dateutil import tz

def convertUTCtoLocal(time):

    utc = datetime.strptime(time, '%Y-%m-%dT%H:%M:%SZ')

    utc = utc.replace(tzinfo=tz.gettz('UTC'))
    local = utc.astimezone(tz.gettz('America/New York'))

    return local.strftime("%Y-%m-%dT%I:%M %p")


# print(convertUTCtoLocal('2019-06-07T19:00:00Z'))