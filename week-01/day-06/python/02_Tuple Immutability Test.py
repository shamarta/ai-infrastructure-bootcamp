SERVER_ADDRESS = ("10.0.0.5", 443)

print(SERVER_ADDRESS)        # Output: ('10.0.0.5', 443)
print(SERVER_ADDRESS[0])     # Output: 10.0.0.5 (IP)
print(SERVER_ADDRESS[1])     # Output: 443 (port)

# Try to change the port value — this should raise an error
SERVER_ADDRESS[1] = 8080