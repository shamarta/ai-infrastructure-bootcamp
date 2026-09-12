def validate_password(password, min_length=8 , max_length=20):
    if len(password) < min_length:
        return False
    if len(password) > max_length:
        return False

    has_digit = False
    has_upper = False

    for char in password:
        if char.isdigit():
            has_digit = True
        elif char.isupper():
            has_upper = True    

    return has_digit and has_upper

print(validate_password("Abc12345"))              
print(validate_password("abc12345"))              
print(validate_password("ABCDEFGH"))                
print(validate_password("Ab1"))                 
print(validate_password("Password123"))           
print(validate_password("ThisPasswordIsWayTooLong1")) 
print(validate_password("shamarta123"))