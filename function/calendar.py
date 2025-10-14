import calendar 
year_input=int(input("Enter the year "))
month_input=int(input("Enter the month"))
cal=calendar.month(year_input,month_input)
print(cal)