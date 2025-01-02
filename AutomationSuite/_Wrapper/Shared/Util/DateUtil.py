import datetime

from .Utils import Utils


def get_date_serial(suffix_length=4):
    suffix = Utils().unique_string(suffix_length)
    serial = datetime.datetime.now().strftime('%d%H%M%S')
    return serial + suffix