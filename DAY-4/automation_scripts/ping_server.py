import os

servers = ["8.8.8.8", "google.com", "127.0.0.1"]

for server in servers:
    
    response = os.system(f"ping -n 1 {server} > nul")  


    if response == 0:
        print(f"{server} is UP")
    else:
        print(f"{server} is DOWN")
