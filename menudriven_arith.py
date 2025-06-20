choice=int(input("1. Addition  2. Subtraction  3. Multiplication  4. Division"))
num1=int(input("Enter the 1st number."))
num2=int(input("Enter the 2nd number."))
if choice==1:
    sum=num1+num2
    print("sum= ",sum)
elif choice==2:
    sub=num1-num2
    print("sub= ",sub)
elif choice==3:
    multi=num1*num2
    print("multi= ",multi)
elif choice==4:
    divi=num1/num2
    print("Division= ",divi)
else:
    print("Invalid.")