#
# Example file for working with timedelta objects
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta


# construct a basic timedelta and print it
print(timedelta(days=365, hours=5,minutes=1))


# print today's date
now = datetime.now()
print("Today is: " + str(now))

# print today's date one year from now
print("Six months from now it will be: " + str(now + timedelta(days=180)))

# create a timedelta that uses more than one argument
print("In 2 days and 3 weeks, it will be:" + str(now + timedelta(days=2, weeks=3)))

# calculate the date 1 week ago, formatted as a string
t = datetime.now() - timedelta(weeks=1)
s = t.strftime("%A %B %d, %Y" )
print ("One week ago it was", s)

### How many days until April Fools' Day?
today = date.today()
print("Today is:", today)
xmas = date(today.year, 12,25)

# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year

afd = date(today.year, 4, 1)  # get April Fool's for the same year
# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year
if afd < today:
  print ("April Fool's day already went by %d days ago" % ((today-afd).days))
  afd = afd.replace(year=today.year + 1)  # if so, get the date for next year

# Now calculate the amount of time until April Fool's Day
time_to_afd = afd - today
print ("It's just", time_to_afd.days, "days until next April Fools' Day!")




if xmas < today:
    print("Christmas Day already went by %d days ago" % ((today-xmas).days))
    xmas = xmas.replace(year=today.year+1)


# Now calculate the amount of time until April Fool's Day  

time_to_xmas = xmas - today
print("It's just", time_to_xmas.days, "days until next Christmas!")