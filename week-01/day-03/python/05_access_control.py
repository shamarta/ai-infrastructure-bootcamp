age = int(input("Enter your age : "))

is_verified = True
is_banned = False

if age >= 18 and is_verified and not is_banned :
    print("access granted")

else :
    print("access denied")
