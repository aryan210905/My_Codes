# converts strings to datetime object

import datetime as dt
string = "21 June 2005"
current = dt.datetime.strptime(string,"%d %B %Y")
print(current)