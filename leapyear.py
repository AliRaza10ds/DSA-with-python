year=int(input("Enter year"))
if year==0:
    print("invalid year,,please enter a valid year")
elif year %4==0:
    print(year,"is the leap year")
else:
    print(year,"is not a leap year")