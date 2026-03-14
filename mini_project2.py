#  movue ticket checker
age =int(input("enter the age:"))
if (age<5):
    print("free")
elif (age>5 and age<18):
    print("child ticket")
elif (age>18 and age<60):
    print("adult")
else:
    print("senior discount")