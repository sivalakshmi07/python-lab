#Write a function to find the factorial of a number using recursion.
def factorial(n):
  if n==0 or n==1:
    return 1
  else:
    return n*factorial(n-1)
num=5
print("Factorial of",num,"is",factorial(num))