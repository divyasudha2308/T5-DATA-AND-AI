# import threading

# def say_hello():
#     print("Hello from thread")
# t = threading.Thread(target=say_hello)
# t.start()
# t.join()

# print("task finished")


# import time
# def task():
#     print("task started")
#     time.sleep(2)
#     print("task completed")
# task()
# print("program finished")

# import threading
# def greet(name):
#     print(f"hello,{name}!")
# t=threading.Thread(target=greet,args={"divya"})
# # t.start()

# def greet(name):
#     print(f"hello,{name}")
# greet("divya")

# import time
# def greet(name):
#     time.sleep(3)
#     print("hello",name)
# name=input("enter name:")
# greet(name)


# import threading
# import time
# def worker(num):
#     print(f"worker {num} is running")
#     time.sleep(1)
#     print(f"worker {num} is finished")
# for i in range(5):
#     t=threading.Thread(target=worker,args=(i))
#     t.start()


# import urllib.request
# import threading
# import time
# def download_file():
#     url='http://127.0.0.1:5500/jk.txt'
#     filename='downloaded_text.txt'
#     print("starting download for file")
#     urllib.request.urlretrieve(url,'filename')
#     print("completed download for file")
# t=threading.Thread(target=download_file)
# t.start()
# print("main thread continues executing")



# import urllib.request
# import time

# def download_file():
#     url = "http://127.0.0.1:5500/jk.txt"
#     filename = 'download_test.txt'
#     print("starting download...")
#     urllib.request.urlretrieve(url, filename)
#     time.sleep(2)
#     print("download completed.")

# download_file()

# print("main program continues to run")


# import time 
# import threading
# import requests
# import json

# def download_file():
#     url = "https://fakestoreapi.com/products/1"
#     file = "posts.json"

#     time.sleep(1)
#     response = requests.get(url)
#     posts = response.json()   
#     with open(file, "w") as f:
#         json.dump(posts, f, indent=5)
#     print("Download complete!")

# t1 = threading.Thread(target=download_file)
# t1.start()

# print("Main thread continues to run while download is in progress.")

##WITH THREADING##
# import urllib.request
# import threading
# import time
# import json
# import ssl
# def download_json():
#     try:
#         print("connecting to api..")
#         time.sleep(2)
#         url="https://fakestoreapi.com/products"
#         headers={
#             "User-Agent": "Mozilla/5.0"
#         }
#         req=urllib.request.Request(url, headers=headers)
#         context=ssl._create_unverified_context()
#         with urllib.request.urlopen(req, context=context) as response:
#             data=response.read()
#         print("Data downloaded")
#         posts=json.loads(data)
#         with open('posts.json','w')as f:
#             json.dump(posts,f,indent=4)
#         print("starting download complete")
#     except Exception as e:
#         print("Error:", e)
# t=threading.Thread(target=download_json)
# t.start()
# print("Main thread continues execution")



##ITH THREADING##
import urllib.request
import time
import json
import ssl

def download_json():
    try:
        print("connecting to api..")
        time.sleep(2)
        url="https://fakestoreapi.com/products"
        headers={"User-Agent":"Mozilla/5.0"}
        req=urllib.request.Request(url,headers=headers)
        context=ssl._create_unverified_context()
        with urllib.request.urlopen(req,context=context) as response:
            data=response.read()
        print("Data downloaded")
        posts=json.loads(data)
        with open('posts.json','w') as f:
            json.dump(posts,f,indent=4)
        print("starting download complete")
    except Exception as e:
        print("Error:",e)

download_json()
print("Main thread continues execution")