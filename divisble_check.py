#divisible by 5 and 11 print divisible by both
#only by 5 print divisible by 5
#only by 11 print divisible by 11
#else print not divisible


num=int(input("enter a number:"))
if (num%5==0 and num%11==0):
    print("both are divisible")
elif (num%5==0):
    print("divisible by 5")
elif (num%11==0):
    print("divisible by 11")
else:
    print("not divisible")
    