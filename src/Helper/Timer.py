import pytz
from datetime import datetime
from pytz.exceptions import UnknownTimeZoneError


def get_current_date_time(timezone_str='UTC'):
    """
    Get current time in Datetime with certain timezone
    :param timezone_str: pytz timezone str

    :return str: current time
    """

    try:
        timezone = pytz.timezone(timezone_str)
        current_time = datetime.now(timezone)
    except UnknownTimeZoneError:
        current_time = datetime.now()
    return current_time


def get_current_date_time_str(str_format='%Y-%m-%d %H:%M:%S', timezone_str='UTC'):
    """
    Get current time in string format with certain timezone
    :param str_format: str
    :param timezone_str: pytz timezone str

    :return str: current time in string format
    """

    try:
        timezone = pytz.timezone(timezone_str)
        current_time = datetime.now(timezone).strftime(str_format)
    except UnknownTimeZoneError:
        try:
            current_time = datetime.now().strftime(str_format)
        except Exception:
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return current_time

