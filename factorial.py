#find factorial
a=int(input("enter a number"))
factorial=1
for i in range(1,a+1):
    factorial=factorial*i
print("Factorial is: ",factorial)