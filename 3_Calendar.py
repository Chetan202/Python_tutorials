import calendar

print(calendar.weekheader(3))
print(calendar.firstweekday())
print(calendar.month(2020,3))
print(calendar.monthcalendar(2020,3))
print(calendar.calendar(2020))
print(calendar.calendar(2050))

day_of_the_week=calendar.weekday(3000,8,1)
print(day_of_the_week)  

is_leap=calendar.isleap(2020)
print(is_leap)

how_many_leap_days=calendar.leapdays(2000,2005)
print(how_many_leap_days)