#Write a program to create two matrices and perform addition, subtraction,multiplication, and transpose using NumPy.
import numpy as np
a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
print("Addition:\n",a+b)
print("Subtraction:\n",a-b)
print("Multiplication:\n",np.dot(a,b))
print("Transpose of A:\n",a.T)
print("Transpose of B:\n",b.T)
