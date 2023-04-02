# Rules for Leap Year Calculation
# 1 year != 365 days
# 1 year ~= 365 and 1/4 days(which ain't precise either!)
# The idea of 365 and 1/4 days for a year would make a "leap year",
# once in  every 4 years. 
# But, it makes it a little too much! It makes 1 day extra for every 100 years.
# Therefore, we look for another rule, which is:
# "Skip the century" rule: 
# In every century, one leap year is diregarded(but this makes a day off, once in 400 years)
# So, here comes the final rule which takes the error to very low levels
#  Final rule: If the century is divisible by 400, then it is a leap year

year  = int(input("Enter a year: "))

if year % 4 == 0:
    isLeapYear = True
else:
    if year % 100 == 0:
        if year % 400 == 0:
            isLeapYear = True
        else:
            isLeapYear = False
    else:
        isLeapYear = True

if isLeapYear:
    print(f"The year {year}, is a Leap year!")
else:
    print(f"The year {year}, is not a Leap year!")
