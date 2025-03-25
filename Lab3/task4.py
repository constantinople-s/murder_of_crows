import re


def change_date_format(text):
    date_dict = re.match(r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})", text).groupdict()
    return date_dict['day'] + '-' + date_dict['month'] + '-' + date_dict['year']
