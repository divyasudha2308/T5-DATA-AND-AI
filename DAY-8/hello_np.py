# import numpy as np
# numbers=[1, 2, 3, 4, 5]
# result = []
# for i in numbers:
#     result.append(i*1000)
# print(result)


# import numpy as np
# arr = np.arange(1, 25)
# arr = arr.reshape(2, 3, 4)
# print("Shape:", arr.shape)
# print(arr)


# arr = np.arange(1, 25).reshape(2, 3, 4)
# print(arr[0])
# print(arr[1][2][3])
# print(arr[:, 0, :])
# print(arr[:, -1, :])

# arr = np.arange(1, 25).reshape(2, 3, 4)
# print(arr[arr > 10])
# print(np.sum(arr % 2 == 0))
# arr[arr < 10] = 0
# print(arr)


import numpy as np
arr = np.arange(1, 25)
arr = arr.reshape(2, 3, 4)
print("Shape:", arr.shape)
print(arr)


image=np.random.randint(0,255,(64,64,3))
r=image[:,:,0] 
g=image[:,:,1] 
b=image[:,:,2] 
print(r)
print(g)
print(b)

print(d+10)
print(d*2)
print(d**2)
m=np.sum(d)
m=np.sum(d,axis=0)
m=np.sum(d,axis=1)
m=np.sum(d,axis=2)
print(m)