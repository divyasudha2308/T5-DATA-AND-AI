import shutil
import datetime
import time
import os

src = r"C:\Users\divya\Desktop\DAY-4\automation_scripts\data.txt"


backup_root = r"C:\Users\divya\Desktop\DAY-4\backup"
os.makedirs(backup_root, exist_ok=True)

while True:
    now = datetime.datetime.now()

    if now.hour == 11 and now.minute == 43:
        dst = os.path.join(
            backup_root,
            "data_backup_" + now.strftime("%Y%m%d_%H%M%S") + ".txt"
        )

        shutil.copy(src, dst)
        print("Backup created:", dst)
        with open("automation_output.txt","a")as file:
            file.write(f"Backup created:, {dst}")
        time.sleep(60)  

    time.sleep(1)
    


