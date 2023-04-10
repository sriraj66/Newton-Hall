from datetime import *
from helpers import *
from django.utils.dateparse import parse_datetime

datetime_string = "2023-04-11 08:45:00+00:00"
dt = parse_datetime(datetime_string)

print(dt)
s =dt
e = datetime.now()+timedelta(days=3)

# print(s," ",e)
ns = format_date("2023-04-12T08:45")
ne = format_date("2023-04-15T08:45")
# print(ns," ",ne)

if(ns>s and ns<e):
    print("b/w")
