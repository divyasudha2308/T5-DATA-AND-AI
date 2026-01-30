import re
with open("app.log", "r") as file:
    with open("divya.txt","w")as f:
        for line in file:
            if re.search(r"ERROR", line):
                f.write(line)
           
print("analysis completed")