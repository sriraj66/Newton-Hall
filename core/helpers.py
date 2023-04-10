from datetime import datetime, timedelta

def format_min_max(date):
    return f"{date.year}-{ date.month if date.month>=10 else '0'+str(date.month)}-{ date.day if date.day>=10 else '0'+str(date.day)}-T{date.hour}:{date.minute}"

def format_date(date_string):
    date_format = '%Y-%m-%dT%H:%M'

    datetime_obj = datetime.strptime(date_string, date_format)

    return datetime_obj
