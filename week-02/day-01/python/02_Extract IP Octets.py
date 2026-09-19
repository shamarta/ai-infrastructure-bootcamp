def get_ip_octets(ip) :
    octets = ip.split(".")
    return octets
ip = input("Enter an IP address: ")
octets = get_ip_octets(ip)
print(octets)

