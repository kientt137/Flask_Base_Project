from datetime import datetime
from pytz import timezone


def get_time_zone():
    list_time = {}
    fmt = "%Y-%m-%d %H:%M:%S"
    timezone_list = [
        {
            'key': 'utc',
            'timezone': 'UTC'
        },
        {
            'key': 'japan',
            'timezone': 'Japan'
        },
        {
            'key': 'asia_jakarta',
            'timezone': 'Asia/Jakarta'
        },
    ]
    for zone in timezone_list:
        now_time = datetime.now(timezone(zone['timezone']))
        list_time[zone['key']] = now_time.strftime(fmt)
    return list_time
