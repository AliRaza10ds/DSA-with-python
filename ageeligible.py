age=int(input("Enter yourt age"))
if age==0 or age<0:
    print ("Invalid age,,please enter a valid age")
elif age>18:
    print("you are eligible for vote")
else:
    print("You are not eligible for vote")