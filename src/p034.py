import locale
import calendar
from datetime import datetime

locale.setlocale(locale.LC_MONETARY, "")       # Monetary format (OS default)
locale.setlocale(locale.LC_TIME, "pt_BR")      # Time format (Brazil)
locale.setlocale(locale.LC_ALL, "pt_BR.utf8")  # All formats (Brazil, UTF-8)

now = datetime.now()
current_year = now.year
current_month = now.month
month_range = calendar.monthrange(current_year, current_month)

weekday_of_the_first_day_of_the_current_month = month_range[0]
weekday_name = calendar.day_name[weekday_of_the_first_day_of_the_current_month]
print(weekday_of_the_first_day_of_the_current_month, weekday_name)

last_day_of_current_month = month_range[1]
weekday_of_the_last_day_of_the_current_month = calendar.weekday(
    current_year, current_month, last_day_of_current_month)
weekday_name = calendar.day_name[weekday_of_the_last_day_of_the_current_month]
print(last_day_of_current_month, weekday_name)


print("-" * 80)
for i, week in enumerate(calendar.monthcalendar(current_year, current_month)):
    print(f"W{i+1}:", '[' + ', '.join(f"{day:3}" for day in week) + ']')


print("-" * 80)
print(calendar.month(current_year, current_month))

print("-" * 80)
print(calendar.calendar(current_year))
