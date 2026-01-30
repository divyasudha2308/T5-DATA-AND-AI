with open("log.log", "r") as file:
    for line in file:
        if "ERROR" in line:
            print(line.strip())
