#arithmetic  operations using lambda
choice=int(input("1. Addition  2. Subtraction  3. Multiplication  4. Division"))2
a=int(input("Enter the first value:"))
b=int(input("Enter the second value:"))
if choice==1:
    print("sum is ",add(a,b))
    c=add(a,b)
elif choice==2:
    sub=lambda a,b: a-b
    print("diffrence is ",sub(a,b))
    c=sub(a,b)
elif choice==3:
    multi=lambda a,b: a*b
    print("Multiplication is:",multi(a,b))
    c=multi(a,b)
elif choice==4:
    divi=lambda a,b: a/b
    print("division is:",divi(a,b))
    c=divi(a,b)
else:
    print("INVALID")