# Write a program to define a custom exception for invalid marks (e.g., negative or above 100) and raise it if the input is invalid.
class InvalidMarksError(Exception):
    pass
marks=int(input("Enter a mark: "))
try:
    if marks<0 or marks>100:
        raise InvalidMarksError
    print("Marks entered are:",marks)
except InvalidMarksError:
    print("Invalid marks!!.")
