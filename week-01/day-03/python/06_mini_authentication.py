admin_username = "sina"
admin_password = "1234"

user_username = "sara"
user_password = "9876"

guest_username = "david"
guest_password = "0000"

username = str(input("username : "))
password = str(input("password : "))
role = int(input("enter your role number:"))

if username == admin_username and password == admin_password and role == 1 :
    print("welcome admin")

elif username == user_username and password == user_password and role == 2 :
    print("welcome user")

elif username == guest_username and password == guest_password and role == 3 :
    print("welcome guest")

else :
    print("invalid user")