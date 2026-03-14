
#login system
correct_username="Akshat@12"
correct_password=1234

username1=input("enter the username:")
password1=int(input("enter the password:"))

if(username1==correct_username and password1==correct_password):
 print("login successful")
else:
 print("access denied")