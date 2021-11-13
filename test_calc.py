'''
This programme will be used to test the date calculator app
'''

from datetime import date, datetime
from datecalc import duration
from datecalc import when 

#Testing simple calculations
#This will test if the duration calculator correcting calculates the 4 days difference between the 1st - 5th November.
def test_duration_difference():
    start_date = date(2021,11,0o1)
    end_date = date(2021,11,0o5)
    # calculate the difference between the start and end dates
    days_difference = duration(start_date, end_date)
    #check it correctly calculates 4 days difference
    assert days_difference == 4

#This will test if the when calculator correcting calculates that 4 days after the 1st of November is the 5th
def test_when_difference():
    start_date = date(2021,11,0o1)
    days_between = 4
    #calculate the days between the start date is correct
    days_when = when(start_date, days_between)
    #check it correctly calculates the 5th November
    assert days_when == date(2021,11,0o5)

## testing negative numbers (calculating days in the past)
## would be nice if it said - x days
#This will test if the duration calculator correcting calculates the 4 days difference between the 5th - 1st November.
def test_duration_negative_difference():
    start_date = date(2021,11,0o5)
    end_date = date(2021,11,0o1)
    # calculate the difference between the start and end dates
    neg_difference = duration(start_date, end_date)
    #check it correctly calculates 4 days difference
    assert neg_difference == 4

#This will test if the when calculator correcting calculates that 4 days after the 5th of November is the 1st November
def test_when_negative_difference_two():
    start_date = date(2021,11,0o5)
    days_between = -4
    #calculate the days between the start date is correct
    days_when = when(start_date, days_between)
    #check it correctly calculates the 1st November
    assert days_when == date(2021,11,0o1)

# test zero difference in dates using datatime.now()
#This will test if the duration calculator correcting calculates that if both dates are the same using datetime now the difference will be zero
def test_duration_zero_difference():
    start_date = datetime.now()
    end_date = datetime.now()
    # calculate the difference between the start and end dates
    difference = duration(start_date, end_date)
    #check it correctly calculates 0 days difference
    assert difference == 0

#This will test if the when calculator correcting calculates that 0 days after the 5th of November is the same date 5th November
def test_when_zero():
    start_date = date(2021,11,0o5)
    days_between = 0
    #calculate the days between the start date is correct
    days_when = when(start_date, days_between)
    #check it correctly calculates the 5th November
    assert days_when == date(2021,11,0o5)
