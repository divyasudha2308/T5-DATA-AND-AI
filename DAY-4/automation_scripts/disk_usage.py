import shutil

total, used, free = shutil.disk_usage("/")

t=total // (1024**3)
u=used // (1024**3)
f=free // (1024**3)
print("Total Storage:", t, "GB")
print("Used Storage:", u, "GB")
print("Free Storage:", f, "GB")

with open("automation_output.txt","w") as file:
    file.write(f"Total Storage: {t} GB\n")
    file.write(f"Used Storage: {u} GB\n")
    file.write(f"Free Storage: {f} GB\n")
print("added in document successfully")