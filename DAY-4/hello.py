# # regular expressions
# import re
# text="python is powerful"
# result=re.match("python",text)
# if result:
#     print("match found:",result.group())


# text="my number is 1234567890 and 0987654321"
# number=re.findall("\d{10}",text)
# print(number)

# for match in re.finditer("\d{10}",text):
#     print("match found at index:",match.start(),"to",match.end())

# text="my phone number is 9492287323"
# masked=re.sub("\d{6}","XXXXXX",text)
# print(masked)

try:
    print("step1")
    a=int(input("enter numerator:"))
    b=int(input("enter denominator"))
    result=a/b
    print("Step2")
    print("result is",result)
except Exception as e:
    print("error:division by 0 is not allowed")
finally:
    print("execution completed")

