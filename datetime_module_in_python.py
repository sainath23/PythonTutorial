import datetime

date = datetime.date(2017, 9, 11)
print(date)

# Print today's date
print(datetime.date.today())
print(datetime.date.today().isoweekday())

# date after 7 days
print(datetime.date.today() + datetime.timedelta(days = 7))

# time
print(datetime.time(9, 30, 45, 100000))

# datetime
print(datetime.datetime(2017, 9, 10, 9, 30, 45, 100000))

# today's date time
print(datetime.datetime.today())

# Datetime now
print(datetime.datetime.now())

print(datetime.timezone())