num= int(input("Enter your number"))
if num %5==0 and num %11==0:
    print("The number",num,"is divisible by both 5 and 11")
elif num %5==0 and num%11!=0:
    print ("The number",num,"is divisible by 5 but not by 11")
elif num %11==0 and num %5!=0:
    print("The number",num,"is divisible by 11 but not by 5")
else:
    print("The number",num,"is neither divisible by 5 nor 11")