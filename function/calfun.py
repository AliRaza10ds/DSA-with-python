import calendar
def show_calendar(year,month):
    if year >0 and month <12 :
        return calendar.month(year,month)
    else:
        return "Invalid year or month name..please enter a valid year or month "

year_input=int(input("Enter the year: "))
month_input=int(input("Ente the month: "))
result=show_calendar(year_input,month_input)
print(result)