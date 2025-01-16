# strftime() is used to format the datetime by various specifiers
# converts datetime to strings
import datetime as dt
current_dt = dt.datetime.now()
datetime2 = current_dt.strftime("%A, %B %d, %Y, %I:%M:%S %p")
print(datetime2)

'''
Date
%Y = Year with century (e.g., 2025)
%y = Year without century (e.g., 25)
%m = Month as a zero-padded number (e.g., 01)
%d = Day of the month as a zero-padded number (e.g., 06)
%A = Full weekday name (e.g., Monday)
%a = Abbreviated weekday name (e.g., Mon)
%b = Abbreviated month name (e.g., Jan)
%B = Full month name (e.g., January)

Time
%H = Hour (24-hour clock, zero-padded, e.g., 14)
%I = Hour (12-hour clock, zero-padded, e.g., 02)
%p = AM or PM (e.g., PM)
%M = Minute (e.g., 30)
%S = Second (e.g., 45)
'''
