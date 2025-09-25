#Write a program that handles multiple exceptions: divide by zero, invalid input, and index out of range.
try:
    num1=int(input("Enter 1st number: "))
    num2=int(input("Enter 2nd number: "))
    result=num1/num2
    print("Result:",result)
    numbers=[10,20,30]
    index=int(input("Enter index (0-2): "))
    print("Value at index:",numbers[index])
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Invalid input.")
except IndexError:
    print("Index out of range.")