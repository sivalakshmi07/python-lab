a=[10,20,30,40,50]
try:
    index=int(input("Enter an index:"))
    value=a[index]
    divisor=int(input("Enter the divisor:"))
    result=value/divisor
    print("The result is",result)
except(IndexError,ZeroDivisionError)as e:
    print(e)