def process(line):
    print(line,string())
with open('file.txt','r') as f:
    for line in f:
        process(line)