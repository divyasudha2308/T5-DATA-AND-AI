1.prime number (recursive check)

def prime(n, i):
    if n <= 1:
        return False
    if i == n:
        return True
    if n % i == 0:
        return False
    return prime(n, i + 1)

num = int(input())
print("Prime" if prime(num, 2) else "Not Prime")


2.CLI Calculator

a=int(input("enter a number:"))
op=input("enter operator(+,-,*,/,%):")
b=int(input("enter a second number"))
if op=='+':
    print("result:",a+b)
elif op=='-':
    print("result:",a-b)
elif op=='*':
    print("result:",a*b)
elif op=='/':
    print("result:",a/b)
elif op=='%':
    print("result:",a%b)
else:
    print("invalid operator")

    
3.UserForm Validator

email=input("enter the mail :")
password=input("enter the password:")
name=input("Enter name:")
age=input("enter age:")
if '@' not in email:
    print("invalid mail")
elif len(password)<6:
    print("password is short")
elif not name.isalpha() and len(name)>2:
    print("enter name in characters and greater than 2 letters")
elif not age.isdigit() and age>0:
    print("enter age in numbers and greater than 0")
else:
    print("form submitted succesfully")


4. sys.argv – print program name & arguments

import sys

print("prog name:", sys.argv[0])
for i in range(1, len(sys.argv)):
    print(f"arg{i}:", sys.argv[i])

5. Script runs only if more than 2 arguments

import sys

if len(sys.argv) > 3:
    print("Running the program...")
    for i in range(1, len(sys.argv)):
        print(f"arg{i}:", sys.argv[i])
else:
    print("Not enough arguments! Need more than 2.")


6.Backup a file


import shutil
import datetime

source=r"C:\Users\divya\Desktop\cmr_opensource\data.txt"
backup=r"C:\Users\divya\Desktop\cmr_opensource\backupdata_{datetime.date.today()}.txt"

shutil.copy(source, backup)
print(f"Backup of {source} created at {backup}")

7.create a main folder


import shutil
import datetime
import os

source = "C:\Users\divya\Desktop\data.txt"

main_folder = "C:\Users\divya\Desktop\backups"
if not os.path.exists(main_folder):
    os.mkdir(main_folder)

timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
subfolder = f"{main_folder}/backup_{timestamp}"
os.mkdir(subfolder)

backup_file = f"{subfolder}/data_backup_{timestamp}.txt"
shutil.copy(source, backup_file)

print(f"Backup created at: {backup_file}")

8.backup only jpg file


import os
import shutil

source_folder = "C:/Users/divya/Desktop/images"

backup_folder = "C:/Users/divya/Desktop/backup_jpg"

if not os.path.exists(backup_folder):
    os.mkdir(backup_folder)

for file in os.listdir(source_folder):
    if file.lower().endswith(".jpg"):
        source_path = f"{source_folder}/{file}"
        backup_path = f"{backup_folder}/{file}"
        shutil.copy(source_path, backup_path)
        print(f"Copied: {file}")

print("Backup completed — all JPG files copied!")


9.tasks

print("1. Add Task")
print("2. View Tasks")

choice = input("Enter your choice: ")

if choice == "1":
    task = input("Enter task: ")
    with open("tasks.txt", "a") as f:
        f.write(task + "\n")
    print("Task added")

elif choice == "2":
    try:
        with open("tasks.txt", "r") as f:
            print("Your tasks:")
            print(f.read())
    except FileNotFoundError:
        print("No tasks found")

else:
    print("Invalid choice")



