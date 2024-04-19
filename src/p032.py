from datetime import datetime
from pytz import timezone

now = datetime.now()
print("A)", now)

only_date = datetime(2024, 4, 18)
print("B)", only_date)

date_with_time = datetime(2024, 4, 18, 22, 7, 33)
print("C)", date_with_time)

'''
Directives:
https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
'''

my_date_time = "22h 14m 48s 18/04/2024"
my_dt_format = "%Hh %Mm %Ss %d/%m/%Y"

date_time_with_formatter = datetime.strptime(my_date_time, my_dt_format)
print("D)", date_time_with_formatter)

'''
Time zones:
https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
'''

with_timezone = datetime.now(timezone("America/Sao_Paulo"))
print("E)", with_timezone)

with_tz_spain = datetime.now(timezone("Europe/Madrid"))
print("F)", with_tz_spain)

custom_with_tz = datetime(2024, 4, 13, 13, 30, 20,
                          tzinfo=timezone("Australia/Canberra"))
print("G)", custom_with_tz)

'''
Unix time (since 00:00:00 UTC on 1 January 1970):
https://en.wikipedia.org/wiki/Unix_time
'''

my_time_stamp = custom_with_tz.timestamp()
print("H)", my_time_stamp)

from_timestamp = datetime.fromtimestamp(
    my_time_stamp, timezone("Australia/Canberra"))
print("I)", from_timestamp)
