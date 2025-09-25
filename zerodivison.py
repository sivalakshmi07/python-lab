#Write a program to handle ZeroDivisionError while dividing two numbers.
try:
    a = int(input("Enter the 1st number: "))
    b = int(input("Enter the 2nd number: "))
    print(a / b)
except ZeroDivisionError:
    print("Division by zero is not allowed")
