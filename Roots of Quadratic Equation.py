#Write a program to find roots of a Quadratric equation(handle complex roots too)
import math
a=float(input("ENTER VALUE FOR a: "))
b=float(input("ENTER THE VALUE FOR b: "))
c=float(input("ENTER THE VALUE FOR c: "))
qua=b**-4*a*c
root1=-b+(math.sqrt(qua))/2*a
root2=-b-(math.sqrt(qua))/2*a
print("QUADRATIC EQUATION 1 =",root1)
print("QUADRATIC EQUATION 2 =",root2)