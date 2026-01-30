ip_address = []

with open("sample.log", "r") as log:
    lines = log.readlines()

    for line in lines:
        if "check" in line:
            words = line.split("[")
            ip_addr = words[1].split("]")
            ip_address.append(ip_addr[0].strip())  

with open("ip_addr_out.csv", "w") as ip:
    ip.write("IP_Address\n") 
    for addr in ip_address:
        ip.write(addr + "\n")

print("IP address extracted successfully")
