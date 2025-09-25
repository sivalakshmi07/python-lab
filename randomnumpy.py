#Write a program to create a NumPy array with 10 random integers and find their mean and standard deviation.
import numpy as np
arr=np.random.randint(1,10, size=10)
print("Array:",arr)
mean_value=np.mean(arr)
print("Mean:",mean_value)
std_value=np.std(arr)
print("Standard Deviation:",std_value)

