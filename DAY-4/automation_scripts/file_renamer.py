import os

old_file = r"C:\Users\divya\Desktop\DAY-4\automation_scripts\automation_output.txt"
new_file = os.path.join(os.path.dirname(old_file), "outputs_file.txt")
os.rename(old_file, new_file)

print("File renamed successfully!")