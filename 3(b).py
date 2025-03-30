import numpy as np
arr=np.array([10,20,30,40,50,60,70,80,90,100])
print("slicing example")
print("elements from index 2 yo 5",arr[2:5])
print("every second element from array:",arr[::2])
print()
print("Integer indexing example")
indices=[1,3,5,7]
print("elements at specified indices",arr[indices])
print()
print("boolean indexing example")
bool_id=arr>50
print("element greater than 50",arr[bool_id])
