import datetime as dt
import time

print(dt.datetime.now())    # gives cuurent date and time
print(dt.date(2029,1,24))   # converts arguments into a date
print(dt.date.today())      # gives current date

date1 = dt.datetime.now()
print("Year:",date1.year)
print("Month:",date1.month)
print("Day:",date1.day)
print("Hour:",date1.hour)
print("Minute:",date1.minute)
print("Seconds:",date1.second)
print("Microseconds:",date1.microsecond)

time1 = dt.time(10,26,29,1495)  # converts arguments into time (Hour:Minute:Second:Microsecond)
print(time1)

# print datetime left for your birthday
current_dt = dt.datetime.now()
birthday_dt = dt.datetime(2025,9,21)

days_left = birthday_dt - current_dt
print(f"Datetime left for your birthday = {days_left}")

print("Hello")

t = time.sleep(5)   # stops program for the given time 
print("bye")